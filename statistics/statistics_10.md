# statistics_10

# 차원 축소  Dimensionality Reduction

- 데이터에서 차원 = 변수의 수
- 차원이 크면
• 시각화가 어려움 (대부분 시각화는 2차원)
• 이해하기 어려움 (사람이 생각할 수 있는 차원에는 한계)
• 분석하기 어려움 (차원이 클 수록 과적합이 일어나기 쉬움)
- 차원 축소: 차원을 줄이는 다양한 기법들 (변수를 줄이는 방법들)
    - 보통 2차원인데 3차원, 4차원으로 갈 수록 분석하기 어렵고 눈에 잘 안들어옴

## 차원 축소로서 평균 점수

- 여러 과목의 점수를 평균 내어 점수내는 것도 일종의 차원 축소
- 과목이 많으면 → 점수가 많아짐 → 이해/비교하기 어려움
- 평균을 내면 → 점수가 하나로 줄어듦 → 이해/비교하기가 쉬움
- 가중치를 두기도 함 → 근거는???

## 선형 모형을 이용한 차원 축소

- 𝑋 = 𝑊𝑍
- y = ax (관찰)
    - x (관찰) = wz (잠재) 
    • 관찰된 데이터 X
    • 잠재 변수 Z
    • 계수 W

## 주성분 분석 Principal Component Analysis

- 축을 회전시켜 새로운 축(성분)을 찾아내는 방법
- 분산이 큰 순서대로 성분을 정함
- 분산이 작은 성분들을 제거하여 차원을 축소
- PCA 논리
    - 2차원 데이터는 움직일 수 있는 방향이 2개 → 어느 쪽으로 움직이냐? → 제일 큰 방향만 남기고 나머지는 지워서 1차원 데이터로 만들자
    - 실습 통계10 파일 참고
- 가장 큰 단점 : 계수 해석이 어려움 - (-)가 나온다? 사실 존재 하지 않는 변수를 가지고 해석하는 거기 때문에 , 계수 해석이 어려움 그래서 나온 방법이 밑에 있는 방법!

![](Untitled-11776a75-2cae-4ac9-b935-709d16eb8e8a.png)

## NMF Non-negative Matrix Factorization

- 하나의 데이터 X를 가중치 W와 점수 H의 곱으로 쪼갬(factorize)

    =  원 데이터를 계수와 변환된 데이터로 쪼갠다

- 이때 W와 H는 모두 ≥0 (non-negative)
- PCA에 비해 점수의 해석이 좀 더 쉬움 **(음수가 나오지 않으므로)**
- 양수라서 좋은 점? - 직관적이고 크기만 비교하면 되므로
- 원데이터를 보존하지는 않음 (원래 데이터를 잘 보존하고 싶으면 pca)
- 컴포넌트가 몇 % 이다 설명하기 어렵지만 그래도 점수 해석이 쉽다
    - 그렇지만 nmf는 해석자의 의도를 반영하기 어렵다.
    - 그래서 두둥! 오늘의 주인공 `요인분석` 이 나옴

## 요인 분석 Factor Analysis

- 주성분 분석과 비슷(성분 = 요인) - 잠재 요인을 곱해서 원 데이터가 나오도록 하는 거
    - 요인 분석 - 탐색적 요인 분석, **확인적 요인 분석**
- 점수보다 **계수를 해석**하는데 관심
- 요인 = comp(컴포넌트) 다 같은 말
- n_component == n_facotors

## 탐색적 요인 분석 Exploratory FA

- 모든 요인이 관찰변수에 영향을 주는 것으로 분석 후
- 단순한 구조를 가지도록 회전(rotation)을 적용 (또는 요인 회전이라고 불림)
- 회전 - 요인이 특정한 이론적 구조를 가지도록 변환해줌
- 직교 회전: 요인들이 서로 독립(varimax, quartimax)
- 사교 회전: 요인들이 서로 독립이 아님(oblimin, promax)

## 공통성 Communality

- 회귀분석에서 R제곱과 동일
- 한 관찰변수의 분산 중 잠재변수들에 의해 설명되는 비율
- 유일성(uniqueness) = 1 – 공통성
- 공통성의 최대값은 1이나 여러 가지 계산 오류로 1보다 클 때도 있음
• 발견자의 이름을 따서 Heywood case라고 함
• 모형을 수정하거나, 데이터를 추가, 또는 변수를 삭제

## 확인적 요인 분석 Confirmatory FA

- 요인 구조를 **분석가가 정하고 실시**
- 잠재변수를 이용한 회귀분석

— 오늘 선생님 코드 변경된 게 많으니까 다시 다운 받아서 보기 

# 복습테스트

1. 종속변수 y를 독립변수 x와 m으로 예측하고자 합니다. 이때 m은 0 또는 1의 값을 가집니다. 그림과 같이 m에 따라 x의 절편이 달라지는 모형을 만들려면 statsmodels에서 어떻게 입력해야 합니까? *

