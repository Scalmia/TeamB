# ResultScreen.tsx

- **대상 파일** `apps/frontend/src/ResultScreen.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/ResultScreen.tsx`)
- **PR** [#60](https://github.com/Scalmia/Zeteo/pull/60)

## ① 정의

> 결과 화면 — 승패·봇 색출·제시어 요약 + 정체 공개 목록.

164줄, 선언 2개(`TAG_CLASS`, `ResultScreen`).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (164줄, 선언 2개) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 — 이미 재료(`TAG_CLASS`) 먼저 |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — [[LandingScreen.md]]·[[LobbyScreen.md]]와 같은 패턴 (3번째)

`position: "relative"` 근거가 이 파일에 없어서 `FullscreenButton.tsx` 헤더 주석과 대조해 확인했다.

**참고 — 이 셋(Landing·Lobby·Result)이 전부 같은 패턴이라는 게 눈에 띈다.** FullscreenButton.tsx를 쓰는 헤더 없는 화면 전부가 부모 카드에 `position:relative`를 직접 걸어야 하는 구조라, 화면이 늘어날 때마다 이 요구사항을 또 놓치기 쉽다. 구조적으로 고칠 방법(예: FullscreenButton이 자기 wrapper를 스스로 relative로 감싸는 것)이 있을 수 있지만, 그건 리팩터링이라 cleanflow 범위 밖.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `position: "relative"` 위 | `FullscreenButton.tsx` 헤더 주석과 대조 확인 |

## ⚠️ 확인 필요

없음(추정 아님). 소유자(박진)에게는 참고로만 통보.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
