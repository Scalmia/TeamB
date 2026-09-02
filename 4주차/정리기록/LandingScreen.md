# LandingScreen.tsx

- **대상 파일** `apps/frontend/src/LandingScreen.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/LandingScreen.tsx`)
- **PR** [#58](https://github.com/Scalmia/Zeteo/pull/58)

## ① 정의

> 닉네임을 입력받는 랜딩 화면.

66줄, export 1개(기본 내보내기).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (66줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 (export 1개) |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (2건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 1 — `position: "relative"` (확정)

`FullscreenButton.tsx` 자기 헤더 주석에 "쓰는 쪽 카드에 `position:"relative"`가 반드시 있어야 한다"고 적혀 있다. 이 카드가 그 요구를 충족시키는 자리였는데, 이 파일 쪽에는 근거가 없었다.

## 드러난 것 2 — 폰트 크기 불일치 (⚠️ 추정)

입력창 `fontSize: 21` 이 `tokens.css`의 `--text-button`(21px)과 같은 값이다. 바로 아래 `<Button>` 은 토큰을 쓰는데 입력창만 리터럴 — 의도인지 우연인지 코드만으론 판단 불가.

## 남긴 주석 — 확정 1건, 추정 1건

| 위치 | 근거 |
|---|---|
| `position: "relative"` 위 | **확정.** `FullscreenButton.tsx` 헤더 주석과 대조 확인 |
| `fontSize: 21` 위 | **추정.** `--text-button` 값과 우연히 일치 — 의도 불명, 소유자 확인 필요 |

## ⚠️ 확인 필요 — 박진님께 통보 (2026-09-02)

폰트 크기 건. `--text-button` 이 바뀌면 이 입력창만 안 따라간다는 점을 확인 요청. 손대지 않음 — 리터럴을 토큰으로 바꾸는 건 지금은 결과가 같아도 실질적 코드 변경이라 cleanflow 범위 밖.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
