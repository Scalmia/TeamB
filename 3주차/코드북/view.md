# 📖 `apps/backend/src/view.ts` 코드북

> 조사 시점 가장 최신인 `origin/dev` 기준 (98줄). `origin/feat/server`도 동일. `origin/feat/bot`은 로비 익명화·제시어 공개 수정이 아직 안 들어간 살짝 이전 버전.

<a id="n1"></a>
## 1. 시작 — 이 파일이 뭘 하는지 아시나요?

`buildGameStateFor(room, playerId)`. 방(room)의 진짜 상태 하나를 놓고, **플레이어마다 다른 결과**를 만들어내는 함수예요.

- **같은 방인데 사람마다 다른 화면을 받는다는 걸 이미 아신다** → [6번으로](#n6)
- **아니요, 처음 봅니다** → [2번으로](#n2)

---

<a id="n2"></a>
## 2. RoomInternalState vs GameState

서버는 방 하나당 진짜 상태(`RoomInternalState`)를 하나만 들고 있어요. 누가 봇인지, 누가 라이어인지, 제시어가 뭔지 — **전부 다 들어있는** 날것의 상태예요 (`room.ts`).

문제는 이걸 그대로 클라이언트에 보내면 안 된다는 거예요. `GameState`는 그 날것의 상태에서 **"이 사람에게 보여줘도 되는 것만"** 추려낸 결과물이고, `view.ts`가 그 변환을 담당해요.

▶ [3번으로](#n3)

---

<a id="n3"></a>
## 3. 왜 사람마다 다른 화면이 필요한가

라이어 게임이라 그래요. 라이어에겐 제시어를 숨겨야 하고, 봇은 정체가 끝까지 안 들켜야 해요. 5명이 같은 방에 있어도 **"내가 라이어인지 아닌지"에 따라 받는 정보가 달라야** 게임이 성립해요.

```ts
word: me.role === 'liar' && !isPostGame ? null : room.word,
```

라이어(`me.role === 'liar'`)면서 게임이 아직 안 끝났으면(`!isPostGame`) `word`를 `null`로 감춰요. 다른 사람은 그냥 `room.word` 그대로 받고요.

▶ [4번으로](#n4)

---

<a id="n4"></a>
## 4. 유출 금지 필드가 타입에 박혀있다

`shared-types`를 보면 플레이어 정보가 두 가지예요.

```ts
export interface InternalPlayer {
  isBot: boolean; // 유출 금지
  role: Role;     // 유출 금지
}
export interface PublicPlayer {
  id: string;
  label: string;
  isAlive: boolean;
  isReady: boolean;
}
```

`InternalPlayer`엔 `isBot`·`role`이 있고, 클라이언트가 받는 `PublicPlayer`엔 **아예 그 필드가 존재하지 않아요.** 타입 자체가 "이건 못 나간다"를 강제하는 구조예요.

▶ [5번으로](#n5)

---

<a id="n5"></a>
## 5. 누가 이 함수를 몇 번 부르는가

`index.ts`의 `broadcastRoom`이 방에 있는 소켓 수만큼 **반복해서** 이 함수를 불러요.

```ts
for (const socketId of socketsInRoom) {
  const meta = socketMeta.get(socketId);
  if (!meta) continue;
  const event: ServerEvent = { t: 'state', state: await buildGameStateFor(room, meta.playerId) };
  io.to(socketId).emit('event', event);
}
```

5명이 있으면 `buildGameStateFor`가 **5번** 불려서, 5개의 서로 다른 `GameState`가 각자에게 개별로 나가요. "한 번 계산해서 다 같이 보내는" 게 아니에요.

▶ [6번으로](#n6)

---

<a id="n6"></a>
## 6. 이 파일의 지도 ★

`buildGameStateFor` 하나가 하는 일 순서:

```
1. room.players에서 나(me) 찾기 — 없으면 에러
2. isPostGame / myPhase 계산        → 8번
3. publicPlayers 배열 만들기 (로비면 id·label 익명화) → 10번
4. GameState 객체 조립해서 return
   - 전원 공개 필드 (category, turnOrder, messages...)
   - 나만 보는 필드 (myRole, myVote, myId...)
   - 게임 끝나야 보이는 필드 (botVoteCorrectCount 등)   → 11번
```

**아는 사람이면 여기서 8~11번만 훑고 12번으로 가도 이 파일의 핵심을 다 봐요.**

- **survey가 result에서 갈라진 별도 phase라는 걸 아시나요?** → [9번으로](#n9)
- **모르겠습니다** → [8번으로](#n8)

---

<a id="n8"></a>
## 8. isPostGame · myPhase — 회귀 버그가 남긴 로직

```ts
// B-4: survey가 result에서 분리된 별도 phase가 되면서, "게임이 끝난 뒤"를 의미하던
// room.phase === 'result' 체크들이 survey로 넘어가는 순간 전부 false가 되어버린다.
const isPostGame = room.phase === 'result' || room.phase === 'survey';
const myPhase = room.phase === 'result' && room.surveyedIds.has(playerId) ? 'survey' : room.phase;
```

기획서 v3.0(§2)에서 설문이 결과 화면과 분리된 독립 phase가 됐어요. 그런데 원래 코드 곳곳에 "게임 끝났나?"를 `room.phase === 'result'`로만 체크하던 부분들이, 설문으로 넘어가는 순간 전부 `false`가 돼버리는 **회귀(regression)**가 생겼어요. 방금 공개됐던 봇 정체·라이어·승패가 설문 화면에서 다시 숨겨지는 버그였던 거예요.

`isPostGame`이 그 회귀를 막는 방패예요. `myPhase`는 조금 다른 문제를 풀어요 — `room.phase`는 방 전체가 공유하는 값(`result`)인데, 실제로는 **설문에 응답했는지가 사람마다 달라서** `room.surveyedIds`(누가 설문 화면으로 넘어갔는지 기록하는 `Set`)를 봐서 그 사람만 `'survey'`로 바꿔줘요.

▶ [9번으로](#n9)

---

<a id="n9"></a>
## 9. word 필드 — 라이어도 결국 제시어를 봐야 한다

```ts
// ★ A-4 수정: 게임이 끝난 뒤(result·survey)엔 라이어에게도 제시어를 공개해야 한다
// (기존엔 phase 조건이 없어서 게임이 끝나도 라이어는 제시어를 영영 못 봤다).
word: me.role === 'liar' && !isPostGame ? null : room.word,
```

3번에서 본 "라이어는 제시어를 못 본다"는 룰은 **게임이 진행 중일 때만** 맞는 말이에요. 게임이 끝나면(`isPostGame`) 라이어도 "아, 제시어가 이거였구나"를 알아야 하는데, 원래 코드엔 이 `isPostGame` 조건이 없어서 라이어는 게임이 끝나도 영영 제시어를 못 보는 버그가 있었어요. `!isPostGame` 조건 하나가 이 버그를 고친 흔적이에요.

▶ [10번으로](#n10)

---

<a id="n10"></a>
## 10. 로비 익명화 — id와 label을 몰래 바꿔치기

```ts
const publicPlayers: PublicPlayer[] = room.players.map((p) => ({
  id: room.phase === 'lobby' ? (room.lobbyTokens.get(p.id) ?? p.id) : p.id,
  label: room.phase === 'lobby' ? p.name : p.label,
  ...
}));
```

로비 단계에서만 두 가지가 달라져요:

- **id**: 평소엔 서버 내부 id(`p1`, `p2`...)를 그대로 쓰는데, 로비에서만 `room.lobbyTokens`에 저장된 무작위 토큰(`randomUUID()`, `room.ts`)으로 바꿔요.
- **label**: 평소엔 `p.label`(예: "참가자 3" 같은 익명 표시)인데, 로비에서만 `p.name`(실제 입력한 닉네임)을 그대로 보여줘요.

즉 로비에서는 "누구인지(닉네임)는 보여주되, 서버 내부 id는 감춘다"는 방향이에요 — 대기실에서는 서로 누가 들어와 있는지 알아야 하니까 닉네임은 공개하지만, 게임이 시작되기 전의 내부 id까지 그대로 노출할 이유는 없다는 판단으로 보여요. (이 부분은 코드에 별도 설명 주석이 없어서, `room.ts`의 `lobbyTokens.set(player.id, randomUUID())` 코드로부터 추론한 내용이에요.)

▶ [11번으로](#n11)

---

<a id="n11"></a>
## 11. 설계원칙 5 — 유출 금지 필드 묶음

```ts
// ★ 설계원칙 5 (봇 정보 유출 금지) — 아래 세 필드는 반드시 게임이 끝난 뒤(result·survey)에만
// 채운다. 한 단계라도 먼저 노출되면 개발자도구로 결과를 미리 볼 수 있게 된다.
botVoteCorrectCount: isPostGame
  ? Object.values(tallyBotVoteResults(room)).filter(Boolean).length
  : 0,
revealedBotId: isPostGame ? (room.players.find((p) => p.isBot)?.id ?? null) : null,
revealedLiarId: isPostGame ? (room.players.find((p) => p.role === 'liar')?.id ?? null) : null,
revealedNames: isPostGame ? Object.fromEntries(room.players.map((p) => [p.id, p.name])) : null,
botVoteResults: isPostGame ? { ...room.botVotes } : null,
```

다섯 필드 전부 같은 패턴이에요: `isPostGame`이면 진짜 값, 아니면 `null`/`0`. 그중 `botVoteCorrectCount`는 `vote.ts`의 `tallyBotVoteResults`를 불러서 계산하는데, 그 함수 내부를 보면:

```ts
// vote.ts
results[voterId] = !!target?.isBot;
```

**`p.isBot`(4번에서 본 그 유출 금지 필드)을 직접 읽어요.** 하지만 `view.ts`는 그 결과를 그대로 안 돌려주고 `.filter(Boolean).length`로 **몇 명이 맞췄는지 개수만** 뽑아내요 — "누가 맞췄는지"가 아니라 "몇 명이 맞췄는지"만 내보내는 거예요.

`botVoteResults`도 마찬가지예요. 봇 지목은 익명 투표라서, 게임이 끝나기 전에 이 값이 새면 "누가 나를 찍었는지" 투표 도중에 알게 돼서 익명성이 무너져요.

▶ [12번으로](#n12)

---

<a id="n12"></a>
## 12. 깨지면 무슨 일이 벌어지는가

이 다섯 필드 중 하나에서 `isPostGame ?` 조건을 빼먹으면 어떻게 될까요 — README가 이미 답을 갖고 있어요.

> 🔴 `isBot`·`role`은 절대 클라이언트로 나가지 않는다 — 상태 출구가 `apps/backend/src/view.ts`의 `buildGameStateFor` 한 곳으로 모여 있다. **이게 새면 개발자도구 한 번에 게임이 끝난다.**

예를 들어 `revealedBotId`의 `isPostGame ?`를 실수로 지우면, 게임 시작하자마자 모든 클라이언트가 `GameState.revealedBotId`로 봇의 정체를 받게 돼요. 브라우저 개발자도구 콘솔을 열어서 소켓 이벤트 하나만 찍어봐도 누가 봇인지 바로 보이는 거예요 — 라이어 게임의 전제 자체가 무너져요.

이 파일이 "상태 출구 한 곳"으로 불리는 이유가 이거예요. 유출 금지 필드를 다루는 곳이 여기 하나뿐이라, **여기 하나만 검토하면 유출 여부를 전부 확인할 수 있어요.**

▶ [13번으로](#n13)

---

<a id="n13"></a>
## 13. 바깥과의 계약

**누가 부르는가**: 5번에서 본 `index.ts`의 `broadcastRoom` 딱 하나 (`git grep`으로 확인 — 다른 호출부 없음).

**무엇을 약속하는가**: 반환 타입 `GameState`는 `shared-types`에 정의된 계약이에요. 기획서 v3.0(§6-1)에 따르면 이 타입은 v2.0 작성 당시 20개 필드에서 이틀 사이 네 번 바뀔 정도로 불안정했는데, 지금은 **26개 필드에서 멈춰있고 마지막 통합 병합에서 충돌이 0건**이었어요. `view.ts`가 그 26개 필드를 전부 채우는 유일한 곳이에요.

**왜 `async`인가**: 마지막 줄 때문이에요.

```ts
reasons: myPhase === 'survey' ? await fetchSurveyReasons() : [],
```

`fetchSurveyReasons`는 Supabase DB를 조회하는 비동기 함수예요(`db/survey.ts`). `broadcastRoom`은 방 상태가 바뀔 때마다(발언·투표 등) 매번 불리는데, 그때마다 DB를 조회하면 낭비니까 **`myPhase === 'survey'`일 때만** DB를 건드리도록 조건을 걸어놨어요.

---

<a id="n14"></a>
## 14. 도착 🏁

**이제 이걸 설명할 수 있습니다.**
- `view.ts`는 방의 진짜 상태(`RoomInternalState`, 봇·역할·제시어 다 포함) 하나를, 플레이어마다 다른 `GameState`로 개별 변환하는 **유일한 출구**다.
- `isPostGame`(게임이 끝났는가)이 거의 모든 분기의 기준이고, `myPhase`는 그중에서도 "이 사람이 지금 설문 화면에 있는가"를 개인별로 다시 조정한다.
- 봇·라이어 정체, 봇지목 결과처럼 유출되면 게임이 끝나는 정보는 전부 `isPostGame ?` 패턴 뒤에 숨어있고, 이 패턴이 하나라도 빠지면 README가 경고하는 "개발자도구 한 번에 게임이 끝난다"가 실제로 일어난다.
- `index.ts`의 `broadcastRoom`이 방 안 인원수만큼 이 함수를 반복 호출해서, "한 방 안에서도 사람마다 다른 화면"을 만든다.

### 더 볼 만한 곳
| 파일 | 이 파일과의 관계 |
|---|---|
| `apps/backend/src/room.ts` | `view.ts`가 읽는 `RoomInternalState`·`lobbyTokens`·`surveyedIds`의 원본 정의 |
| `apps/backend/src/vote.ts` | `tallyBotVoteResults`가 `isBot`을 직접 읽는 곳 — 11번에서 나온 그 함수 |
| `apps/backend/src/index.ts` | `broadcastRoom` — 이 파일을 부르는 유일한 곳 |
| `packages/shared-types/src/index.ts` | `InternalPlayer` vs `PublicPlayer`, `GameState` 26개 필드 계약 |

> 📌 이해가 안 된 노드가 있으면 **몇 번인지** #code-book 에 적어주세요. 그 노드를 쪼개서 다시 만듭니다.
