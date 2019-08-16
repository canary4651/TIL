# PYTHON3_09

- github
- module : 그냥 file을 만드는 순간 module이 된다
- import : 의존성
- from - import
- library
- pip install
- [파이썬9번](https://docs.google.com/document/d/1RLcgSx2tFV70oNd-t0H1nZS0gi6tAqCxeS7Bsq23Iak/edit) : pycharm에서 pandas 불러오기
    - score_test / score/ dataframe.py 파일 참조
    - 파일을 깃헙에 올릴 땐 원본-테스트 파일을 같이 올려야 다운 받을 때도 돌아간다는 사실~!

- conditional branch : 조건문
    - 50점 이상인 점수들을 모아보자
    - bool / and/ or /
    - 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 불 자료형은 다음 2가지 값만을 가질 수 있다.
        - True - 참
        - False - 거짓

        if condition:
        	do_something()
        

## 둘 중 작은 숫자 얻기

    # less number 함수 test 파일에다가 
    
    from 파일이름 import less_number 
    # 만약 원본 파일을 다른 폴더로 옮겼다면? (예시 : moduel 폴더 안에 옮겼다고 가정) 
    # from **moduel.**파일이름 import less number
    # 앞에 폴더이름과 .을 해주면 됨 
    
    # 1. Test-first
    def test_less_number():
        assert less_number(10, 20) == 10
        assert less_number(20, 10) == 10
    
    # less number 함수 만들어진 파일 
    
    # 2. Implement
    def less_number(x, y):
        if x < y:
            return x # x가 y보다 작으면 x 리턴
        return y # x가 y보다 크면 y 리턴 

## 50점 이상인 점수 리스트 얻기

    # 쉬운 예시 (score만 들어간 예시) 
    # 1. Test-first
    from first import select_high_scores
    
    def test_select_high_scores():
        assert select_high_scores([])== []
        assert select_high_scores([60, 50]) == [60]
        assert select_high_scores([60, 40, 50]) == [60]
        assert select_high_scores([60, 40, 50, 50]) == [60]
        assert select_high_scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 70, 80, 90, 100]
    
    # 2. Implement
    
    def select_high_scores(scores):
        high_scores = []
        for score in scores:
            if score >= 60:
                high_scores.append(score)
        return high_scores
    
    
    
    # 1. Test-first
    def test_select_high_scores():
        assert select_high_scores([], 50) == []
        assert select_high_scores([60], 50) == [60]
        assert select_high_scores([60, 40], 50) == [60]
        assert select_high_scores([60, 40, 50], 50) == [60, 50]
        assert select_high_scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 50) == \
               [50, 60, 70, 80, 90, 100]
    
    
    # 2. Implement
    # pivot : 기준 임의로 넣어준 변수 값 
    # ex) 위의 에시에서 if score >= 50: 과 똑같은 말 
    
    def select_high_scores(scores, pivot):
        # Initial accumulator
        high_scores = []
    
        # Accumulation
        for score in scores:
            # Conditional
            if score >= pivot:
                high_scores.append(score)
    
        # Return
        return high_scores

# 숙제

- moduel 써서 올리기
- clas_scores 로 해도 됨..
    - 1. 20점 단위로 a-f까지 학점 적기
    - 2. 테이블로 표시
    - til에 올리기 어려우면 어렵다고 써도 됨 ㅎㅎ