import typing as tp


def filter_list_by_list(lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range]) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    len_a: int = len(lst_a)
    it_a: int = 0
    it_b: int = 0
    len_b: int = len(lst_b)
    answer: list[int] = []
    while it_a < len_a and it_b < len_b:
        if lst_a[it_a] == lst_b[it_b]:
            it_a += 1
            it_b += 1
        elif lst_a[it_a] < lst_b[it_b]:
            answer.append(lst_a[it_a])
            it_a += 1
        elif lst_a[it_a] > lst_b[it_b]:
            it_b += 1
    if it_a != len_a:
        while it_a < len_a:
            answer.append(lst_a[it_a])
            it_a += 1
    return answer
