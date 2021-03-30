from containers.unicode import normalized_str
import pytest



strings = [
    'César Chávez',                             # spanish, NFD normalized
    'César Chávez',                             # spanish, NFC normalized
    'César Chávez',                             # spanish, unnormalized
    'Strauß',                                   # german
    '计算机编程是最好的！！！',                 # chinese
    '컴퓨터 프로그래밍이 최고입니다 !!!',       # korean
    'lập trình máy tính là tốt nhất !!!',       # vietnamese
    '!‏برمجة الكمبيوتر هي الأفضل!‏!‏',     # arabic
    '😊',                                       # emoji
    '💩',                                       # emoji
    '৪৭'                                        # In Tamil ৪ = 4 , ৭ = 7
    ]


def test_repr_0():
    assert repr(normalized_str(strings[0])) == "normalized_str('César Chávez', 'NFC')"

def test_repr_1():
    assert repr(normalized_str(strings[1])) == "normalized_str('César Chávez', 'NFC')"

def test_repr_2():
    assert repr(normalized_str(strings[2])) == "normalized_str('César Chávez', 'NFC')"


def test_repr_NFD_0():
    assert repr(normalized_str(strings[0], 'NFD')) == "normalized_str('César Chávez', 'NFD')"

def test_repr_NFD_1():
    assert repr(normalized_str(strings[1], 'NFD')) == "normalized_str('César Chávez', 'NFD')"

def test_repr_NFD_2():
    assert repr(normalized_str(strings[2], 'NFD')) == "normalized_str('César Chávez', 'NFD')"


def test_str_0():
    assert str(normalized_str(strings[0])) == 'César Chávez'

def test_str_1():
    assert str(normalized_str(strings[1])) == 'César Chávez'

def test_str_2():
    assert str(normalized_str(strings[2])) == 'César Chávez'


def test_len_0():
    assert len(normalized_str(strings[0])) == 12

def test_len_1():
    assert len(normalized_str(strings[1])) == 12

def test_len_2():
    assert len(normalized_str(strings[2])) == 12


def test_len_NFD_0():
    assert len(normalized_str(strings[0], 'NFD')) == 14

def test_len_NFD_1():
    assert len(normalized_str(strings[1], 'NFD')) == 14

def test_len_NFD_2():
    assert len(normalized_str(strings[2], 'NFD')) == 14


def test_contains_0():
    assert strings[0] in normalized_str(strings[0])

def test_contains_1():
    assert strings[0] in normalized_str(strings[1])

def test_contains_2():
    assert strings[0] in normalized_str(strings[2])

def test_contains_3():
    assert strings[0] in normalized_str(strings[0], 'NFD')

def test_contains_4():
    assert strings[0] in normalized_str(strings[1], 'NFD')

def test_contains_5():
    assert strings[0] in normalized_str(strings[2], 'NFD')

def test_contains_6():
    assert strings[1] in normalized_str(strings[0])

def test_contains_7():
    assert strings[1] in normalized_str(strings[1])

def test_contains_8():
    assert strings[1] in normalized_str(strings[2])

def test_contains_9():
    assert strings[1] in normalized_str(strings[0], 'NFD')

def test_contains_10():
    assert strings[1] in normalized_str(strings[1], 'NFD')

def test_contains_11():
    assert strings[1] in normalized_str(strings[2], 'NFD')

def test_contains_12():
    assert strings[2] in normalized_str(strings[0])

def test_contains_13():
    assert strings[2] in normalized_str(strings[1])

def test_contains_14():
    assert strings[2] in normalized_str(strings[2])

def test_contains_15():
    assert strings[2] in normalized_str(strings[0], 'NFD')

def test_contains_16():
    assert strings[2] in normalized_str(strings[1], 'NFD')

def test_contains_17():
    assert strings[2] in normalized_str(strings[2], 'NFD')

def test_contains_18():
    assert 'Cesar' not in normalized_str(strings[0], 'NFD')

def test_contains_19():
    assert 'Cesar' not in normalized_str(strings[1], 'NFD')

def test_contains_20():
    assert 'Cesar' not in normalized_str(strings[2], 'NFD')

def test_contains_21():
    assert 'Cesar' not in normalized_str(strings[0], 'NFC')

def test_contains_22():
    assert 'Cesar' not in normalized_str(strings[1], 'NFC')

def test_contains_23():
    assert 'Cesar' not in normalized_str(strings[2], 'NFC')


def test_getitem_0():
    assert normalized_str(strings[0], 'NFC')[0] == 'C'

def test_getitem_1():
    assert normalized_str(strings[0], 'NFC')[1] == 'é'

def test_getitem_2():
    assert normalized_str(strings[0], 'NFC')[9] == 'v'

def test_getitem_3():
    assert normalized_str(strings[0], 'NFD')[0] == 'C'

