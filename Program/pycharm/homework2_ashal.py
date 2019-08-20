# 성적 등급 구하기
# 번뜩임으로 접근하기

# 이 방식은 얼핏 보면 멋지지만 실제론 변경에 취약합니다.
# 아주 특별한 경우가 아니면 추천하고 싶지 않습니다.

def test_grade():
    assert grade(10) == 'F'
    assert grade(30) == 'D'
    assert grade(50) == 'C'
    assert grade(70) == 'B'
    assert grade(90) == 'A'
    assert grade(100) == 'A'
    assert grade(0) == 'F'


def grade(score):
    return 'FDCBAA'[score // 20] #만약 100점을/20으로 해서 5가 나오면 5번째 알바벳 A라는 뜻,,ㅎ,,


# 평범하게 if 사용

def test_grade():
    assert grade(10) == 'F'
    assert grade(30) == 'D'
    assert grade(50) == 'C'
    assert grade(79) == 'B'
    assert grade(90) == 'A'
    assert grade(100) == 'A'
    assert grade(0) == 'F'
    assert grade(-10) == '이상해요'
    assert grade(110) == '이상해요'


def grade(score):
    if score < 0:
        return "이상해여" # 비정상적인 처리를 미리해주는 거
    if score > 100:
        return '이상해요'
    # 혹은 한줄로 엮어도 됨(return이 같은 값일때!)
    # if score < 0 or score > 100:
    #   return '이상해요'
    if score >= 80:
        return 'A'
    if score >= 60:
        return 'B'
    if score >= 40:
        return 'C'
    if score >= 20:
        return 'D'
    return 'F' # elif나 else를 계속쓰면, 이건가? 아니다 이건가? 아니다 이렇게 가야 하니까 힘들다. 그래서 그냥 if 쓰고 아닐 때 return 값 넣어줘도 된다
# default는 f 학점인데 if 조건이면 if 조건의 return 값을 준다는 뜻



# 같은 모양을 for로 정리

def test_grade():
    assert grade(10) == 'F'
    assert grade(30) == 'D'
    assert grade(50) == 'C'
    assert grade(70) == 'B'
    assert grade(90) == 'A'
    assert grade(100) == 'A'
    assert grade(0) == 'F'


def grade(score):
    grades = {'A': 80, 'B': 60, 'C': 40, 'D': 20} #복잡하게 할때는 dict로 바꿔서 풀면 더 쉽다 value 값에는 리스트가 들어가도 되고, 많은 값들이 들어가도 된다
    for grade in grades:
        if score >= grades[grade]:
            return grade
    return 'F'


# 딕셔너리 items 사용

def test_grade():
    assert grade(10) == 'F'
    assert grade(30) == 'D'
    assert grade(50) == 'C'
    assert grade(70) == 'B'
    assert grade(90) == 'A'
    assert grade(100) == 'A'
    assert grade(0) == 'F'


def grade(score):
    grades = {'A': 80, 'B': 60, 'C': 40, 'D': 20}
    for grade, min_score in grades.items(): #grade: grades.key값, min_score = grades.values 값
        if score >= min_score:
            return grade
    return 'F'




# homework2_ashal2.py file

class_scores = [{'Korean': 100, 'English': 100, 'Math': 100}, {'Korean': 10, 'English': 20, 'Math': 30}]

def class_grades(class_scores, subject):
    grades = []
    for scores in class_scores:
        # grades.append(grade(scores[subject])) # grades += [grade(scores)] 해도 되긴함
        score = scores[subject]
        grades.append(grade(score))
    return grades



# 학급 정보에 등급 추가

def update_class_grades(class_scores, subject):
    grades = class_grades(class_scores, subject)
    for i in range(len(grades)):
        class_scores[i][subject + ' Grade'] = grades[i]