![](https://lh5.googleusercontent.com/-IzT-Ov1sRjFP4dXnnzsQHk0DPZ3t2tiDTpF6htbKoKw8lpEB0Qr1yDqFgl-xqDndiCcmMzV_ivl_gg6iVw0Zhn3mbhGiv8PBKGPId3D2FTRPjz4Ak0fxqKBMCym=w562)

**y ~ x + m**

y ~ x * m

y ~ x:m

y ~ x + x:m

2. 종속변수 y를 독립변수 x와 m으로 예측하고자 합니다. 이때 m은 0 또는 1의 값을 가집니다. 그림과 같이 m에 따라 x의 기울기가 달라지는 모형을 만들려면 statsmodels에서 어떻게 입력해야 합니까? *

![](https://lh6.googleusercontent.com/Iw_e3QFzVLhX7ajiAl4NFbeMW0sl-uUcJIK5wURms4jIh_dTyXC3ezE1cOyXd2b7SiAJUYBeNcr4ZtfoDYkAkwNw29pAy50QGDHZOhlIJS-qjlJ2FaC8BTSB_RwY=w714)

     y ~ x + m

y ~ y * m

y ~ x:m

y ~ x + x:m

= y = ax + bxm + c

3. 종속변수 y를 독립변수 x와 m으로 예측하고자 합니다. 이때 m은 0 또는 1의 값을 가집니다. 그림과 같이 m에 따라 x의 절편과 기울기가 모두 달라지는 모형을 만들려면 statsmodels에서 어떻게 입력해야 합니까? *

![](https://lh3.googleusercontent.com/jFTGZwOrf0iIg3w4C9q3rsxPdS3M9x-jW0jb79r2z51Xo6BDTEzv4o6L1A_b8j9E6tjTo7oAvr1lZIha5FEjODUnV2up9_O2HlEyJT3zI3k5YwUZr7lnk-hrtMgy=w696)

     y ~ x + m 

y ~ x * m (곱하기가 아니라 축약표현 +랑 x 다 해주는 거) 

y ~ x:m

y ~ x + x:m

y = x + m + xm  → 축약표현 * 

4. 3가지 모형으로 회귀분석을 하였습니다. 각 모형의 AIC가 다음과 같을 때 가장 성능이 높은 모형을 골라 보세요. *

AIC = 100

AIC = 200

AIC = 300

5. 로지스틱 회귀분석을 하여 예측을 했을 때, 실제 값과 비교한 혼돈 행렬이 아래와 같았습니다. 여기에서 정확도(accuracy)는 얼마입니까? *

![](https://lh4.googleusercontent.com/tSG_nExUDfMnI1ZzgpVw3tU3pBssB9RDPEk214HFHgpWPajHtlh8u2sPu1_fAVxGCcMI63707lkx2hnfpNbTIJtLMc1iP3vv16KpPMC188wo0tiP40ucwtQQ1up-=w740)

      10%

40%

65%

80%

6. 로지스틱 회귀분석을 하여 예측을 했을 때, 실제 값과 비교한 혼돈 행렬이 아래와 같았습니다. 여기에서 정밀도(precision)는 얼마입니까? *

![](https://lh4.googleusercontent.com/tSG_nExUDfMnI1ZzgpVw3tU3pBssB9RDPEk214HFHgpWPajHtlh8u2sPu1_fAVxGCcMI63707lkx2hnfpNbTIJtLMc1iP3vv16KpPMC188wo0tiP40ucwtQQ1up-=w740)

     10%

40%

65%

80%

양성 합 10+40 중 40 맞음 

7. 로지스틱 회귀분석을 하여 예측을 했을 때, 실제 값과 비교한 혼돈 행렬이 아래와 같았습니다. 여기에서 재현도(recall)는 얼마입니까? *

![](https://lh4.googleusercontent.com/tSG_nExUDfMnI1ZzgpVw3tU3pBssB9RDPEk214HFHgpWPajHtlh8u2sPu1_fAVxGCcMI63707lkx2hnfpNbTIJtLMc1iP3vv16KpPMC188wo0tiP40ucwtQQ1up-=w740)

10%

40%

65%

80%

실제 양성 합(60+40) 중 내가 맞은 거 40%

8. 다음 중 ROC 곡선에 대한 설명으로 옳은 것을 모두 고르세요. *

문턱값(threshold)에 따라 변하는 FPR과 TPR의 관계를 나타낸 것이다

ROC 곡선의 곡선 아래 면적(AUC)은 모형의 성능 지표로 사용할 수 있다

AUC는 높을 수록 좋다

무작위로 예측했을 때 AUC는 0이다. → 0.5이다. 

9. 표준화(standardization)에 대한 설명으로 옳은 것을 모두 고르세요. *

모든 값에서 평균을 빼고, 표준편차로 나누는 것이다

표준화 후에는 변수의 평균이 0이 된다

표준화를 하는 이유는 변수간에 단위를 일정하게 하기 위해서이다

k-Means 등 거리를 바탕으로 한 클러스터링을 할 때 변수들의 영향력을 모두 같게 만들기 위해 표준화를 한다

변수를 표준화하면 표준정규분포를 따른다 → 아님 정규분포를 해야만 정규분포가 나옴 

10. k-Means 클러스터링에 대한 설명으로 옳은 것을 모두 고르세요. *

한국식 클러스터링이다. 일본식 클러스터링은 J-Means라고 한다.

비슷한 고객들끼리 묶는데 사용할 수 있다.

클러스터의 수를 분석자가 지정해야 한다.

클러스터의 평균점(중심점)을 기준으로 데이터들이 밀집되어 있는 경우에 유용하다.

11. DBSCAN에 대한 설명으로 옳은 것을 모두 고르세요. *

일정 거리(ε) 내에 N개 이상의 사례가 있으면 핵심점(core point)으로 지정한다.

서로 일정 거리(ε) 내에 있는 핵심점들을 같은 클러스터로 합친다.

클러스터의 수를 분석가가 지정하지 않아도 된다.

데이터들이 밀집되어 있지 않고 이웃에 이웃으로 길게 이어져 있는 형태일 때 유용하다.

다양한 클러스터링 지표에서 k-Means보다 DBSCAN이 더 높게 나오는 경향이 있다. → 아님 모든 지표가 다 k-means에 맞게 설정되어있음