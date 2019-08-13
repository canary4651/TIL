
scores = [80,100,70,90,40]
sum1 = 0

for i in range (0,5):
    sum1 += scores[i]

print(sum1)

my_scores = [30, 90, 80, 40, 50]
sum1 = 0

len(my_scores)
print(len(my_scores))

for i in range(len(my_scores)):
    sum1 += my_scores[i]
print(sum1)

for i in range(0,5):
    average = sum1/len(my_scores)
print(average)

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]
val = 0
for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        val += class_scores[i][j]
print(val)

val=0
for i in class_scores:
    val += sum(i)

print(val)

avg = 0 # 평균은 어떻게 구하는 걸까
for i in range(len(class_scores)):
    for j in range(len(class_scores[i])):
        avg /= class_scores[i][j]
print(avg)

val = 0
for i in range(len(class_scores)):
    val += sum(class_scores[i])
print(val)


ave = val/(len(class_scores[i])*len(class_scores))
print(ave)


#왜 여기서는 ragne가 2일까? 그건 앞에 my_socre = 와 같은 리스트가 없기 때문에 그냥 2이다
#
for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ")
    print('')

#
class_scores = [[30, 90, 80, 40, 50], [100, 100, 100, 100, 100], [90, 90, 30, 30, 20]]
sum = 0
for i in range(len(class_scores)):
   for j in range(len(class_scores[i])):
       sum += class_scores[i][j]
       average = sum/(len(class_scores[i])*len(class_scores))
print(average)

# 
