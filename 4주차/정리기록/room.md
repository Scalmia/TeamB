# room.ts

- **대상 파일** `apps/backend/src/room.ts`
- **요청** 2026-08-21, 유민성 (`#cleanflow` 채널, `/cleanflow apps/backend/src/room.ts`)
- **PR** [#30](https://github.com/Scalmia/Zeteo/pull/30)

## ① 정의

> 한 판이 도는 동안 방 하나가 기억해야 할 것 전부와, 그것을 만들고 지우는 일.

한 문장으로 써진다 — 책임이 하나. 쪼갤 필요 없음.

## 판정

| | |
|---|---|
| 스크롤 없이 윤곽이 잡히는가 | ❌ (172줄, 12개 선언이 순서 없이 배치돼 있었음) |
| 선언을 찾을 때 훑어야 하는가 | ✅ 걸림 (`deleteRoom`이 파일 중간, `assignRoles`가 뒤쪽) |
| 책임을 한 문장으로 말할 수 있는가 | 있음 (위) |
| 안 드러나는 이유가 있는가 | ✅ 걸림 (7건) |

→ 구역 나누기 + 주석 둘 다 필요.

## ② 구역 5개 — 게임 순서

```
1. 방이 기억하는 것          RoomInternalState · rooms
2. 방이 생기고 사람이 모인다   createRoom · getRoom · joinRoom · ready 토글
3. 판이 시작된다             assignRoles · 라벨 배정
4. 판이 도는 동안            pushSystemMessage
5. 방이 정리된다             removePlayerFromLobby · deleteRoom
```

옮기면서 붙인 것: `markReady`/`unmarkReady`(토글 쌍) · `LABEL_POOL`/`assignLabel`(실제 사용처인 `assignLabels` 옆으로).

## 드러난 구조 문제

- `shufflePlayers`가 제거되면서 `players` 배열이 이제 입장 순서로 고정된다. `assignLabel`의 무작위 배정이 봇 위치(`players[0]`)를 안 새게 하는 유일한 방어선이다.
- export 12개 전부 다른 파일에서 최소 1번 이상 호출됨 — 안 쓰는 것 없음.

## 남긴 주석 — 전부 확인됨 (추정 0건)

| 위치 | 근거 |
|---|---|
| 파일 머리 | 신규 (책임 문장 + 구역 지도) |
| `abandonedSurveyIds` / `finalized` | `index.ts`의 `finalizeSurveyIfDone` 주석 |
| `pendingLiarGameResult` | `stateMachine.ts`의 `reveal`/`botVote` 주석 (포인터만, 중복 설명 안 함) |
| `markReady`/`unmarkReady` 분리 이유 | `index.ts:508-512` 실제 토글 코드 |
| `isEveryoneReady`의 `players.length > 0` | JS `every()` 언어 차원 사실 |
| `assignLabel` 무작위 이유 | `index.ts` case `'join'` (봇이 항상 `players[0]`으로 먼저 참가) |

## ⚠️ 확인 필요 — 됐음(2026-08-21)

민성님이 최근 `80896c5 room.ts 안내 주석 제거`로 설명 주석을 정리한 이력이 있어, PR에서 커밋 2(주석)를 선택적으로 되돌릴 수 있음을 명시함. 커밋 1과 독립적으로 분리돼 있어 가능.

## ④ 활용

*(아직 비어 있음 — PR 머지 후, 이 파일에 실제로 코드를 추가해보고 새 자리가 자명했는지 여기 덧붙일 것)*