def test_getitem_4():
    assert normalized_str(strings[0], 'NFD')[1] == 'e'

def test_getitem_5():
    assert normalized_str(strings[0], 'NFD')[9] == 'a'


def test_lower_0():
    assert str(normalized_str(strings[0], 'NFD').lower()) == 'césar chávez'

def test_lower_1():
    assert str(normalized_str(strings[0], 'NFC').lower()) == 'césar chávez'

def test_lower_2():
    assert str(normalized_str(strings[1], 'NFD').lower()) == 'césar chávez'

def test_lower_3():
    assert str(normalized_str(strings[1], 'NFC').lower()) == 'césar chávez'

def test_lower_4():
    assert str(normalized_str(strings[2], 'NFD').lower()) == 'césar chávez'

def test_lower_5():
    assert str(normalized_str(strings[2], 'NFC').lower()) == 'césar chávez'

def test_lower_6():
    x = normalized_str(strings[0])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'

def test_lower_7():
    x = normalized_str(strings[1])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'

def test_lower_8():
    x = normalized_str(strings[2])
    y = x.lower()
    assert str(x) == 'César Chávez'
    assert str(y) == 'césar chávez'


def test_upper_0():
    assert str(normalized_str(strings[0], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_1():
    assert str(normalized_str(strings[0], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_2():
    assert str(normalized_str(strings[1], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_3():
    assert str(normalized_str(strings[1], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_4():
    assert str(normalized_str(strings[2], 'NFD').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_5():
    assert str(normalized_str(strings[2], 'NFC').upper()) == 'CÉSAR CHÁVEZ'

def test_upper_6():
    x = normalized_str(strings[0])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_upper_7():
    x = normalized_str(strings[1])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_upper_8():
    x = normalized_str(strings[2])
    y = x.upper()
    assert str(x) == 'César Chávez'
    assert str(y) == 'CÉSAR CHÁVEZ'

def test_add_0():
    x = normalized_str(strings[0])
    y = normalized_str(strings[1])
    z = normalized_str(strings[2])
    assert str(x + y + z) == str(y + x + z)
    assert str(x) == str(normalized_str(strings[0], 'NFC')) 
    assert str(y) == str(normalized_str(strings[1], 'NFC')) 
    assert str(z) == str(normalized_str(strings[2], 'NFC')) 

def test_add_1():
    x = normalized_str(strings[0], 'NFD')
    y = normalized_str(strings[1], 'NFD')
    z = normalized_str(strings[2], 'NFD')
    assert str(x + y + z) == str(y + x + z)
    assert str(x) == str(normalized_str(strings[0], 'NFD')) 
    assert str(y) == str(normalized_str(strings[1], 'NFD')) 
    assert str(z) == str(normalized_str(strings[2], 'NFD')) 

def test_add_2():
    x = normalized_str(strings[0], 'NFD')
    y = normalized_str(strings[1], 'NFD')
    z = normalized_str(strings[2], 'NFD')
    assert str(x + strings[1] + strings[2]) == str(y + x + z)
    assert str(x) == str(normalized_str(strings[0], 'NFD')) 
    assert str(y) == str(normalized_str(strings[1], 'NFD')) 
    assert str(z) == str(normalized_str(strings[2], 'NFD')) 

def test_add_3():
    x = normalized_str(strings[0], 'NFC')
    y = normalized_str(strings[1], 'NFC')
    z = normalized_str(strings[2], 'NFC')
    assert str(x + strings[1] + strings[2]) == str(y + x + z)
    assert str(x) == str(normalized_str(strings[0], 'NFC')) 
    assert str(y) == str(normalized_str(strings[1], 'NFC')) 
    assert str(z) == str(normalized_str(strings[2], 'NFC')) 


def test_add_3():
    x = '\u0301'
    y = 'a'
    assert str(normalized_str(x)) + y == str(normalized_str(x+y))

def test_add_4():
    x = '\u0301'
    y = 'a'
    assert str(normalized_str(x,'NFD')) + y == str(normalized_str(x+y,'NFD'))

def test_add_5():
    x = '\u0302'
    y = 'a'
    assert str(normalized_str(x)) + y == str(normalized_str(x+y))

def test_add_6():
    x = '\u0302'
    y = 'a'
    assert str(normalized_str(x,'NFD')) + y == str(normalized_str(x+y,'NFD'))


def test_iter_0():
    x = normalized_str(strings[0], 'NFC')
    assert list(x) == list(strings[0])

def test_iter_1():
    x = normalized_str(strings[0], 'NFD')
    assert list(x) == list(strings[1])

def test_iter_2():
    x = normalized_str(strings[0], 'NFC')
    assert len(list(x)) == 12

def test_iter_3():
    x = normalized_str(strings[2], 'NFC')
    assert len(list(x)) == 12
