# 학급의 성적을 등급으로 변경

# 한 학생의 성적

# 과목명과 점수가 짝을 이루는 dictionary.

student1 = {'Korean': 100, 'English': 100, 'Math': 100}

student2 = {'Korean': 10, 'English': 20, 'Math': 30}


# 한 학급의 성적

# 학생의 성적 모음(dictionary)을 모은 list.

# [student1, student2, …]

class_scores = [{'Korean': 100, 'English': 100, 'Math': 100}, {'Korean': 10, 'English': 20, 'Math': 30}]


# 성적에 대한 Grade 구하기
from homework2_ashal import class_grades, update_class_grades

def test_class_grades():
    assert class_grades([], 'Korean') == []
    assert class_grades([{'Korean': 100}], 'Korean') == ['A']
    assert class_grades([{'Korean': 90}], 'Korean') == ['A']
    assert class_grades([{'Korean': 70}], 'Korean') == ['B']
    assert class_grades([{'Korean': 100}, {'Korean': 10}], 'Korean') == ['A', 'F']


# 학급 정보에 등급 추가하기


def test_update_class_grades():
    class_scores = [{'Korean': 100}, {'Korean': 10}]

    update_class_grades(class_scores, 'Korean')
    # => 이건 입력값을 맘대로 고칩니다. 대단히 위험한 일이죠.
    # 따라서 update_란 접두어로 구분해서 볼 수 있게 했습니다.

    assert class_scores[0]['Korean Grade'] == 'A'
    assert class_scores[1]['Korean Grade'] == 'F'


