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
