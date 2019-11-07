# PYTHON3-16

# [프로그래머스 문제 풀이](https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3)

## K번째의 수

- 사람이 알아볼 수 있는 코드를 짜는 게 중요하다

문제를 작은 단위로 나눕니다.

→ i부터 j까지 구간의 숫자를 정렬하고 k번째 숫자를 구하는 걸 command마다 처리.

1. i부터 j까지 구간의 숫자 목록 구하기
2. 숫자 목록 정렬하기
3. k번째 숫자 구하기
4. 1~3까지를 활용해 여러 정답 구하기

## i부터 j까지 구간의 숫자 목록 구하기

파이썬의 slice 기능 활용.

numbers = [1, 2, 3, 4, 5]

numbers[1:4]

# ⇒ [2, 3, 4]

index는 0부터 시작. end는 포함하지 않는다는 점에 주의!

이 문제의 조건 확인:

- i와 j는 1부터 시작.
- j를 포함한다.
- 즉, 파이썬과 다름.

i = 2, j = 4일 때…

numbers[i - 1:j - 1 + 1]

⇒ numbers[i - 1:j] 로 표현해야 함.

numbers = [1, 2, 3, 4, 5]

i = 2

j = 4

numbers[i - 1:j]

# ⇒ [2, 3, 4]

## 정렬

sorted 사용.

