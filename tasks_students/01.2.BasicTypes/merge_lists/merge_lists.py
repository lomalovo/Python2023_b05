def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    len_a: int = len(lst_a)
    it_a: int = 0
    it_b: int = 0
    len_b: int = len(lst_b)
    answer: list = []
    while it_a < len_a and it_b < len_b:
        if lst_a[it_a] < lst_b[it_b]:
            answer.append(lst_a[it_a])
            it_a += 1
        else:
            answer.append(lst_b[it_b])
            it_b += 1
    if it_a == len_a:
        while it_b < len_b:
            answer.append(lst_b[it_b])
            it_b += 1
    else:
        while it_a < len_a:
            answer.append(lst_a[it_a])
            it_a += 1
    return answer


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """

    return sorted(lst_a+lst_b)
