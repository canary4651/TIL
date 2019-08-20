# 학급 점수 및 등급을 테이블로 보기

# 평범하게 모두 쓰기

import pandas as pd

# def main():
#     class_scores = [
#         {'Name': 'Jane', 'Korean': 100, 'English': 100, 'Math': 100},
#         {'Name': 'Brown', 'Korean': 10, 'English': 20, 'Math': 30},
#         {'Name': 'Susan', 'Korean': 90, 'English': 70, 'Math': 50}
#     ]
#
#     update_class_grades(class_scores, 'Korean')
#     update_class_grades(class_scores, 'English')
#     update_class_grades(class_scores, 'Math')
#
#     columns = [
#         'Korean Grade', 'Korean',
#         'English Grade', 'English',
#         'Math Grade', 'Math'
#     ]
#
#     table = pd.DataFrame(class_scores, columns=columns)
#     print(table)
#
#
# main()

# 똑같은 모양의 코드 정리하기

import pandas as pd

from homework2_ashal import update_class_grades


def main():
    class_scores = [
        {'Name': 'Jane', 'Korean': 100, 'English': 100, 'Math': 100},
        {'Name': 'Brown', 'Korean': 10, 'English': 20, 'Math': 30},
        {'Name': 'Susan', 'Korean': 90, 'English': 70, 'Math': 50}
    ]

    subjects = ['Korean', 'English', 'Math']

    for subject in subjects:
        update_class_grades(class_scores, subject)

    columns = []
    for subject in subjects:
        columns += [subject + ' Grade', subject]

    table = pd.DataFrame(class_scores, columns=columns)
    print(table)


main()

# python homework2_ashal_table.py
