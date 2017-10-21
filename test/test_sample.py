# should output absolute value of input + 1
def inc(x):
    return abs(x) + 1


def test_answer():
    assert inc(3) == 4


def test_negative_input():
    assert inc(-3) == 4
