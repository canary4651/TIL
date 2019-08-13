# 입력
numbers = [1, 3, 5, 7, 9]

# 초기값
accumulator = 0

# 누산
for i in range(len(numbers)):
    accumulator += numbers[i]

# 출력
print(accumulator)

# 입력
numbers = [1, 3, 5, 7, 9]

# 초기값
accumulator = 1

# 누산
for i in range(0,len(numbers)):
    accumulator *= numbers[i]

print(accumulator)

numbers = [1, 3, 5, 7, 9]

# 초기값
accumulator = 1

# 누산
for number in numbers:
    accumulator *= number

# 출력
print(accumulator)


def double(n):
    return n * 2

print(double(1))
print(double(2))

def add(x,y):
    return x+y

print(add(1,3))

def factorial(n):
    accumulator = 1
    for i in range(1, n + 1):
        accumulator *= i
    return accumulator

for i in range(1, 10 + 1):
    print(factorial(i))

def bmi(weight,height):
    """calculate bmi(body mass index) with weight and height.

    parameter:
    weight:body weight in kilograms.
    height: Body height in meters.
    """
    return weight/(height**2)

x = bmi(1, 2)
print(bmi(68,1.82))

print('******')
print(bmi.__doc__)
print('******')
help(print)
print('******')
