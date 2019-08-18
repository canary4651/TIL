# 20점 단위 A-F 학점
# (A:100-80/B:80-60/C:60-40/D:40-20/F:20-0)
# 테이블로 표시

class_scores = [{'국어': 80,'영어': 100,'수학': 50}, {'국어': 90,'영어': 70,'수학': 40}]

# score값이 자꾸 없다고 함...근데 저번 문제에서는 scores해도 잘 되었는 데 뭐가 문제일까..?

# 오류
# def grade_scores(scores,subject):
#     grade_scores = []
#     for dict in scores:
#         # for subject in dict.keys:
#         grade_scores = dict[subject]
#         if dict[subject] >= 80:
#             return 'A'
#         elif dict[subject] >= 60:
#             return 'B'
#         elif dict[subject] >= 40:
#             return 'C'
#         elif dict[subject] >= 20:
#             return 'D'
#         else:
#             return 'F'

#0

def grade(scores):
    if scores >= 80:
        return 'A'
    elif scores >= 60:
        return 'B'
    elif scores >= 40:
        return 'C'
    elif scores >= 20:
        return 'D'
    else:
        return 'F'

print(grade(80))


#1
def grade_scores(Scores, which_dict, subject):
    if Scores[which_dict][subject] >= 80:
        return 'A'
    elif Scores[which_dict][subject] >= 60:
        return 'B'
    elif Scores[which_dict][subject] >= 40:
        return 'C'
    elif Scores[which_dict][subject] >= 20:
        return 'D'
    else:
        return 'F'

# # class_scores의 2가지 dict 중 두 번째 dict의 영어 과목의 학점이 궁금하다
print(grade_scores(class_scores,1,'영어'))


# 마지막

def grade_scores2(Scores, subject):
    grade = []
    for which_dict in range(len(Scores)):
        if Scores[which_dict][subject] >= 80:
            grade.append('A')
        elif Scores[which_dict][subject] >= 60:
            grade.append('B')
        elif Scores[which_dict][subject] >= 40:
            grade.append('C')
        elif Scores[which_dict][subject] >= 20:
            grade.append('D')
        else:
            grade.append('F')
    return grade

# class_scores의 2가지 dict 중 두 번째 dict의 국어 과목의 학점이 궁금하다

# print(grade_scores2(class_scores, '국어'))


#tdd 넘 어렵고....아직도 잘 모르겠다....print해서 뽑아 보면 돌아가는 데 tdd가 안되네...

