# Button.tsx

- **대상 파일** `apps/frontend/src/components/Button.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/components/Button.tsx`)
- **PR** [#51](https://github.com/Scalmia/Zeteo/pull/51)

## ① 정의

> 공용 버튼. variant(primary/secondary)·block 폭과, 클릭 시 리플 효과를 담당한다.

21줄, export 1개(`Button`, default). 소유: 이현우(요청자 본인, `components/`).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (21줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 (export 1개뿐) |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — `setTimeout(... , 500)` 의 500

이 파일만 보면 근거 없는 숫자로 보인다. `apps/frontend/src/styles/tokens.css`를 확인하니 `.btn::before { transition: all 0.5s ease; }` — 정확히 같은 값(500ms = 0.5s)이었다. `btn-ripple` 클래스를 계속 붙여두면 트랜지션이 끝난 채로 멈춰 있어 빠르게 재클릭해도 리플이 다시 안 터진다. 500ms 뒤 클래스를 떼는 것이 다음 클릭에서 처음부터 다시 재생되게 하는 유일한 방법이다.

Ambience.tsx의 "12개 하드코딩" 건과 같은 모양의 문제 — TSX의 매직 넘버가 CSS의 매직 넘버와 짝이 맞아야 하는데 그 연결이 TSX 쪽에서는 안 보이는 패턴.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `rippling` state 선언 위 | `tokens.css`의 실제 `transition: all 0.5s` 값과 대조해 확인 |

## ⚠️ 확인 필요

없음. 소유자(현우)가 요청자 본인.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
