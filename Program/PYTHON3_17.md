# PYTHON3-17

### [오늘의 문제](https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3)

    DAY_NAMES = 'SUN MON TUE WED THU FRI SAT'.split()
    DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    def dayname(month, day):
        days = sum(DAYS[:month - 1]) + day
        return DAY_NAMES[(4 + days) % len(DAY_NAMES)]
    
    
    def test_sample():
        assert dayname(1, 1) == 'FRI'
        assert dayname(2, 1) == 'MON'
        assert dayname(5, 24) == 'TUE'
        assert dayname(12, 25) == 'SUN'

문제를 작은 단위로 나눕니다.

1. 요일을 어떻게 구할까?
    - 1월 1일은 금요일
    - 1월 2일(+1)은 토요일
    - 1월 8일(+7)은 금요일
    - 요일을 숫자로 표현할 수 있을까?
    - 증가하는 숫자를 일정 범위 안에 들어오게 할 수 있을까?
2. a월 b일을 어떻게 다루기 쉬운 값으로 바꿀 수 있을까?
    - 1월 1일과 2월 1일은 어떻게 다를까?
    - 1월은 며칠일까?
    - 2월은 며칠일까? 윤년이 뭘까?
3. 테스트를 위해 2016년 달력을 찾아볼 수 있을까?

요일을 7개의 숫자로 표현: 0~6 (금요일은 5)

DAY_NAMES = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

1월 1일과 하루 차이나는 1월 2일은 토요일 = 6 = 5 + 1

1월 1일과 일주일 차이나는 1월 8일은 금요일 = 5 = (5 + 7) % 7

2월 1일과 1월 1일은 31일 차이 ← 1월이 31일까지 있다.

MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

1월 b일은 1월 1일과 b - 1일 차이 = 요일은 (5 + b - 1) % 7

2월 b일은 1월 1일과 31 + b - 1일 차이 = 요일은 (5 + 31 + b - 1) % 7

1월 1일과 며칠 차이가 나는지 구하는 게 문제의 핵심.

    def calculate_days(month, day):
        # 초기값 지정
        days = 0
        # 이전 달까지의 누적 일수 계산
        for i in range(month - 1):  # 이전 달까지 구해야 하므로 -1
            days += MONTH_DAYS[i]
        # 이번 달에 흐른 날짜 계산
        days += day - 1  # 차이를 구해야 하므로 -1
        return days
    
    
    slice와 sum 함수를 활용하면 더 단순해집니다.
    
    
    def calculate_days(month, day):
        # 초기값 지정
        days = 0
        # 이전 달까지의 누적 일수 계산
        days += sum(MONTH_DAYS[:month - 1]
        # 이번 달에 흐른 날짜 계산
        days += day - 1
        return days
    
    
    이런 경우는 한번에 쓰는 게 더 읽기 쉽습니다.
    
    
    def calculate_days(month, day):
        return sum(MONTH_DAYS[:month - 1]) + day - 1
    
    
    요일은 (5 + days) % 7로 구합니다.
    
    
    def solution(month, day):
        return DAY_NAMES[(5 + calculate_days(month, day)) % 7]

# 클래스

    클래스는 객체를 추상화한 것.
    객체는 데이터와 프로시저(행동)를 하나로 묶은 것.
    
    객체는 서로 협력하기 때문에 나를 표현하기 위해 self란 개념을 활용해야 함.
    
    # GameObject 클래스로 객체 생성
    human = GameObject()
    monster = GameObject()
    
    # 주어.동사(목적어) 형태로 사용
    human.attack(monster)
    
    클래스 기본 정의
    
    class GameObject:
        def attack(self, target):
            print('막 때린다 ㅠㅠ')
    
    데이터 활용
    
    # 랜덤한 대미지를 위해 randrange 함수 활용 https://docs.python.org/3/library/random.html
    from random import randrange
    
    class GameObject:
        def __init__(self):
            self.hp = 100
    
        def attack(self, target):
            damage = randrange(10)
            target.hp -= damage
            print('막 때린다:', damage)
    
    
    이진 트리
    
    
    
    Node는 값을 갖는다. → value란 변수 활용.
    
    Node는 최대 2개의 자녀를 갖는다. → 크기가 2인 list로 처리. 자녀가 없을 땐 None.
    
    
    Jupyter Notebook
    https://nbviewer.jupyter.org/github/ahastudio/CodingLife/blob/master/20191115/python/tree.ipynb
    
    
    노드
    
    class Node:
        pass
    
    node = Node()
    
    값을 가진 노드
    
    class Node:
        def __init__(self, value):
            self.value = value
    
    자녀를 가질 수 있는 노드
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
    자기보다 작은 값은 왼쪽 자녀로, 크거나 같은 값은 오른 쪽 자녀로 만들기
    
    LEFT = 0
    RIGHT = 1
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = [None, None]
    
        def add(self, value):
            child = Node(value)
            if value < self.value:
                self.children[LEFT] = child
                return self.children[LEFT]
            self.children[RIGHT] = child
            return self.children[RIGHT]
    
    
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
    
    더 깊은 트리 만들기
    
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
        # 