def test_list():
    scores = [10, 20, 30]
    assert scores[0] == 10
    assert scores[1] == 20
    assert scores[2] == 30
    assert scores[-1] == 30
    assert scores[-2] == 20
    assert scores[:2] == [10, 20]
    assert scores[1:] == [20, 30]
    assert scores[1:2] == [20]
    assert scores[:-1] == [10, 20]
    # append 실험
    scores.append(5)
    assert scores == [10, 20, 30, 5]
    # 바꾸기
    scores[0] = 0
    assert scores == [0, 20, 30, 5]
    # scores[0] = 10


def test_dictionary():
    scores = {
        '국어': 10,  # 왼쪽은 키, 오른쪽은 값
        '영어': 20,
        '수학': 30
    }
    assert scores['국어'] == 10
    assert scores['영어'] == 20
    assert scores['수학'] == 30


def test_dictionary2():
    korean = '국어'
    scores = {
        korean: 10,
        20: 15}
    assert scores[korean] == 10
    assert scores['국어'] == 10
    assert scores[20] == 15
    # 새로운 것 추가
    scores['영어'] = 20
    assert scores['영어'] == 20


# {0:10, 1:20, 2:}
# {10, 20, 30}

def test_set():
    subjects = {'국어', '영어', '수학'}
    assert '국어' in subjects
    assert '영어' in subjects
    assert '수학' in subjects
    assert '음악' not in subjects
    assert '음악' in subjects.union({'음악'})  # union이 합집합
    assert '음악' in subjects.union(other_subjects)
    assert subjects.union(other_subjects) == {'국어', '영어', '음악', '수학'}
    subjects.add('체육')
    assert '체육' in subjects


