import pandas as pd # 판다스 설치해주기 (밑에 terminal 에서 하면됨)

def main():
    class_scores = [
        {'Name': 'Jane', 'Korean': 100, 'English': 100, 'Math': 100},
        {'Name': 'Brown', 'Korean': 10, 'English': 20, 'Math': 30}
    ]

    total = {'Name': '<Total>'}
    for subject in ['Korean', 'English', 'Math']:
        total[subject] = class_total(class_scores, subject)

    table = pd.DataFrame(class_scores + [total],
                         columns=['Name', 'Korean', 'English', 'Math'])
    print(table)

main()



# <터미널> 에서 직접 실행하고 싶을 때 이렇게 써서 하면 됨! 파일 하나하나 테스트 하기 어려우니까 바로 밑에서 ㅎㅎ
#
# pytest
#
# python dataframe.py