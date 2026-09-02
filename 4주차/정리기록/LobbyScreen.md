# LobbyScreen.tsx

- **대상 파일** `apps/frontend/src/LobbyScreen.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/LobbyScreen.tsx`)
- **PR** [#59](https://github.com/Scalmia/Zeteo/pull/59)

## ① 정의

> 대기실 화면 — 정원 슬롯 채우기, 준비 상태 표시, 준비 토글.

100줄, export 1개(기본 내보내기).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (100줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — [[LandingScreen.md]]와 같은 패턴

`position: "relative"` 가 왜 필요한지 이 파일엔 없었다. `FullscreenButton.tsx` 자기 헤더 주석("쓰는 쪽 카드에 반드시 있어야 한다")과 대조해 확인 — 확정 사실.

이 파일 나머지는 `var(--text-*)` 토큰을 전부 일관되게 쓰고 있어, LandingScreen.tsx에서 봤던 리터럴/토큰 불일치는 없었다.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `position: "relative"` 위 | `FullscreenButton.tsx` 헤더 주석과 대조 확인 |

## ⚠️ 확인 필요

없음(추정 아님). 소유자(박진)에게는 참고로만 통보.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
