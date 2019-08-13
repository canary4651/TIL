
my_scores = [30, 90, 80, 40, 50]

# 숙제 했는데 순서대로 안 나눠서 하고 그대로 그냥 하면서 했더니 이런 결과가,,,ㅎㅎ,,,


def total(my_scores):
    total = 0
    for i in range(len(my_scores)):
        total += my_scores[i]
    return total

def test():
    assert total([30]) == 30
    assert total([30, 90]) == 120
    assert total([30,90,80,40]) == 240

def avg(my_scores):
    avg = 0
    avg = total(my_scores) / len(my_scores)
    return avg


def test2():
    assert avg([30]) == 30
    assert avg([30.90]) == 60
    assert avg([30.90,80]) == 80
    assert avg([30,90,80,40,50]) == 58


class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

def total_class(class_scores):
    total_class = 0
    for i in range(len(class_scores)):
        for j in range(len(class_scores[i])):
             total_class += class_scores[i][j]
    return total_class

def test3():
    assert total_class([[30,90,80,40,50]]) == 290
    assert total_class([[30,90,80,40,50],[100]]) == 390
    assert total_class([[30,90,80,40,50],[100,100,100,100,100]]) == 790


def avg_class(class_scores):
    avg_class = 0
    total_length = 0
    for i in range(len(class_scores)):
        total_length += len(class_scores[i])
        avg_class = total_class(class_scores) / total_length
    return avg_class


def test4():
    assert avg_class([[30,90,80,40,50]]) == 58
    assert avg_class([[30, 90, 80, 40, 50], [100, 100, 100, 100, 100]]) == 79
    assert avg_class([[30, 90, 80, 40, 50], [100, 100, 100, 100, 100], [90, 90, 30, 30, 20]]) == 70



# test함수 만드는 게 더 어렵다 평균값 구하는 것도 어려움...계속 안 되었는 데 항에 [] 를 더 추가하니까 되가지고 기뻤다



#구구단


for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ")
    print('')


# 구구단 = Multiplication table

def mt(i,j):
    return i*j
    assert 2 * 4 == 8
    assert 5 * 9 == 45

for i in range(2,10):
    for j in range(1,10):
        print(i*j)
return mt

def test5():
    assert mt(2*1) == 2
    assert mt(2*2) == 4
    assert mt(2*4) == 6


# 구구단 모르겠다....내 생각엔 돌아가야하는 데 왜 안되지,,,
# python3_06 에서 천천히 보고 이해함!!



