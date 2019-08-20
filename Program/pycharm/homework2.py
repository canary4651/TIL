# 20점 단위 A-F 학점
# (A:100-80/B:80-60/C:60-40/D:40-20/F:20-0)
# 테이블로 표시

class_scores = [{'국어': 80, '영어': 100, '수학': 50}, {'국어': 90, '영어': 70, '수학': 40}]

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

# 0

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

# print(grade(80))


# 1
def grade_scores(scores, index, subject): #원래 Scores 라고 했는데, 대문자가 아니라 소문자 사용하기
    return grade(scores[index][subject]) #만들어 놓은 grade 함수 응용하기 #which_dict가 아니라 Index 사용하기

    # if scores[inedx][subject] >= 80:
    #     return 'A'
    # elif scores[index][subject] >= 60:
    #     return 'B'
    # elif scores[index][subject] >= 40:
    #     return 'C'
    # elif scores[index][subject] >= 20:
    #     return 'D'
    # else:
    #     return 'F'


# # class_scores의 2가지 dict 중 두 번째 dict의 영어 과목의 학점이 궁금하다
# print(grade_scores(class_scores, 1, '영어'))


# 마지막

def grade_scores2(scores, subject):
    grades = [] #단수형과 복수형에 주의하기
    for i in range(len(scores)): #일반적으로 인덱스는 i라고 쓸 수 있다
        grades.append(grade(scores[i][subject]))
        # grades.append(grade_scores(scores, index, subject))
        # if scores[index][subject] >= 80: #만약 이렇게 쓰고 싶으면 for i를 index로 바꾸거나 if의 [index]를 [i]로 바꾸기
        #     grade.append('A')
        # elif scores[index][subject] >= 60:
        #     grade.append('B')
        # elif scores[index][subject] >= 40:
        #     grade.append('C')
        # elif scores[index][subject] >= 20:
        #     grade.append('D')
        # else:
        #     grade.append('F')
    return grades

# class_scores의 2가지 dict 중 두 번째 dict의 국어 과목의 학점이 궁금하다

# print(grade_scores2(class_scores, '국어'))
