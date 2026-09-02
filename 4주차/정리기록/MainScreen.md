# MainScreen.tsx

- **대상 파일** `apps/frontend/src/screens/MainScreen.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/screens/MainScreen.tsx`)
- **PR** [#56](https://github.com/Scalmia/Zeteo/pull/56)

## ① 정의

> 게임 페이즈 내내 항상 떠 있는 단일 화면 — 채팅 + 투표. 기존 Describe·Debate·FinalDefense 세 화면을 하나로 합친 것.

292줄, 선언 2개(`MainScreen`, `phaseLabel`).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ❌ (292줄) — 다만 선언은 2개뿐 |
| 선언을 찾을 때 훑어야 하는가 | ✅ 걸림 — `phaseLabel`이 파일 맨 끝, `MainScreen`이 그걸 앞에서 씀 |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (아래, 추정) |

→ **커밋 2개.**

## ② 이동 — 재료 먼저, 진입점 마지막

`phaseLabel`(순수 헬퍼)이 파일 맨 끝에 있었다. [[room.md]](room.md)·index.ts에서 쓴 관례를 그대로 적용해 `MainScreen` 앞으로 옮겼다. 정렬 후 동일 확인(273줄, 함수 본문 무변경).

## 드러난 것 — FullscreenButton.tsx와 중복

전체화면 관련 state·effect·toggle 함수·SVG 아이콘 두 개(~35줄)가 `components/FullscreenButton.tsx`와 사실상 동일하다. 같은 날 FullscreenButton.tsx를 검토할 때 이미 Discord로 짚었던 의심(아래 참고)을, 이번에 MainScreen.tsx 쪽 코드를 직접 봐서 확정 확인한 것이다.

## 남긴 주석 — ⚠️ 추정 1건

| 위치 | 근거 |
|---|---|
| 전체화면 블록 위 | **추정.** `FullscreenButton.tsx`는 헤더 없는 화면에서 `position:absolute`로 카드 우상단에 얹는 용도(자기 헤더 주석)라, 이 파일의 헤더(`.zt-head`) flex 자식으로는 그대로 못 써서 따로 뒀을 것으로 추론. 두 파일 주석을 대조한 것이지 확인된 사실 아님. |

## ⚠️ 확인 필요

소유자(현우)가 요청자 본인. 다만 추정 주석 1건 — 맞으면 ※ 제거, 다르면 정정.

**참고 — FullscreenButton.tsx 기록 없음:** FullscreenButton.tsx는 2026-09-02 같은 세션에서 요청받았으나 판정 4문항이 안 걸려 "이 파일은 됐다"로 끝나 PR·기록이 없다. 그때 이미 이 중복을 짐작하고 Discord로만 짚었는데, 이번에 MainScreen.tsx 쪽에서 확정 확인했다.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
