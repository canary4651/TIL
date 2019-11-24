import math
#절대값 알고리즘
# 입력 : 실수 a
# 출력 : a의 절댓값

# def abs_sign(a):
#     if a >= 0
#         return a
#     else:
#         return -a
#
# def abs_square(a):
#     b = a * a
#     return math.sqrt(b)
#
#
# def abs_square_sum(a):
#     for i in abs_square_sum(i):

#
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]==a[j]:
                result.add(a[i])
    return result

name = ['tom','jerry','mike','tom']
print(find_same_name(name))