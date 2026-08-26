# index.ts

- **대상 파일** `apps/backend/src/index.ts`
- **요청** 2026-08-26, 유민성 (`#cleanflow` 채널)
- **PR** [#41](https://github.com/Scalmia/Zeteo/pull/41)

## ① 정의

> 소켓 이벤트를 받아 방 상태를 바꾸고, 바뀐 상태를 참가자 각자에게 다시 보낸다.

서버 진입점. `export` 없음(정상).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ❌ 819줄, 함수 18개 순서 없음 |
| 선언을 찾을 때 훑어야 하는가 | ✅ 걸림 — `broadcastRoom`·`isDescribeComplete`·`maybeTriggerBot`이 첫 호출부보다 270줄 넘게 뒤에 정의 |
| 책임 한 문장 | 있음 |
| 안 드러나는 이유 | ✅ 걸림 |

→ 오늘 처리한 네 파일(content.ts·game.ts·survey.ts·index.ts) 중 유일하게 손볼 게 있었던 파일.

## ② 구역 5개

```
1. 서버가 켜진다        Express · Socket.IO · 상수
2. 판정과 기록          broadcastRoom · recordSpeak · 판정 함수들 · 로그/리포트 체인
3. 페이즈가 넘어간다     enterPhase · advancePhase (서로를 부른다)
4. 봇이 움직인다        maybeTriggerBot
5. 사람이 보내는 이벤트  io.on 전체 + 그 외 라우트 + 서버 시작
```

`io.on('connection', ...)` 스위치(300줄) 내부는 전혀 안 건드림 — 통째로 한 블록으로만 이동. 이유: 게임 흐름(`join → chat → describe → ready → listRooms → startGame → vote → lifeVote → guessWord → botVote → survey`)이 이미 맞고, 단일 statement 내부 절단은 위험이 더 큼.

## 드러난 구조 문제

- `enterPhase`/`advancePhase` 상호 재귀 — 페이즈 전이 자체가 두 함수가 번갈아 도는 루프라 완전한 선형 순서가 불가능. `startDescribeTurnTimer → maybeTriggerBot`도 같은 이유로 순방향 참조 하나 남음. 둘 다 원래 270줄 이상 떨어져 있던 게 20~25줄 이내로 좁혀짐.
- `export` 0건 — 진입점 파일이라 정상.
- 원래 순서도 완전 무작위는 아니었음(느슨한 의미 뭉치는 있었으나 leaf 함수가 뭉치 뒤쪽에 있어 참조 거리가 멀었음).

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| 파일 머리 | 신규 (책임 문장 + 구역 지도) |
| `enterPhase` 앞 | 순환 관계가 코드에서 직접 확인됨 — 왜 이 방향으로 뒀는지만 추가 |

## ⚠️ 확인 필요 — 판단 밖의 것

`PHASE_DURATIONS` 위 `TODO: 지금은 테스트용 임시값` — 기획서 v3.0 §6-2엔 실측값 확정으로 적혀 있어 낡은 TODO일 가능성. 손대지 않고 PR에서 확인만 요청함.

## ④ 활용

*(비어 있음 — 머지 후 실제 기능 추가해보고 자리가 자명했는지 덧붙일 것)*
