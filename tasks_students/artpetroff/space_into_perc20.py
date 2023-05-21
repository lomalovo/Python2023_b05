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
space_into_perc20(a)
print(a)