[https://docs.python.org/ko/3/howto/sorting.html](https://docs.python.org/ko/3/howto/sorting.html)

numbers = [3, 1, 5, 2, 4]

sorted(numbers)

# ⇒ [1, 2, 3, 4, 5]

i부터 j까지 구간의 숫자 목록을 정렬하기

numbers = [3, 1, 5, 2, 4]

i = 2

j = 4

sliced_numbers = numbers[i - 1:j]

sorted(sliced_numbers)

# ⇒ [1, 2, 5]

## k번째 숫자 얻기

index는 0부터 시작. 문제에서 k는 1부터 시작.

numbers = [1, 2, 3, 4, 5]

k = 3

numbers[k - 1]

# ⇒ 3

i부터 j까지 구간의 숫자 목록을 정렬하고 k번째 숫자 얻기

numbers = [3, 1, 5, 2, 4]

i = 2

j = 4

k = 2

sliced_numbers = numbers[i - 1:j]

sorted_numbers = sorted(sliced_numbers)

sorted_numbers[k - 1]

# ⇒ 2

## 여러 command에 적용하기

단수형(command)과 복수형(commands)을 구분하는 게 중요하다는 것부터 확인하고 출발!

numbers = [1, 5, 2, 6, 3, 7, 4]

commands = [

[2, 5, 3],

[4, 4, 1],

[1, 7, 3],

]

for command in commands:

print(command)

* for에서 command를 i, j, k로 분해

for i, j, k in commands:

print(i, j, k)

* 위에서 다룬 연산 가져오기

for i, j, k in commands:

sliced_numbers = numbers[i - 1:j]

sorted_numbers = sorted(sliced_numbers)

kth_number = sorted_numbers[k - 1]

print(kth_number)

* 정답 모으기

kth_numbers = []

for i, j, k in commands:

sliced_numbers = numbers[i - 1:j]

sorted_numbers = sorted(sliced_numbers)

kth_number = sorted_numbers[k - 1]

kth_numbers.append(kth_number)

* 연산하는 부분을 한 줄로 정리하기

kth_numbers = []

for i, j, k in commands:

kth_number = sorted(numbers[i - 1:j])[k - 1]

kth_numbers.append(kth_number)

* List Comprehension!!!

kth_numbers = [sorted(numbers[i - 1:j])[k - 1] for i, j, k in commands]

    # 수민님의 쉬운 풀이 
    def solution(array, commands):
        answer = []
        for i in commands:
            array_ = array[i[0]-1:i[1]]
            array_ = sorted(array_)
            ans = array_[i[2]-1]
            answer.append(ans)
    
        return answer
    
    
    # 한슬님의 풀이 
    def solution(array, commands):
        answer = []
        for command in commands :
            [i,j,k] = command
            a = sorted(array[i-1:j])[k-1]
            answer.append(a)
    ​
        return answer
    
    # 보민님 풀이 
    def solution(array, commands):
        return [sorted(array[iter[0]-1 : iter[1]])[iter[2]-1] for iter in commands]
    
    
    # 아샬님 풀이 
    def knumbers(numbers, commands):
        return [knumber(numbers, command) for command in commands]
    
    
    def knumber(numbers, command):
        begin, end, k = command
        return sorted(numbers[begin - 1:end])[k - 1]
    
    
    def test_sample():
        assert knumbers([1, 5, 2, 6, 3, 7, 4],
                        [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
    
    
    def test_knumber():
        assert knumber([1, 5, 2, 6, 3, 7, 4], [2, 5, 3]) == 5
        assert knumber([1, 5, 2, 6, 3, 7, 4], [2, 4, 3]) == 6
    
    
    

# 객체지향 (object-oriented)

- 복잡한 프로그램을 어떻게 관리할까? 어려운 기술을 써서 해결?
- - 자율적으로 행동, 협력하게 만들고 복잡복잡
- 데이터 다루기 vs 행동 다루기

    player = {
        'name': '전사',
        'hp': 100,
        'str': 5,
    }
    
    enemy = {
        'name': '귀여운 슬라임',
        'hp': 10,
        'str': 3,
    }
    
    enemy['hp'] -= player['str'] # ⇒ 무슨 일이 왜 벌어졌는지, 이 일은 누구의 책임인지 불명확함.
    
    # 위에처럼 복잡한 것을 class로 만들어서 좀 더 명확히 지정해주고, 데이터를 어디다가 넣어야 할 지 고민들을 덜 할 수 있음 
    class Character:
        def __init__(self, name, hp, str):
            self.name = name
            self.hp = hp
            self.str = str
    
        def attack(self, target):
            target.hp -= self.str
    
    player = Character(‘전사’, 100, 10)
    enemy = Character(‘귀여운 슬라임’, 10, 3)
    player.attack(enemy)
    
    # ⇒ 조금 어렵지만 “attack”이란 행동을 통해 다른 캐릭터에게 피해를 입히는 책임을 내가 갖고 있음이 드러남.

- 파이썬은 클래스를 중심으로 객제지향을 함
- 변수, 함수보다 한 단계 위의 추상화.
- 객체 = 데이터 + 연산(Procedure, Function, Method)
- 객체를 한번 더 추상화한 게 Class.
- 프로그래밍의 타입 → 처리 가능한 연산으로 정의.
    - e.g. 숫자는 사칙연산이 가능. 문자열은 사칙연산이 불가능. 숫자는 길이(len)를 구하는 게 불가능. 문자열은 길이를 구하는 게 가능.
- 클래스는 개념에 속하고, 이걸 실체화한 게 인스턴스.
    - 이데아와 현실의 관계 (플라톤)
    - 개라는 개념은 짖지 않는다. (스피노자)
- 우리가 객체라고 부르는 건 대부분 인스턴스를 뜻함. Ruby 등의 순수 객체지향 언어는 클래스와 인스턴스 모두 객체로 취급.

## 기본 클래스 만들기

    class Human:
        pass
    
    # 사람 만들기
    
    human = Human()
    
    # ⇒ 그러나 아무 것도 할 수 없었다…
    
    # 인사 할 수 있는 사람 
    
    class Human:
    	def say_hello(self):  # ← 여기에 self가 들어간다는 점에 주의! (
    # 파이썬은 약간 너 자신을 알아야해, 하는 느낌으로 self를 항상 넣어줘야함) 
            print('hello')
    
    # 사람 만들고 인사하기
    
    human = Human()
    human.say_hello() #책임을 줌 (인사하는 사람) -> hello라고 말하는 주체가 다름 
    
    
    human2 = Human()
    human2.say_hello() #책임을 줌 (인사하는 사람) -> hello라고 말하는 주체가 다름 
    # 객체들마다 아이디가 있음 실제로 파이참에서 찍어보면 구분이 된다. 실제로 쓸만하게 만드는 거 뒤에서 다룰 거임
    
    
    # 이름도 말할 수 있는 사람 
    class Human:
        def __init__(self, name):  # ← 여기도 self가 들어간다.
    					# __ __ ? : 미리 파이썬이 정해놓은 문법.
            self.name = name  # ← 내 이름이기 때문에 self.name
    				# .name과 name은 다르다! .name은 self**의** 네임이다. 
    
        def say_hello(self):
            print('hello')
    
        def say_name(self):
            print(self.name)  # ← 내 이름이기 때문에 self.name
    
    # 사람을 만들 때 이름을 써준다.
    
    human = Human('JOKER')  # ← __init__(self, name)을 여기서 ClassName(name) 형태로 사용.
    
    # 인사도 하고, 이름도 말하고…
    
    human.say_hello()
    human.say_name()
    print(human.name)
    

## 다른 사람에게 인사하는 사람

    class Human:
        def __init__(self, name):
            self.name = name
    
        def say_hello(self):
            print('hello')
    
        def say_name(self):
            print(self.name)
    
        def say_hello_to(self, other): # ← 항상 self를 빼먹지 않도록 주의!
            print(f'(Hello, {other.name}')  # ← f-string 사용. 다른 사람의 이름이라 other.name
    
    
    # 두 사람을 만든다.
    
    human1 = Human('JOKER')
    human2 = Human('Ashal')
    
    # 인사를 잘 합니다.
    
    human.say_hello_to(human2)

- 파이썬이나 개발(특히 자바)를 하기 위해서는 무조건 클래스를 써야 한다!

# Ruby 언어로 만든 게임 오브젝트 사례

데모: [https://ahastudio.com/temp/opal-demo/](https://ahastudio.com/temp/opal-demo/)

소스 코드

[https://github.com/ahastudio/CodingLife/blob/master/20191010/ruby/app/main-objects.rb](https://github.com/ahastudio/CodingLife/blob/master/20191010/ruby/app/main-objects.rb)

# 이진 트리

- CS 2학년 정도에 배우는 “자료구조와 알고리즘” 수업 때 다루는 내용. 쉽지 않을 수 있습니다.
- 하지만 우리는 XML을 다루면서 Tree를 다뤘기 때문에 생각보다는 쉬울 수도 있어요(어쩌면).
- 이진 = Binary = 양자택일
- 이진법, 이진수 = 0과 1로만 이뤄진 숫자

    [https://ko.wikipedia.org/wiki/이진법](https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84%EB%B2%95)

- 이진 트리 = Binary Tree = 자녀가 둘로 제한되는 트리. 자녀가 둘인 게 아니라 둘로 제한이란 점에 주의!

    [https://ko.wikipedia.org/wiki/이진_트리](https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84_%ED%8A%B8%EB%A6%AC)

    ![](Untitled-c2174771-228b-4472-b033-1dbe3c4e4e2c.png)

    - 왼쪽이냐 오른쪽이냐 **양자택일**!

## 노드

## 노드

    class Node:
        pass
    
    node = Node()

## 값을 가진 노드

    class Node:
        def __init__(self, value):
            self.value = value
    
    node = Node(13)
    print(node.value)

## 자녀를 가질 수 있는 노드

    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
    node = Node(13)
    print(node.value)
    print(node.children)
    
    # 값이 있고, 자녀가 있는 노드 준비 완료 

## 자녀를 가진 노드 → 트리 만들기

    # 실제로 값을 가지는 자녀 만들기 
    
    root = Node(13)
    root.children[0] = Node(3)
    root.children[1] = Node(23)
    
    # * 0과 1에 의미 부여하기
    
    LEFT = 0
    RIGHT = 1
    
    root = Node(13)
    root.children[LEFT] = Node(3)
    root.children[RIGHT] = Node(23)

## 자기보다 작은 값은 왼쪽 자녀로, 크거나 같은 값은 오른 쪽 자녀로 만들기

    LEFT = 0
    RIGHT = 1
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
        def add(self, value): #나한테(self) 새로운 벨류를 넣어줘 
            child = Node(value)
            if value < self.value:
                self.children[LEFT] = child  #node(value)나보다 작으면 왼쪽으로 노드를 만들어서 넣어줘. 
                return self.children[LEFT]
            self.children[RIGHT] = child # 나랑 같거나 크면, 오른쪽으로 노드를 만들어서 넣어줘. 
            return self.children[RIGHT]
    
    
    root = Node(13)
    
    child = root.add(3)
    child.value
    child == root.children[LEFT]
    
    child = root.add(23)
    child.value
    child == root.children[RIGHT]
    
    
    * add의 중복 제거
    
        def add(self, value):
            child = Node(value)
            position = RIGHT
            if value < self.value:
                position = LEFT
            self.children[position] = child
            return self.children[position]
    
    * True, False가 1, 0에 대응되는 걸 활용
    
        def add(self, value):
            child = Node(value)
            position = [RIGHT, LEFT][value < self.value]
            self.children[position] = child
            return self.children[position]
    
    * child 정리
    
        def add(self, value):
            position = [RIGHT, LEFT][value < self.value]
            self.children[position] = Node(value)
            return self.children[position]

## 더 깊은 트리 만들기

    LEFT = 0
    RIGHT = 1
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
        def add(self, value):
            position = [RIGHT, LEFT][value < self.value]
            if self.children[position]:  # ← 만약 이미 노드가 있는 상태라면!!!!!!!!
                child = self.children[position]
                return child.add(value)  # ← 자녀에게 책임을 “위임”한다.
            self.children[position] = Node(value)
            return self.children[position]
    
    
    root = Node(13)
    
    child = root.add(3)
    child.value
    child == root.children[LEFT]
    
    child = root.add(1)
    child.value
    child == root.children[LEFT].children[LEFT]
    
    child = root.add(8)
    child.value
    child == root.children[LEFT].children[RIGHT]
    
    child = root.add(23)
    child.value
    child == root.children[RIGHT]
    
    child = root.add(20)
    child.value
    child == root.children[RIGHT].children[LEFT]
    
    # ⇒ 계속 확인하기 너무 귀찮고 힘들다!!!

## 간단히 보기

- 실제로 하면 꽤 어렵고, 어렵다고 좌절하지 마세요.

    LEFT = 0
    RIGHT = 1
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
        def add(self, value):
            position = [RIGHT, LEFT][value < self.value]
            if self.children[position]:
                child = self.children[position]
                return child.add(value)
            self.children[position] = Node(value)
            return self.children[position]
    
        def traversal(self, depth, rows):
            # 이번 depth가 처음이면 만들어 줍니다.
            if depth == len(rows):
                rows.append([])
            # 이번 depth에 value를 추가합니다.
            rows[depth].append(self.value)
            # 자녀에게도 기회를 줍니다.
            for position in [LEFT, RIGHT]:
                child = self.children[position]
                if child:
                    child.traversal(depth + 1, rows) # ← 여기서도 자녀에게 책임을 “위임”합니다.
    
    
    root = Node(13)
    child = root.add(3)
    child = root.add(1)
    child = root.add(8)
    child = root.add(23)
    child = root.add(20)
    child = root.add(33)
    
    rows = []
    root.traversal(0, rows)
    print(rows)