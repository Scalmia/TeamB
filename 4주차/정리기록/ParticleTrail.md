# ParticleTrail.tsx

- **대상 파일** `apps/frontend/src/components/ParticleTrail.tsx`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/components/ParticleTrail.tsx`)
- **PR** [#53](https://github.com/Scalmia/Zeteo/pull/53)

## ① 정의

> 마우스를 따라가는 붉은 파티클 트레일. 50ms 쓰로틀. 파트 D(박진) 소유.

26줄, export 1개(`ParticleTrail`).

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (26줄) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 (export 1개뿐) |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (1건) |

→ 배치는 손댈 게 없음. 주석만 필요 — 이동 커밋 없이 **커밋 1개**로 처리.

## 드러난 것 — `particle.remove()` 타이머의 800

`ambience.css`의 `@keyframes zt-particle-fade` 가 `0.8s` — 정확히 같은 값(800ms)이었다. 애니메이션이 끝나기 전에 DOM에서 지우면 파티클이 페이드 도중 뚝 끊겨 사라진다. [[Ambience.md]](Ambience.md)(12개)·[[Button.md]](Button.md)(500ms)에 이어 세 번째로 발견된 같은 모양의 문제 — TSX의 매직 넘버가 CSS의 매직 넘버와 짝이 맞아야 하는데, 그 연결이 TSX 쪽에서는 전혀 안 보이는 패턴.

## ⚠️ 확인 필요 — 박진님께 통보 (2026-09-02)

이 파일과 `ambience.css` 헤더 둘 다 **"prefers-reduced-motion 사용자는 끈다"**고 적혀 있으나, `apps/frontend/src` 전체를 검색해도 실제 `@media (prefers-reduced-motion)` 규칙이 없다. 주석과 실제 동작이 어긋나 있다.

동작을 바꾸는 일이라 cleanflow 범위 밖 — 손대지 않고 박진-logs에 확인을 요청했다. 실제로 빠뜨린 구현인지, 계획만 있고 아직 안 만든 것인지는 박진님 확인 대기 중.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| `particle.remove()` 타이머 위 | `ambience.css`의 실제 `0.8s` 값과 대조해 확인 |

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
