---
날짜: 2026-08-12
주제: Next.js
이유: 서버쪽에서 next js를 사용한다고 하는데, 어떤 역할이고, 어떤 식으로 사용되고 있는지 모르겠음.
---

## 기본설명

Next.js는 React 위에 얹는 프레임워크로, React만으로는 직접 구성해야 하는 것들(라우팅, 서버에서 미리 화면을 그려서 보내는 렌더링, API 엔드포인트 등)을 프레임워크 차원에서 대신 처리해준다. 대표적으로 두 가지가 핵심이다:

1. **파일 기반 라우팅** — `app/` 폴더 안에 폴더·파일을 만들면 그게 곧 URL 경로가 됨. 라우터 설정 코드를 따로 안 써도 됨.
2. **서버 사이드 렌더링(SSR)** — 브라우저가 빈 HTML을 받아서 JS로 그때부터 화면을 그리는(CSR) React 기본 방식과 달리, Next.js는 서버에서 미리 완성된 HTML을 만들어 보낼 수 있어서 초기 로딩이 빠르고 검색엔진 최적화(SEO)에도 유리함.

즉 "Next.js를 쓴다"는 건 React 프론트엔드를 만들면서, 그 프론트엔드를 서비스하는 방식 자체를 Next.js가 제공하는 서버(Node.js 기반)에 맡긴다는 뜻이다.

## 우리 프로젝트에서의 활용처

**결론부터: Zeteo 코드베이스 어디에서도 Next.js가 쓰이는 근거를 찾지 못했다.** 지어내지 않고 조사 과정을 그대로 남긴다.

조사 방법:
1. `git fetch origin`으로 원격 참조 최신화 후, `origin/main`·`origin/dev`·`origin/feat/bot`·`origin/feat/server`·`origin/feat/game-ui`·`origin/feat/layout` 전체 브랜치를 대상으로 `next` 관련 키워드(`"next":`, `from 'next`, `next.config`, `next dev/build/start`, `getServerSideProps`, `app/layout` 등)를 `git grep`으로 검색 — 전 브랜치 매칭 0건.
2. 모든 브랜치의 `apps/frontend/package.json`, `apps/backend/package.json`, 루트 `package.json`을 직접 열어 의존성 목록 확인 — `next` 패키지는 어디에도 없음.
3. `origin/main`의 `README.md`를 확인한 결과, 프로젝트 구조가 이미 명시적으로 문서화되어 있었음:
   - `apps/backend/src/index.ts` — **게임 서버**. `express` + `socket.io` 기반 Node.js 서버(→ [[웹소켓]] 참고). "게임 상태를 들고 있고 봇도 여기 산다"고 README에 직접 쓰여 있음.
   - `apps/frontend/` — **Vite 개발 서버**. "React 파일을 브라우저에 배달만 함"이라고 README에 명시. `package.json`의 `dev` 스크립트도 `"vite"`.

**추정**: 아마 "서버쪽에서 Next.js를 쓴다"는 이야기는 "서버쪽에서 **Node.js**를 쓴다"의 착오일 가능성이 높다. 두 이름이 비슷하고(Next.js도 Node.js 위에서 동작하는 프레임워크라 개념적으로도 헷갈리기 쉬움), 실제로 백엔드가 Node.js(Express)로 돌아가는 건 맞기 때문이다. 다만 이건 코드로 확인된 사실이 아니라 추정이므로, 정확한 출처(누가 언제 그렇게 말했는지)를 다시 확인해보는 게 좋다.

## 퀴즈

1. Next.js가 일반 React 앱과 다르게 제공하는 대표적인 기능 두 가지는?
   - 정답: 파일 기반 라우팅, 서버 사이드 렌더링(SSR) (해설: React 자체는 라우팅·렌더링 방식을 직접 구성해야 하는데, Next.js는 이 두 가지를 프레임워크 차원에서 제공한다.)

2. Zeteo의 `apps/frontend`는 실제로 무엇으로 개발 서버를 띄우나?
   - 정답: Vite (해설: `package.json`의 `"dev": "vite"` 스크립트와 README의 "Vite 개발 서버" 명시로 확인됨. Next.js 의존성은 어느 브랜치에도 없음.)

3. Zeteo의 `apps/backend`는 무엇으로 만들어져 있나?
   - 정답: Node.js + Express + Socket.IO (해설: `package.json` dependencies에 `express`, `socket.io`가 있고 Next.js는 없음. "서버가 Next.js"라는 말은 "서버가 Node.js"의 착오였을 가능성이 큼.)

4. 이번 조사에서 "찾지 못했다"는 결론을 내리기 전에 확인한 범위는 어디까지인가?
   - 정답: `origin`의 전체 원격 브랜치(main/dev/feat/bot/feat/server/feat/game-ui/feat/layout) 전부의 코드와 의존성 목록, 그리고 README (해설: 로컬에 체크아웃된 브랜치 하나만 보면 다른 팀원 브랜치의 변경을 놓칠 수 있어서, study-note 스킬은 항상 전체 원격 브랜치를 조사 대상으로 삼는다.)
