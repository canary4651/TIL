#0

from homework2 import grade

def test_grade():
    assert grade(80) == 'A'
    assert grade(100) == 'A'
    assert grade(50) == 'C'
    assert grade(90) == 'A'
    assert grade(70) == 'B'
    assert grade(40) == 'C'
    assert grade(20) == 'D'
    assert grade(0) == 'F'

#1
from homework2 import grade_scores
Class_scores = [{'국어': 80,'영어': 100,'수학': 50}, {'국어': 90,'영어': 70,'수학': 40}]
def test_grade_scores():
    # 0,1 순서 헷갈리지 말자 ㅎㅎ
    assert grade_scores(class_scores,0,'국어') == 'A'
    assert grade_scores(class_scores,0, '영어') == 'A'
    assert grade_scores(class_scores,0, '수학') == 'C'
    assert grade_scores(class_scores,1, '국어') == 'A'
    assert grade_scores(class_scores,1, '영어') == 'B'
    assert grade_scores(class_scores,1, '수학') == 'C'
    assert grade_scores([{'국어': 80, '영어': 100, '수학': 100}, {'국어': 90, '영어': 70, '수학': 0}],2, '수학') == ['F']  #리스트의 형식으로 써야 알아먹음!
    assert grade_scores([{'국어': 30, '영어': 100, '수학': 100}, {'국어': 70, '영어': 70, '수학': 0}],1, '국어') == ['D']
    assert grade_scores([{'국어': 80, '영어': 20, '수학': 100}, {'국어': 90, '영어': 50, '수학': 0}], 2,'영어') == ['C']


#2
from homework2 import grade_scores2
class_scores = [{'국어': 80,'영어': 100,'수학': 50}, {'국어': 90,'영어': 70,'수학': 40}] #나는 grade_score2 함수만 데려온거니까, class_scores 한번 더 알려줘야함
def test_grade_scores2():
    # class_scores = [{'국어': 80,'영어': 100,'수학': 50}, {'국어': 90,'영어': 70,'수학': 40}]
    assert grade_scores2(class_scores,'국어') == ['A', 'A']
    assert grade_scores2(class_scores, '영어') == ['A', 'B']
    assert grade_scores2(class_scores, '수학') == ['C', 'C']
    assert grade_scores2([{'국어': 80,'영어': 100,'수학': 100}, {'국어': 90,'영어': 70,'수학': 0}], '수학') == ['A', 'F'] #리스트의 형식으로 써야 알아먹음!
    assert grade_scores2([{'국어': 30, '영어': 100, '수학': 100}, {'국어': 70, '영어': 70, '수학': 0}], '국어') == ['D', 'B']
    assert grade_scores2([{'국어': 80, '영어': 20, '수학': 100}, {'국어': 90, '영어': 50, '수학': 0}], '영어') == ['D', 'C']

