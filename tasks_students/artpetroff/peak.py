import typing as tp


def find_peak_element(list_: list[int]) -> tp.Union[int, None]:
    if not list_:
        return None
    left = 0
    right = len(list_) - 1

    while left < right:
        mid = (left + right) // 2

        if list_[mid] > list_[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_[left]


assert find_peak_element([1, 2, 7, 4, 6, 3, 2, 1]) == 7 or 6
assert find_peak_element([1, 2, 3, 4, 5, 6, 7, 8]) == 8
assert find_peak_element([1]) == 1
