# Ambience.tsx

- **대상 파일** `apps/frontend/src/components/Ambience.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/components/Ambience.tsx`)
- **PR** [#50](https://github.com/Scalmia/Zeteo/pull/50)

## ① 정의

> Blood Moon 장식 레이어(핏방울 12개)를 렌더링한다. 클릭에 관여하지 않는다.

파일 머리에 이미 적혀 있던 문장 그대로. 22줄, export 1개(`Ambience`). 파트 D 소유 — 박진.

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (22줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 (export 1개뿐) |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — `<div className="blood-drop" />` 가 정확히 12번

이 파일만 보면 근거 없는 하드코딩으로 보인다. `apps/frontend/src/styles/ambience.css`를 확인하니 `.blood-drop:nth-child(1)`부터 `(12)`까지 각각 다른 `left`·`animation-delay`·`animation-duration`을 지정하고 있었다 — 두 파일의 12가 서로 맞춰야 하는 숫자였다. 늘리면 스타일 없는 방울이 생기고, 줄이면 안 쓰는 CSS 규칙이 남는다.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `<div className="blood-drops">` 위 | `ambience.css` 머리 주석에 이미 적혀 있던 내용을 옮김 |

## ⚠️ 확인 필요

없음. 소유자(박진) 확인 대기 중이나, 추정으로 쓴 부분이 없어 되돌릴 것도 없음.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
