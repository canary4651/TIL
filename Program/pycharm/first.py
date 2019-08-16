def less_number(x, y):
    if x < y:
        return x
    return y

# tab은 콜론 뒤에만 하기!
# def는 항상 return 값이 나와줘야 한다
def select_high_scores(scores):
    high_scores = []
    for score in scores:
        if score >= 60:
            high_scores.append(score)
    return high_scores
