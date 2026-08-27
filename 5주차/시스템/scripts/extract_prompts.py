# -*- coding: utf-8 -*-
"""세션 로그(.jsonl)에서 사용자 프롬프트만 뽑아 분석용 다이제스트를 만든다."""
import argparse
import io
import json
import os
import re
import sys
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

PROJECTS = os.path.join(os.path.expanduser("~"), ".claude", "projects")

# 되돌리기·재지시 신호. 프롬프트가 한 번에 통하지 않았다는 흔적이다.
REWORK = re.compile(r"아니|말고|다시|틀렸|잘못|왜 안|안 됐|안됐|원래대로|되돌려|취소|그게 아니")
# 실제 프롬프트가 아닌 시스템/훅 주입 메시지
NOISE = re.compile(r"^\s*<(system-reminder|local-command-stdout|command-message|user-prompt-submit-hook)")


def sessions():
    """subagent 로그를 뺀 모든 세션 로그를 용량 내림차순으로."""
    found = []
    for root, dirs, files in os.walk(PROJECTS):
        if os.path.basename(root) == "subagents":
            continue
        for f in files:
            if f.endswith(".jsonl"):
                p = os.path.join(root, f)
                found.append((os.path.getsize(p), p))
    return sorted(found, reverse=True)


def project_name(path):
    """로그 폴더명(C--Users-minwo-OneDrive----alsl-TeamB)에서 마지막 의미 있는 조각만."""
    parts = [p for p in os.path.basename(os.path.dirname(path)).split("-") if p]
    return parts[-1] if parts else "unknown"


def prompts(path):
    """사람이 실제로 친 프롬프트만 시간순으로. (tool_result·사이드체인·훅 주입 제외)"""
    out, skipped = [], 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") != "user" or d.get("isMeta") or d.get("isSidechain"):
                continue
            c = d.get("message", {}).get("content")
            if isinstance(c, list):
                # 이미지 블록은 base64라 통째로 버린다. tool_result만 있는 턴도 여기서 걸러진다.
                c = "".join(b.get("text", "") for b in c if b.get("type") == "text")
            if not isinstance(c, str) or not c.strip():
                continue
            c = c.strip()
            if NOISE.match(c):
                skipped += 1
                continue
            out.append((d.get("timestamp", ""), c))
    return out, skipped


def digest(path, cap):
    ps, skipped = prompts(path)
    sid = os.path.basename(path)[:-6]
    lens = sorted(len(t) for _, t in ps)
    n = len(ps)
    L = []
    w = L.append
    w("# 세션 프롬프트 다이제스트")
    w("")
    w("- 로그: `%s`" % path)
    w("- 프로젝트: %s / 세션ID: %s" % (project_name(path), sid))
    w("- 용량: %.1f MB / 저장 파일명: `%s_%s_개선점.md`" % (os.path.getsize(path) / 1e6, project_name(path), sid[:8]))
    if ps:
        w("- 기간: %s ~ %s" % (ps[0][0], ps[-1][0]))
    w("")
    w("## 기계적 신호 (해석은 직접 할 것)")
    w("- 사용자 프롬프트 %d개 (시스템/훅 주입 %d개 제외)" % (n, skipped))
    if n:
        w("- 길이: 중앙값 %d자, 최소 %d자, 최대 %d자" % (lens[n // 2], lens[0], lens[-1]))
        w("- 20자 미만 단문: %d개 (%.0f%%)" % (sum(1 for x in lens if x < 20), 100.0 * sum(1 for x in lens if x < 20) / n))
        w("- 되돌리기/재지시 신호어 포함: %d개" % sum(1 for _, t in ps if REWORK.search(t)))
        w("- 슬래시 명령: %d개" % sum(1 for _, t in ps if t.startswith("/") or t.startswith("<command-name>")))
    w("")
    w("## 프롬프트 전문 (각 %d자에서 자름)" % cap)
    for i, (ts, t) in enumerate(ps, 1):
        cut = t[:cap]
        tail = " …(%d자 더)" % (len(t) - cap) if len(t) > cap else ""
        w("")
        w("### %d. [%s] %d자%s" % (i, ts[:19], len(t), " ⟲재지시신호" if REWORK.search(t) else ""))
        w("```")
        w(cut + tail)
        w("```")
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", help="세션 .jsonl 절대경로. 없으면 목록만 출력")
    ap.add_argument("--list", action="store_true", help="용량 내림차순 목록")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--cap", type=int, default=700, help="프롬프트 1개당 표시 글자수")
    ap.add_argument("--out", help="다이제스트를 쓸 파일")
    a = ap.parse_args()

    if a.list or not a.path:
        for size, p in sessions()[: a.top]:
            mt = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
            print("%8.2f MB  %s  %-12s  %s" % (size / 1e6, mt, project_name(p), p))
        sys.exit(0)

    text = digest(a.path, a.cap)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote %s (%d chars)" % (a.out, len(text)))
    else:
        print(text)
