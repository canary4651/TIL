# Python3_02

설치부터 멘붕 

<br>

## accumulation_누산

## state_상태

## 상태변경 = state transition

---

<br>

    age =13
    age = 13 + 1
    age = age + 1 
    	-> 왜 대체 age = age + 1 이라고 하는 걸까? 여기서 =은 같다는 의미가 아니라 state상태의 의미다 
    new_age = age + 1
    age = new_age
    age = age + 1
    age +=1
    += -> age가 1이 증가했다 
    (파이썬 문법) 
    age /= 2 나누기
    age //= 2 나머지
    age %= 2 몫

<br>

## Factorial

<br>

    factorial = 1
    factorial *= 2
    factorial *= 3
    ...
    factorial *= n
    	
    ->  factorial = 1 * 2 * ... * n 이렇게 늘어나면 어려우니까 한줄로 팩토리얼 정리 (패턴찾기)
    
    # 초기값
    facttorial = 1
    #누산 : x는 1부터 n까지 
    factorial *= x
    
    -> 오늘 배울 것 : 반복적으로 실행되는 파이썬 코드 

<br> 

    
    for x in range(1,n+1):
    		factorial *= x

<br>

- for : - 하는 동안 (기간) = loop
- in : 정해진 기간
- range : 범위
- for x in [1,2,3]: → 처음부터 끝까지 반복한다
- 끝은 포함을 시키지 않기 때문에 n+1! (시작 ≤x<끝 )
- 2번째줄에 공백 (tab)은 꼭 있어야함 (엔터치면 알아서 생김) : indent 4칸 들여쓰기
- 한 단위 = 코드블럭 ex) factorial *=x → indent가 맞춰진 코드들을 한 단위로 인식함

<br>

    for x in range (1,n+1):
    	y = x
    	factorial *= y 

<br>

- 요렇게 많이 써도 되지만 항상 들여쓰기(indent) 잊지 말기!

<br>

    factorial = 1
    factorial *= 2 
    factorial *= 3
    ...
    factorial *= x

<br>

원래는 이렇게 써줘야함 

<br>

    실습
    
    scores = [80,100,70,90,40]
    sum = 0
    
    for i in range (0,5):
        sum += scores[i]
    
    print(sum)