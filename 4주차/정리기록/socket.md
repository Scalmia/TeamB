# socket.ts

- **대상 파일** `apps/frontend/src/net/socket.ts`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/net/socket.ts`)
- **PR** [#54](https://github.com/Scalmia/Zeteo/pull/54)

## ① 정의

> 소켓 연결 하나와, `action`/`event` 두 이벤트 이름으로 서버와 주고받는 유일한 통로.

21줄, export 3개(`socket`, `sendAction`, `onServerEvent`). 소유자 명시 없음(테이블에 `net/`이 없음) — `useGameState.ts`만 이 파일을 쓴다.

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (21줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 — 이미 사용 흐름(연결→보내기→받기) 순서 |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건, 추정) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — `autoConnect: false` 의 이유

`useGameState.ts`에 "socket.ts에서 autoConnect: false로 만들어져 있어서 여기서 명시적으로 연결"이라는 문장은 있지만, 그건 "false라는 사실"만 확인해줄 뿐 "왜 false여야 하는가"는 안 알려준다.

## 남긴 주석 — ⚠️ 추정 1건

| 위치 | 근거 |
|---|---|
| `io({ autoConnect: false })` 위 | **추정.** `useGameState.ts`의 이펙트가 `'connect'` 핸들러 등록 후 명시적으로 `connect()`를 부르는 것과 대조해 추론 — `autoConnect: true`였다면 모듈 로드 시점(React 이펙트보다 먼저)에 연결이 시작돼 핸들러 등록 전에 최초 `connect` 이벤트를 놓칠 수 있다는 것이 근거. 개발자가 명시적으로 남긴 이유가 아니다. |

## ⚠️ 확인 필요 — 민성님께 통보 (2026-09-02)

위 추정이 맞는지 확인 요청. `useGameState.ts` 재접속 로직을 최근 크게 손본 이력(`a6637b9 이름 중복 & 새로고침 수정`, 52줄 변경)이 있어 현우(요청자) 대신 민성님께 확인을 부탁했다. 맞으면 ※ 표시 제거, 다르면 정정 요청.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
