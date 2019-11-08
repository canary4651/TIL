# Confusion Matrix

![](Untitled-fa043667-7342-49b1-823f-09ac70dbaa6d.png)

- **Precision(정밀도), PPV(Positive Predictive Value)**
    - 모델이 True라고 분류한 것 중에, 실제 True인 것의 비율
- **Recall(재현율), Sensitivity, hit rate**
    - 실제 True 중에 모델이 True로 분류한 비율

- "Precision만 신경을 쓰면 모델이 인색해지고, Recall만 신경쓰면 모델이 헤퍼진다”
의 의미를 생각해보세요.
    - precision만 신경써서 너무 정확도만 맞추려고 하기 힘듬 (다 죽는다)
        - recall에만 신경 → 산 사람들은 다 살았다! 그럼 항상 recall이 1이겠지
- Accuracy
    - TP, TN을 모두 고려하는 지표.
    - Label 불균형이 심할 때에 사용을 주의해야 합니다.
        - ex) negative가 겁나 많은 데이터 (true가 없을 때) 다 negative라고 한다면 1이 되어버리겠지
        - 그래서 라벨이 0.99 이러면 accuracy로 쓰면 안 됨 (f1 socre 추천)
        - Label 불균형이 심할 때에, Accuracy는 지표로서 신뢰성을 잃습니다. 이유를 생각 해 보세요.

- F1 Score
    - Precision과 Recall의 조화평균Label 불균형이 심할 때에 모델의 성능을 정확하게 평가할 수 있습니다.

### 왜 산술 평균이 아니고 조화 평균인가?

- 라벨의 불균형이 심할 때, 더 정확하게 평가할 수 있음.
- 이유? 기하학적 해석 필요
- [https://sumniya.tistory.com/26](https://sumniya.tistory.com/26)

![](Untitled-6fb3cf33-21de-4a39-9549-a532ade575ea.png)

- 조화평균은 기하학적으로 다음과 같이 표현할 수 있습니다. 서로 다른 길이의 A, B의 끝에서 다른 쪽의 base라인으로 선을 내렸을 때, 만나는 점의 길이입니다
- 기하학적으로 봤을 때, 단순 평균이라기보다는 작은 길이 쪽으로 치우치게 된, 그러면서 작은 쪽보다도 작은 평균이 도출됩니다. 이렇게 조화평균을 이용하면 산술평균을 이용하는 것보다, 큰 비중이 끼치는 bias가 줄어든다고 볼 수 있습니다. 즉, F1-score는 아래와 같이 생각할 수 있습니다

![](Untitled-a7aecda9-8387-4595-b852-ac90e3e8e5c4.png)

- 무조건 작은 값보다(precision, recall)보다 f1 score가 더 작게 나옴. (p,r이 비슷하다고 해도!)

- 중요한 모델들은 별명이 하나씩 있음
- 가로 방향 (모델 중심) / 세로 방향 (정답 중심)

![](Untitled-74b716cf-ebad-48d7-a8c6-1eb1dbd4ce47.png)

- 히스토그램이 겹쳐 있을 수록, x축을 잘못 잡았다. 라고 생각
- 양쪽으로 떨어져있을 때, 뭔가 유의미한 변수를 잡았구나 라고 생각!

### 병 예측 모델 만들기

- 특정 threshold를 넘으면 병이 있다고 가정(기준치) - criterion

- threshold를 극단적으로 우측 이동?

    ![](Untitled-3e4f061f-7953-4394-9b72-21a63be7596a.png)

    - precision 이 올라가고(1) - 실제 병 걸린 사람 중 병 걸린 사람 , recall 값이 떨어짐  (병 걸린 사람 중 몇 %를 맞았냐)
    - Specificity:  올라감          Fall-out:     떨어져요 (1-sp니까)

    - threshold를 극단적으로 좌측 이동?

    ![](Untitled-c186baeb-127f-47a9-866d-ed54c1f77f8c.png)

    - true positive rate:   올라감  (1)    true negative rate:  내려감

    ## ROC curve

    - **간단하게는, Sensitivity와 1-Specificity를 각 축으로 하는 2차원 그래프**

    ![](Untitled-452acebc-60f9-4974-8962-93aee151a81f.png)

    ![](Untitled-a6d56d7a-7b7d-4a79-885d-3f1fbb93a6d1.png)

    - Actual True와 Actual False distribution이 완벽하게 같을 때 (feature의 class 변별능력 없음) ROC curve는 45도 각도 직선
    - 0.5 밑으로 내려가면 쓰레기 모델
    - 정규분포도가 완전히 겹쳐질때!
    - 무의미한 roc 커브

    ![](Untitled-4beb9519-a134-448a-988e-1d2b738350d8.png)

    ![](Untitled-5b5db257-d0cb-41b5-acd0-f8894632e71b.png)

    - **Actual True와 Actual False distribution이 겹치는 영역 없이 완벽하게 분리 될 때 ROC 커브 (feature의 class 변별 능력이 완벽)**
    - **ROC 커브가 좌상단에 가까울수록 feature의 class 변별 능력이 좋다고 할 수 있다.**

    - roc 커브 설명! (ㄱ자 그래프)

    ![](Untitled-80fad39a-721f-4bbf-a418-c4aa1bf79e33.png)

    - random forest 같은 예측 모델은 기본적으로 thresold를 0.5로 정해놓고 함

    - Classifier를 만든다는 건, 두 개의 histogram을 그리고 Threshold를 정의하는 것
    - Histogram을 그렸다는 건 ROC 커브를 그릴 수 있다는 것!
    - **ROC 커브를 그릴 수 있다는 건 여러 ROC 커브 간 비교를 통해 좋은 성능의 모델을 찾아낼 수 있다는 것!**

## **AUC가 크다**

**= 모델이 계산한 probability를 바탕으로 그린 histogram들이 잘 분리되어 있다.
= 모델이 Threshold(Decision Boundary라고도 한다)에 덜 민감하다.
= 안정적인 예측을 한다.**

## **모델 선택에 ROC 커브를 활용한다**

**= Decision Boundary에 상관없이 더 좋은 모델을 찾는다.
= ganzi가 난다.**

# **직접 그려봅시다.**

데이터: titanic

모델

- sklearn.linear_model.LinearRegression
- sklearn.linear_model.LogisticRegression
- sklearn.tree.DecisionTreeClassifier
- sklearn.ensemble.RandomForestClassifier
- 등 whatever you want

팁

- Tree 계열의 모델의 경우 model의 predict_proba() 메소드를 사용하면 확률 계산이 됩니다.
- 처음에는 Threshold를 a 만큼 이동해가며 Sensitivity, Specificity를 계산해 좌표를 구하세요.
- 어떻게 하면 Threshold를 잘 이동시키면서 ROC 좌표를 찍을 수 있을까요?
- 좌표들을 평면 상에 찍어보세요.

### **sklearn.metrics.roc_curve**를 활용 해 봅시다.

데이터: titanic

모델

- sklearn.linear_model.LinearRegression
- sklearn.linear_model.LogisticRegression
- sklearn.tree.DecisionTreeClassifier
- sklearn.ensemble.RandomForestClassifier
- 등 whatever you want

더 나아가서,

- sklearn을 이용해 AUC도 계산 해봅시다.
- 여러 모델들의 성능을 비교 해 봅시다.
- DecisionTreeClassifier를 사용했더라도, 사용한 feature가 다르다면 그건 다른 모델입니다.
- 타이타닉 말고, 다른 classification 문제에도 활용해 보세요.