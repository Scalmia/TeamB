# RoomListScreen.tsx

- **대상 파일** `apps/frontend/src/RoomListScreen.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/RoomListScreen.tsx`)
- **PR** [#61](https://github.com/Scalmia/Zeteo/pull/61)

## ① 정의

> 방 목록 화면 — 필터·정렬·방 만들기·방번호 직접입력. 닉네임 입력 뒤, 대기실 입장 전 단계.

309줄, 선언 4개(`RoomStatus`, `TITLE_MAX_LENGTH`, `STATUS_TAG`, `RoomListScreen`) — 가장 큰 파일이지만 이미 재료 먼저 순서.

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (309줄, 선언 4개, 이미 재료 먼저) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — [[LandingScreen.md]]·[[LobbyScreen.md]]·[[ResultScreen.md]]와 같은 패턴 (4번째, 완결)

`position: "relative"` 근거가 없어 `FullscreenButton.tsx` 헤더 주석과 대조해 확인했다.

**이걸로 FullscreenButton.tsx를 쓰는 헤더 없는 화면 넷(Landing·Lobby·Result·RoomList) 전부 같은 패턴이 확인됐다.** 구조적으로 고칠 여지(FullscreenButton이 자기 래퍼 `div`를 스스로 `position:relative`로 감싸는 것)가 보이지만 리팩터링이라 이 스킬 범위 밖 — 손대지 않음.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `position: "relative"` 위 | `FullscreenButton.tsx` 헤더 주석과 대조 확인 |

## ⚠️ 확인 필요

없음(추정 아님). 이 파일엔 소유 표시가 없어 같은 계열(박진)로 보고 참고 통보만 함.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
