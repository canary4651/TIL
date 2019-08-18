from homewokr2 import grade_scores

def test_grade_scores(class_scores,subejct):
    assert grade_scores(80,'국어') == 'A'
    assert grade_scores(100, '영어') == 'A'
    assert grade_scores(50, '수학') == 'C'
    assert grade_scores(90, '국어') == 'A'
    assert grade_scores(70, '영어') == 'B'
    assert grade_scores(40, '수학') == 'C'
    assert grade_scores(20, '수학') == 'D'
    assert grade_scores(0, '영어') == 'F'

