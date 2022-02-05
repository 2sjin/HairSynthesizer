# 헤어스타일 합성 프로그램<br>(Hairstyle Synthesizing Program)
내 얼굴 사진과 다른 사람의 헤어스타일을 합성하는, 인공지능(AI) 기반의 응용 프로그램

- 기여자: 이승진(팀장), 조준호, 이정훈, 조영현
- 프로젝트 수행 기간: 2021. 8. 2. ~ 2021. 8. 30.

## 다운로드(Download)
- 이 레포지토리 내의 모든 파일 다운로드
- [clovaai/stargan-v2](https://github.com/clovaai/stargan-v2) 내의 모든 파일 다운로드
- 위 두 파일을 동일한 경로(폴더) 내에 위치시킬 것

## 개요
![image](https://user-images.githubusercontent.com/91407433/152633507-7f0c19ff-dd20-449f-831a-d3cfa2e4200c.png)
- 자신의 얼굴과 다른 사람의 헤어스타일을 합성하는 인공지능을 탑재한 응용 프로그램
- ‘어떤 헤어스타일이 가장 아름다울까?’, ‘요즘 유행하는 이 헤어스타일이 내게도 어울릴까?’ 등과 같은 의문을 사진 두 장만으로 손쉽게 해결

## 사용 기술
- Python 3.7
- [STARGAN-v2](https://github.com/clovaai/stargan-v2)
- 주요 라이브러리: tkinter, numpy, openCV, pillow, pytorch

## 시스템 설계
![image](https://user-images.githubusercontent.com/91407433/152633300-1c3e95fd-f5be-4d48-a2ad-62f0f593bfe4.png)

## 학습 데이터 수집
- CelebA-HQ
  - JPG 이미지(1024x1024) 파일 30,000개
  - 서양인 사진 다수, 동양인 사진 일부

## 기계 학습 모델
- wing.ckpt (안면 인식 및 분리)
- 100000_nets_ema.ckpt (이미지 합성)

## GUI 구현
![image](https://user-images.githubusercontent.com/91407433/152633427-762a9184-034e-449f-9fca-15fc9b1fcb6d.png)

![image](https://user-images.githubusercontent.com/91407433/152633450-6b1a89d6-01af-4423-bf1c-0667fef87afc.png)

## 한계 및 보완 방법
- 다소 편향적인 특성의 학습 데이터 → 자연스러운 출력을 위해 더욱 다양한 데이터 수집
  - 특이한 헤어스타일 적용 시 부자연스러운 결과 출력
  - 동양인 사진 적용 시 부자연스러운 결과 출력
- 윈도우 PC 환경에서만 프로그램 실행 가능 → 모바일 및 웹 플랫폼 구축을 위한 전공 학습 수행
