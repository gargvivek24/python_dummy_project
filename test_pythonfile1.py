def test_abc():
    assert 1 == 2, 'Not equal'


def test_bcd():
    dict = {'a': 'hello', 'b': 'world1'}
    str = 'hello world'
    dictstr = dict.get('a') + ' ' + dict.get('b')
    assert dictstr == str, "Strings doesn't match"

def test_xyz():
    a = 4
    b = 2
    assert b != 0, 'not possible mathematically'
    c = a / b
    print(c)
