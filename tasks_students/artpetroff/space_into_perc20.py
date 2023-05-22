import typing as tp


def space_into_perc20(list_: list[tp.Union[str, None]]) -> None:
    left = len(list_) - 1
    right = len(list_) - 1
    while left >= 0 and list_[left] is None:
        left -= 1
    while left >= 0:
        if list_[left] == ' ':
            list_[right] = '0'
            list_[right - 1] = '2'
            list_[right - 2] = '%'
            right -= 3
        else:
            list_[right] = list_[left]
            right -= 1
        left -= 1


a = ['a', 'a', ' ', 'a', ' ', None, None, None, None]
b = []
c = [' ', None, None]
space_into_perc20(a)
space_into_perc20(b)
space_into_perc20(c)
assert a == ['a', 'a', '%', '2', '0', 'a', '%', '2', '0']
assert b == []
assert c == ['%', '2', '0']
