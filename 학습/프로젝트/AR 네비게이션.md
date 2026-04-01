https://gemini.google.com/share/9f08de93eee3
---

## 🎨 프론트엔드/모바일 관점 핵심 강조 포인트

[cite_start]가이드북에서 제시하는 프론트엔드 및 모바일 직무의 핵심 역량[cite: 822, 939]을 기반으로 본인의 경험을 다음과 같이 매칭하세요.

1.  [cite_start]**비주얼 & UI/UX 요소 및 가독성 [cite: 827, 829]**:
    * [cite_start]단순한 기능 구현을 넘어, 복잡한 대중교통 데이터를 어떻게 시각적으로 단순화했는지 강조하세요[cite: 828].
    * [cite_start]**적용**: "68분"을 "1시간 8분"으로 포맷팅하는 등 사용자 인지 부하를 줄인 경험[cite: 866].

2.  [cite_start]**렌더링 및 앱 성능 최적화 [cite: 830, 955]**:
    * [cite_start]모바일 환경에서 가장 중요한 메모리 관리와 반응성 개선 사례를 제시하세요[cite: 957].
    * [cite_start]**적용**: 10초 주기 폴링 최적화를 통한 배터리 소모 절감 및 Watchdog 메커니즘을 통한 서비스 복구 안정성[cite: 956].

3.  [cite_start]**상태(Data) 관리 전략 [cite: 834]**:
    * [cite_start]다양한 소스(GPS, API)에서 들어오는 비동기 데이터를 어떻게 일관되게 관리했는지 보여주세요[cite: 836, 837].
    * **적용**: Provider 기반의 아키텍처 설계 및 상태 머신(State Machine)을 활용한 여정 단계 자동 전환.

---

## 📄 포트폴리오 작성 내용 (Front-End/App Lead)

### 1. 프로필 (Profile)
* [cite_start]**슬로건 [cite: 685][cite_start]**: "사용자의 여정을 끝까지 책임지는 고신뢰도 프론트엔드 개발자" [cite: 687]
* [cite_start]**한 줄 소개 [cite: 690][cite_start]**: 실시간 위치 데이터 기반의 상태 제어 로직 구현에 강점이 있으며, 백그라운드 환경에서도 중단 없는 사용자 경험(UX)을 제공하는 앱 아키텍처 설계를 지향합니다[cite: 693, 696].

### [cite_start]2. 기술 스킬 (Technical Skills) [cite: 707]
* [cite_start]**Frontend/Mobile**: **Flutter (Expert)** - Provider를 활용한 복잡한 상태 관리 및 비동기 스트림 처리 숙련[cite: 712, 714].
* [cite_start]**App Optimization**: 안드로이드 포그라운드 서비스 구현 및 메모리 누수 방지를 위한 생명주기 관리 최적화[cite: 956].
* [cite_start]**Collaboration**: Git 기반의 코드 컨벤션 정립 및 방어적 프로그래밍 수행[cite: 809].

### [cite_start]3. 프로젝트 상세: 나 어디가 (AR 내비게이션 서비스) [cite: 762]

#### [cite_start]**① 프로젝트 개요 [cite: 764]**
* [cite_start]**배경**: 기존 2D 지도의 인지적 한계를 극복하고 대중교통 이용 시의 불안감을 해소하기 위한 AR 기반 서비스[cite: 765].
* [cite_start]**주요 기능**: 실시간 AR 경로 투영, AI 경로 추천, 스마트 승·하차 알림 및 단계별 여정 가이드[cite: 766].

#### [cite_start]**② 담당 역할 및 기여도 (Front-End / App Lead) [cite: 767, 785]**
* **실시간 여정 추적 및 상태 제어 시스템 구축 (기여도 40%)**:
    * [cite_start]상태 머신(State Machine)을 설계하여 [승차 전 - 탑승 중 - 하차 전] 단계를 자동 제어[cite: 769].
    * [cite_start]위치 계산 로직 최적화로 정확한 알림 시점 도출 및 배터리 효율 개선[cite: 807].
* **고신뢰 백그라운드 내비게이션 서비스 (기여도 35%)**:
    * [cite_start]**Foreground Service** 구현으로 앱 종료 시에도 안내 유지[cite: 848].
    * [cite_start]**Watchdog 메커니즘** 설계: 서비스 비정상 종료 시 10초 이내 자동 복구 로직 구현[cite: 881].
* **사용자 중심 UI/UX 고도화 (기여도 25%)**:
    * [cite_start]경로 카드 시각적 위계 재조정 및 시간 수치 가독성(68분 → 1시간 8분) 개선[cite: 825, 866].

#### [cite_start]**③ 문제 해결 및 개선 사례 (Performance Optimization) [cite: 797, 806]**
* [cite_start]**문제 인식 [cite: 811][cite_start]**: AR 및 카메라 상시 가동과 잦은 API 호출로 인한 급격한 배터리 소모 및 프로세서 발열 발생[cite: 813].
* [cite_start]**해결 방안 [cite: 814]**: 
    * **싱글톤 패턴**의 `ArCameraManager`를 구현하여 불필요한 객체 생성 방지.
    * [cite_start]앱 라이프사이클(Paused) 상태에 따른 카메라 자원 즉시 해제 및 복구 로직 적용[cite: 956].
* [cite_start]**개선 성과 [cite: 817]**: 
    * [cite_start]기존 대비 단위 시간당 배터리 효율 개선 및 안정적인 서비스 환경 구축[cite: 818].
    * [cite_start]비동기 호출 간 메모리 누수 전수 조사를 통해 런타임 크래시 방지[cite: 819].

---