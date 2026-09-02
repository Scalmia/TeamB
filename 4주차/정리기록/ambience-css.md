# ambience.css

- **대상 파일** `apps/frontend/src/styles/ambience.css`
- **요청** 2026-09-02, 이현우 (`#cleanflow` 채널, `/cleanflow apps/frontend/src/styles/ambience.css`)
- **PR** [#57](https://github.com/Scalmia/Zeteo/pull/57)

## ① 정의

> **둘.** Ambience.tsx(Blood Moon 핏방울, `.blood-drop*`)와 ParticleTrail.tsx(마우스 트레일, `.zt-particle`). 파트 D(박진) 소유.

74줄. 헤더가 원래 Ambience.tsx 하나만 언급하고 있었다.

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ✅ 잡힘 (74줄, 두 그룹이 빈 줄로 이미 나뉨) |
| 선언을 찾을 때 훑어야 하는가 | ❌ 아님 |
| 책임을 한 문장으로 말할 수 있는가 | ❌ **없음** — 헤더가 절반만 말하고 있었음 |
| 안 드러나는 이유가 있는가 | (기존 발견은 [[ParticleTrail.md]]에서 처리 중) |

→ 배치는 손댈 게 없음. **헤더 주석 확장 1건** — 커밋 1개.

## 드러난 것 — 헤더가 책임 절반을 안 밝히고 있었다

"Blood Moon 장식 레이어(피 방울). Ambience.tsx가 마운트하는 마크업을 스타일링한다"고만 적혀 있었는데, 파일 안엔 `.zt-particle`(ParticleTrail.tsx 전용)도 있다. 헤더만 보면 이 파일이 Ambience.tsx 하나만 담당하는 것처럼 보인다.

## 남긴 것 — 헤더 문장 확장 (추정 아님, 코드로 확인)

| 위치 | 내용 |
|---|---|
| 파일 머리 | Ambience.tsx만 언급하던 문장을 Ambience.tsx + ParticleTrail.tsx 둘 다 언급하도록 확장 |

## ⚠️ 확인 필요 — 박진님께 통보 (2026-09-02)

소유자가 박진님이라 별도 통보. 같은 헤더의 "prefers-reduced-motion 사용자는 끈다" 건은 [[ParticleTrail.md]]에서 이미 확인 요청해둔 것과 동일 — 이 PR에서 다시 안 건드림, 여전히 확인 대기 중.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
