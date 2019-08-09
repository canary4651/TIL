# PYTHON3_03

<br>

# 성적 총합과 평균 구하기

<br>

```python
socres = [80,100,70,90,40]

# 초기값 지정

    total_socre = 0

# 누산

    total_score += scores[0]
    
    total_score += scores[1]
    
    print(total_score)
    
    → 
    
    for i in [0,1]
    	total_score += scores[i]
    
    print(total_score)
    
    ->
    
    for i in range(0,5)
    	total_score += scores[i]
    
    print(total_score)
    
    ->
    
    for i in range(len(scores)):
    	total_socre += scores[i]
    
    print(total_score)
    

#실습

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
    
    val = 0
    for i in range(len(class_scores)):
        val += sum(class_scores[i])
    print(val)
    
    avg = val/3
    print(avg)
    
    for i in range(len(class_scores)):
        ave = sum(class_scores[i])/len(class_scores)
    print(ave)
    
    
    #왜 여기서는 ragne가 2일까? 그건 앞에 my_socre = 와 같은 리스트가 없기 때문에 그냥 2이다
    
    for i in range(2,10):        # ①번 for문
        for j in range(1, 10):   # ②번 for문
            print(i*j, end=" ")
        print('')

---

<br>

<br>

# 추상화

<br>

    n = 1
    factorial = 1
    for x in range(1,n+1):
    	factorial *=x
    print(factorial) 
    .
    .
    .
    # 계승 구하기 
    n = 1
    factorial = 1
    for x in range(1,n+1):
    	accumulator *=x #factorial이란 함수를 만들거니까 acc로 이름을 바꿈 
    print(accumulator) 
    
    -> 
    
    
    def factorial(n): #정의(definition): 팩토리얼이란 함수를 정의할거다 
    	accumulator = 1
    	for x in range(1,n+1):
    		accumulator *= x
    	return accumulator #
    #팩토리얼이 추상화 해주는 코드는 이것이다 라는 뜻 : 들여쓰기는 맞춰주기 
    print(factorial(1))
    
    
    #기본값 
    def double(n):
    	return n*2
    
    print(double(1))
```