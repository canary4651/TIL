# 1) 두 개의 dictionary에서 국어 점수의 총 합은?
# => assert class_total(class_scores, '국어') == 170
# 이렇게 확인할 수 있는 함수를 만들어보세요
# 2) class_scores set에 있는 모든 점수의 합은 얼마인가요?
# => class_total_all(class_scores) == 430

class_scores = [
    {
        '국어': 80,
        '영어': 100,
        '수학': 50
    },
    {
        '국어': 90,
        '영어': 70,
        '수학': 40
    }
]

#1

scores1 = class_scores[0]
scores2 = class_scores[1]

# def total_class(scores, i):
#     total_class = 0
#     total_class = scores1[i] + scores2[i]
#     return total_class
#
#
# def test_subject():
#     assert total_class(class_scores, '국어') == 80 + 90
#     assert total_class(class_scores, '영어') == 100 + 70
#     assert total_class(class_scores, '수학') == 50 + 40

# 대체 어떻게 풀어야 할 지 답이 안나와서 저렇게 값을 지정해주고 했더니 pytest는 돌아갔다.
# 그런데 저렇게 풀면 안 된다는.. 컴공 전공의 친구의 피드백을 들었다. 왜 안되는 걸까...???
# for i in dic.key 와 같은 함수는  검색이나 다른 잘하는 사람의 도움을 얻어야 알 수 있다니...뭔가 이 뜻이 뭔지 이해하는 데 오래 걸림..


def total_class(dic, subject):
    total_subject = 0
    for i in dic: # i(dic)리스트 안의 딕셔너리이고  dic(class_scores) 그니까 리스트 안에 딕셔너리가 2개 들어간 모양..!
        total_subject += i[subject] # 왜 i[subject]가 대체 무슨 값이지? 걍 외워야 하는 문법인가? 했는데 이해했다.
    return total_subject

# 이렇게 풀어도 됨! 사실 이 쪽이 더 이해하기 쉽고 말하기 편한 듯
# def total_class(scores,subject):
#     total_subject = 0
#     for dic in scores:
#         total_subject += dic[subject]
#     return total_subject

# dic은 순서가 없이 key:value로 이루어져 있다. 만약 a = [0,1,2,3] 일떄, a의 첫번째 원소 -> a[0] 인 것처럼
# dic의 "국어" 원소를 뽑는다 하면 dic["국어"] 라고 입력하는 것. dic[0]라고 하면 오류남..! 왜냐면 딕셔너리는 순서를 갖는 게 아니니까

def test_total_class():
    assert total_class(class_scores, '국어') == 80 + 90
    assert total_class(class_scores, '영어') == 100 + 70
    assert total_class(class_scores, '수학') == 50 + 40

# 헐 감격스러워...이제 이해도 되었고 풀었다 ㅠㅠㅠ

#2
def total_all(scores):
    class_all = 0
    for dic in scores:
        for i in dic.values():
            class_all += i
    return class_all


def test_class():
    assert total_all(class_scores) == 430
