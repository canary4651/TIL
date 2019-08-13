# 1. class_total
# 2. class_total_all


# 정의 collection = [1, 2, 3]
# 정의 collection = {'a': 1, 'b': 2, 'c': 3}
# 정의 collection = {1, 2, 3}

# 접근 collection[0]
# 접근 collection['a']
# 접근 collection.get('a', 0)


# Namespace
# Scope


def f(scores):
    a = 13
    b = [1, 2, 3]
    c = {'국어': 100}
    c['국어']
    {'국어': 100}['국어']
    age = 13
    age = 13 + 1
    age = age + 1
    age += 1
    score = 10
    score + 20
    10 + 20
    score = 20
    score + 20
    20 + 20
    # 초기값
    accumulator = 0
    # 누산
    for i in [0, 1, 2]:
        accumulator += scores[i]
    return accumulator


def class_total(class_scores, subject):
    # results = {
    #     0: 0,
    #     1: 100
    # }
    # return results[len(class_scores)]
    total_score = 0
    # 누산
    for i in range(len(class_scores)):
        scores = class_scores[i]
        total_score += scores[subject]
        # total_score += scores.get(subject, 0)
    return total_score


def class_total_all(class_scores):
    total_score = 0
    # for i in range(len(class_scores)):
    #     total_score += total_all(class_scores[i])
    for scores in class_scores:
        total_score += total_all(scores)
    return total_score


def total_all(scores):
    total_score = 0
    for i in scores:
        total_score += scores[i]
    # for score in scores.values():
    #     total_score += score
    # weights = {'국어': 2, '영어': 1}
    # for k, v in scores.items():
    #     total_score += v * weights[k]
    return total_score


def test_class_total():
    assert class_total([], '국어') == 0
    assert class_total([{'국어': 100}], '국어') == 100
    assert class_total([{'국어': 100}, {'국어': 30}], '국어') == 130
    assert class_total([
        {'국어': 100}, {'국어': 30}, {'국어': 80}
    ], '국어') == 210
    assert class_total([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ], '국어') == 210
    assert class_total([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ], '영어') == 190
    # assert class_total([
    #     {'국어': 100, '영어': 100},
    #     {'국어': 30, '영어': 10},
    #     {'국어': 80, '영어': 80}
    # ], '수학') == 0


def test_class_total_all():
    assert class_total_all([]) == 0
    assert class_total_all([{'국어': 100}]) == 100
    assert class_total_all([{'국어': 100, '영어': 100}]) == 200
    assert class_total_all([
        {'국어': 100, '영어': 100},
        {'국어': 30, '영어': 10},
        {'국어': 80, '영어': 80}
    ]) == 400


def test_total_all():
    assert total_all({}) == 0
    assert total_all({'국어': 100}) == 100
    assert total_all({'국어': 100, '영어': 10}) == 110
    assert total_all({'국어': 100, '영어': 10, '수학': 90}) == 200


def total(scores):
    accumulator = 0
    for i in range(len(scores)):
        accumulator += scores[i]
    return accumulator


def test_tatal():
    assert total([10, 20, 30]) == 60
