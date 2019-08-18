# 20점 단위 A-F 학점
# (A:100-80/B:80-60/C:60-40/D:40-20/F:20-0)
# 테이블로 표시

class_scores = [{'국어': 80,'영어': 100,'수학': 50}, {'국어': 90,'영어': 70,'수학': 40}]



def grade_scores(scores,subject):
    grade_scores = 0
    for grade in scores():
        for subject in dic.keys():
            grade_scores == grade[subject]
        if grade[subject] >= 80:
           return 'A'
        elif grade[subject] >= 60:
            return 'B'
        elif grade[subject] >= 40:
            return 'C'
        elif grade[subject] >= 20:
            return 'D'
        else:
            return 'F'

# 대박 과목을 어떻게 넣어야할 지 헤매고 있었는 데, 저번에 푼 문제와 dic.keys 값으로 for문 두번 돌리면 되지 않을까..? 했더니 되서 감격,,,

