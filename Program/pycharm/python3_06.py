# 1. total 함수
# 2. average 함수

scores = [80, 100, 70, 90, 40]

# # 1단계 - 단정문 쓰기 (Red)
assert total[(80)] == 80
#
# # 2단계 - “NameError: name 'double' not defined” 문제 해결 (Red)
def total():
    pass

def test_total():
    assert total[(80)] == 80

#
# # 3단계 - AssertionError를 재빨리 해결 (Green)
def total(n):
    pass 80

def test_total():
    assert total[(80)] == 80
#
# # 4단계 - 의미 드러내기 (Refactoring)

def total(scores):
    total  = 0
    total += scores[i]
    return total

def test_total(1):
    assert total[(80)] == 80


# 5단계 - 일반화하기 (Refactoring)
def total(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    return total

def test_total():
    assert total([80]) == 80
    assert total([80,100]) == 180

# 6단계 - 테스트를 추가해 신뢰 확보하기

def test_total_large_case():
    assert total([80,90,100,80,60,70]) == 80 + 90 + 100 + 80 + 60 + 70


# 구구단


# 1
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6

print('2*1=2')

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, ]:
    print(2, '*', 1
    '=', 2 * 1)



# 2
def mt(x,y):
    return 2

def test_mt():
    assert mt(2, 1) == '2 * 1 = 2'


#3
def mt(x, y):
     return f'(x) * f(y) = f(x*y)' #f() 포맷팅하기 (중괄호) 해서 x를 넣으면 쓸 수 있음

def test_mt():
    assert mt(2, 1) == '2 * 1 = 2'
    assert mt(2, 2) == '2 * 2 = 4'
        for i in range(1, 10):
            print(mt(2,1))


# 수업....넘 빨라서 중간에 놓치니까 걍 놓쳐버림 ㅎ...



# 2*1=2
# 2*2=4
# 2*3=6
# ...
# 9*8=72
# 9*9=81


def multiply(x, y):
    return f'{x} * {y} = {x * y}' #f() 포맷팅하기 (중괄호) 해서 x를 넣으면 쓸 수 있음


def multiplication_table():
    # 초기값
    multiplications = []
    # 누산
    for i in range(1, 9 + 1):
        multiplications.append(multiply(2, i))
    return multiplications


def test_multiply():
    assert multiply(2, 1) == '2 * 1 = 2'
    assert multiply(2, 2) == '2 * 2 = 4'


def test_multiplication_table():
    table = multiplication_table()
    assert table[0] == '2 * 1 = 2'
    assert table[1] == '2 * 2 = 4'
    assert table[2] == '2 * 3 = 6'
    assert table[8] == '2 * 9 = 18'

