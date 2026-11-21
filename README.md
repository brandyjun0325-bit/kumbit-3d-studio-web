# 꿈빛 3D 게임 스튜디오 v3.8 (웹 배포판)

교육용 3D 게임 제작 웹앱 (지형 편집기, 재질 보관함, AI 지형·재질).

- 접속 주소: https://brandyjun0325-bit.github.io/kumbit-3d-studio-web/
- 배포 방식: `main` 브랜치의 `index.html`이 바뀌면 GitHub Actions가 스크립트 문법 검사 후 `gh-pages` 브랜치로 자동 배포합니다.

## 업데이트 방법
1. 새 버전 HTML 파일 이름을 `index.html`로 바꿉니다.
2. 저장소 → **Add file → Upload files** 로 업로드 후 Commit.
3. 1~2분 뒤 접속 주소에서 새로고침(Ctrl+F5).

## 참고
- three.js(0.160.0), PeerJS는 jsDelivr CDN에서 불러오므로 인터넷 연결이 필요합니다.
- 작업 데이터는 각 브라우저의 localStorage에 저장됩니다(서버 저장 없음).
- Gemini API 키는 사용자가 앱에서 직접 입력하며 저장소에 포함되지 않습니다.
