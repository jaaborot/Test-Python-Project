from hypothesis import given
import hypothesis.strategies as st
from hypothesis.strategies import text


def inc(x):
    return abs(x) + 1


@given(st.integers())
def test_positive_input(x):
    assert inc(x) == abs(x) + 1


@given(st.integers())
def test_negative_input(x):
    assert inc(-x) == abs(x) + 1


def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q


@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
