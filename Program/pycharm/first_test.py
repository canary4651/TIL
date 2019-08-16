from first import less_number

def test_less_number():
    assert less_number(10,20) == 10
    assert less_number(20,10) == 10


# 2

from first import select_high_scores

def test_select_high_scores():
    assert select_high_scores([])== []
    assert select_high_scores([60, 50]) == [60]
    assert select_high_scores([60, 40, 50]) == [60]
    assert select_high_scores([60, 40, 50, 50]) == [60]
    assert select_high_scores([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [60, 70, 80, 90, 100]