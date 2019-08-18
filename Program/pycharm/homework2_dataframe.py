import pandas as pd

def table():
    class_scores = [
        {'성적':'dic1', '국어': 'A','영어': 'A','수학':'C'},
        {'성적':'dic2','국어':'A','영어': 'B','수학':'C'}
    ]

    table = pd.DataFrame(class_scores,
                         columns=['성적','국어', '영어', '수학'])
    print(table)

table()

# 이렇게만 해도 나오긴 한데,,,, 함수를 만들어서 자동으로 table에 학점 값을 지정해주는 건 어케 할까

# from homework2 import grade_scores2
# 어쩔땐 from import가 그냥 회색으로 되버리는 데, 어쩔때 그런 걸까? 질문하기!
