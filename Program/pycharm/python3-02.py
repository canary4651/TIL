# scores = [80,100,70,90,40]
# total 함수 만들기
# average 함수 만들기
# github에 올리기

scores = [80,100,70,90,40]


# score 가 다음과 같은 형태로 주어졌을 때
scores = [80, 100, 70, 90, 40]
# 1. total 함수 만들기
def total(scores):
   total_score = 0
   for score in scores:
       total_score += score
   return total_score


# 2. average 함수 만들기
def avg(scores):
   total_score = 0
   for score in scores:
       total_score += score
   return total_score/len(scores)
print(total(scores), avg(scores))

def avg(scores):
    total_score=0
    for score in scores:
        total_score += score
    return total(scores)/len(scores)

print(avg(scores))

def avg(scores):
    return total(scores)/len(scores)
print(avg(scores))


def total(scores):
    total_score = 0
    for i in range(len(scores)):
        total_score += scores[i]
    return  total_score
print(total(scores))

def avg(scores):
    total_score=0
    for i in range(len(scores)):
        total_score += scores[i]
    return total_score/len(scores)

print(avg(scores))

#