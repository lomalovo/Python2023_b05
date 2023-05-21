def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Return reversed list. You can use only iteration
    :param lst: input list
    :return: reversed list
    """
    it_l: int = 0
    len_l: int = len(lst) - 1
    answer: list = []
    while it_l <= len_l:
        answer.append(lst[len_l])
        len_l -= 1
    return answer


def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param lst: input list
    :return: None
    """
    it_l: int = 0
    last_l: int = len(lst)-1
    half: int = last_l//2
    while it_l <= half:
        lst[it_l], lst[last_l - it_l] = lst[last_l - it_l], lst[it_l]
        it_l += 1


def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    lst.reverse()


def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
    return list(reversed(lst))


def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    return lst[::-1]
