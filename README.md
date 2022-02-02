
<img src="/report/project5.png" alt="project_preview" width="100%">

# Balanchew : 머신러닝을 이용한 얼굴 특징점 분석을 통한 편측 저작 여부 추정

### 1. 기획 의도

음식을 섭취할 때, 습관적으로 한 쪽으로만 음식물을 씹는 사람이 많다. 하지만 지속적으로 한 쪽으로 음식물을 씹게 되면, 한쪽 치아와 안면 근육만을 사용하게 되어 안면 비대칭이 발생한다. 안면 비대칭 환자의 경우 치주 질환, 턱관절 장애, 두통 등 다양한 질환이 발생하기 때문에 이를 인지하고 예방해야 한다. 이에 본 연구에서는 신경망을 이용한 얼굴 특징점 분석을 통한 편측 저작(한쪽으로만 음식을 씹는 것)의 방향을 추정하였다.

### 2. 목차

1-1. Experiment Environment 및 Data Collection  
1-2. Video Processing  
1-3. Face Detection & Landmark Prediction  
1-4. 데이터 전처리  
    1-4-(1) 참여자 별 얼굴 크기 및 위치 정규화  
	1-4-(2) 데이터 필터링  
	1-4-(3) 좌표값 정규화  

2-1. 특징점 움직임 분석  
	2-1-(1) 특징점 좌표값 분석  
	2-1-(2) 특징점 이동거리 분석  
	2-1-(3) 특징점 벡터값 분석  
2-2. 좌, 우측 저작 운동의 벡터값 비교  
2-3. 머신러닝을 통한 저작 운동 방향 분류  
	3-3-(1) PCA(Principal Components Analysis)  
	3-3-(2) Feature Extraction  
	3-3-(3) SVM(Support Vector Machine)을 이용한 분류  
	3-3-(4) KNN(K-Nearest Neighbors)을 이용한 분류  
	3-3-(5) Decision Tree, Random Forest, Bagging을 이용한 분류  
    
---

## Final Report  

최종보고서 : ![balanchew-최종보고서.pdf](/report/balanchew-최종보고서.pdf)

### 일부 preview

![project_preview2](/report/report012.png) ![project_preview3](/report/report013.png) ![project_preview4](/report/report014.png)  
![project_preview5](/report/report018.png) ![project_preview6](/report/report019.png) ![project_preview7](/report/report023.png)  
![project_preview8](/report/report024.png) ![project_preview9](/report/report029.png) ![project_preview10](/report/report030.png)  