# PYTHON3_05

- '버그 안녕' 책
- 시연
- [수업자료](https://docs.google.com/document/d/107PJDmhW6bLBE8fAw2mB7wSeK-VnHFoH6m9DaxiVHcI/edit)

## assert 단정문

- 자동화
- 단정문 : assertion : 단언컨대 ,,, 무엇 입니다 라는 뜻
- expected actual

```python
    assert 1 + 1 == 2
    # => 아무 일도 일어나지 않음.
    # expected 기댓값과 실행값을 비교함 
    
    assert 1 + 2 == 2
    # => AssertionError 발생!
    
    # 단계별 단정문 + 추상화 
    
    
    # 1단계 - 단정문 쓰기 (Red)
    
    assert double(2) == 4
    
    # 2단계 - “NameError: name 'double' not defined” 문제 해결 (Red)
    
    def double(n):
        pass  # 아무 것도 안 하는 코드 블럭을 만들고 싶다면 이렇게 pass를 써주면 됩니다.
    # pass       # 아무값도 안 쓰고 싶을 때 pass나 return 쓰면 됨 - 작업 해야함 의 표시
    
    assert double(2) == 4
    
    
    # 3단계 - AssertionError를 재빨리 해결 (Green)
    def double(n):
        return 4
    
    # 4단계 - 의미 드러내기 (Refactoring)
    
    def double(n):
        return 2*2
    
    # 5단계 - 일반화하기 (Refactoring)
    def double(n):
        return n*2
    
    assert double(2) == 4
    
    # 5단계 - 테스트를 추가해 신뢰 확보하기
    
    assert double(1) == 2
    assert double(3) == 6
    assert double(123) == 246
    
    # test 
    
    print(double(2)) 
```

- 에러 났을 때만 메세지를 주기 때문에, 버그를 잡기에 좋다. 많이 쓰이는 코드
- 단정문은 파이썬 프로그램 자체에서 기댓값과 실행값을 비교함으로써 시간을 효율적으로 사용할 수 있음
- 어떤 코딩이 틀렸는 지 알려줌
- 내가 어떻게 실수했는 지 알려주면 좋겠다! → 그런 도구가 있음 : **pytest**

    → 다른 사람이 만든 함수나 코드를 테스트 해볼 때 좋음 

    → 파이참에서는 알아서 되고, 터미널에선 직접 설치해야 해야함 " pip install pytest"

    → 파이참으로 설치함! 

## PyCharm 설정

1. PyCharm > Preferences 메뉴
2. “test” 검색
3. Python Integrated Tools 선택
4. Testing > Default test runner > pytest 선택
5. Fix 버튼 눌러서 pytest 설치

## 테스트 실행

1. Run > Edit Configuration 메뉴
2. 기존의 실행 설정을 선택하고 “-” 버튼을 눌러서 삭제 (모든 run 실행 된거 - 눌러서 없애고 다시 하면 됨)

편집기의 def test_simple 왼쪽에 있는 ▶️ 아이콘을 누르고 “Run 'pytest for …”을 눌러서 실행.

## Auto Test

코드를 변경할 때마다 자동으로 테스트 실행.

1. Run 창의 왼쪽에 있는 “Toggle auto-test”를 ON.
2. Run 창의 위쪽에 있는 톱니바퀴 > Set Auto Test Delay에서 1초를 선택.

# HOMEWORK_01
```python
    assert 1 + 1 == 2
    => 아무 일도 일어나지 않음.
    
    assert 1 + 2 == 2
    => AssertionError 발생!
    
    
    
    # 1단계 - 단정문 쓰기 (Red)
    
    assert double(2) == 4
    
    # 2단계 - “NameError: name 'double' not defined” 문제 해결 (Red)
    
    def double(n):
        pass  # 아무 것도 안 하는 코드 블럭을 만들고 싶다면 이렇게 pass를 써주면 됩니다.
    # pass       # 아무값도 안 쓰고 싶을 때 pass나 return 쓰면 됨 - 작업 해야함 의 표시
    
    assert double(2) == 4
    
    
    # 3단계 - AssertionError를 재빨리 해결 (Green)
    def double(n):
        return 4
    
    # 4단계 - 의미 드러내기 (Refactoring)
    
    def double(n):
        return 2*2
    
    5단계 - 일반화하기 (Refactoring)
    def double(n):
        return n * 2
    
    
    assert double(2) == 4
    # 5단계 - 테스트를 추가해 신뢰 확보하기
    assert double(1) == 2
    assert double(3) == 6
    assert double(123) == 246
    
    값 확인
    
    print(double(2))
    
    
    테스트 함수 작성
    
    
    def test_simple():
        assert 1 + 1 == 2
    
    def test():
        assert 4 * 2 == 8
    
    
    실습 :
    
    scores = [80, 100, 70, 90, 40]
    
    
    def total(scores):
        total = 0
        for i in range(len(scores)):
            total += scores[i]
        return total
    
    
    def test():
        assert total([80]) == 80
        assert total([80, 20]) == 100
    
    
    def avg(scores):
        avg = 0
        avg = total(scores) / len(scores)
        return avg
    
    
    def test_avg():
        assert avg([80]) == 80
        assert avg([80, 100, 30]) == 70
    
    
    def test():
        assert total_scores = 80
    
    
    def test(scores):
        total = 0
        for i in range(len(scores)):
            total += scores[i]
        return total
    
    
    def total(scores):
        accumulator = 0
        for i in range(0, len(scores)):
            accumulator += scores[i]
        return accumulator
    
    
    def test_total():
        assert total([80]) == 80
        assert total([80, 20]) == 100
    
    
    
    def avg(scores):
        avg = 0
        avg = total(scores)/len(scores)
        return avg
    
    
    
    def test_avg():
        assert avg([80]) == 80
        assert avg([80,100,30]) == 70
```