import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    left: int = 0
    right: int = len(nums) - 1
    if right == -1:
        return False
    while left < right:
        mid: int = (left + right) // 2
        if nums[mid] < value:
            left = mid + 1
        else:
            right = mid
    if nums[left] == value:
        return True
    else:
        return False
