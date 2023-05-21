import typing as tp


def get_squares(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    """
    answer: list = []
    for i in range(len(elements)):
        answer.append(elements[i] ** 2)
    return answer


# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    return list(range(1, len(elements) + 1))


# ====================================================================================================


def get_max_element_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    if elements:
        max_el: int = elements[0]
        max_ind: int = 0
        for i in range(len(elements)):
            if elements[i] >= max_el:
                max_el = elements[i]
                max_ind = i
        return max_ind
    else:
        return None


# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    answer: list = elements[:]
    return answer[1::2]


# ====================================================================================================


def get_first_three_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    if elements:
        i: int = 0
        len_el: int = len(elements)
        while i < len_el:
            if elements[i] == 3:
                return i
            i += 1
    return None


# ====================================================================================================


def get_last_three_index(elements: list[int]) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    if elements:
        i: int = 0
        it_el: int = len(elements) - 1
        while i <= it_el:
            if elements[it_el] == 3:
                return it_el
            it_el -= 1
    return None


# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    """
    :param elements: list with integer values
    :return: sum of elements
    """
    return sum(elements)


# ====================================================================================================


def get_min_max(elements: list[int], default: tp.Optional[int]) -> tuple[tp.Optional[int], tp.Optional[int]]:
    """
    :param elements: list with integer values
    :param default: default value to return if elements are empty
    :return: (min, max) of list elements or (default, default) if elements are empty
    """
    if elements:
        return min(elements), max(elements)
    else:
        return default, default


# ====================================================================================================


def get_by_index(elements: list[int], i: int, boundary: int) -> tp.Optional[int]:
    """
    :param elements: list with integer values
    :param i: index of elements to check with boundary
    :param boundary: boundary for check element value
    :return: element at index `i` from `elements` if element greater then boundary and None otherwise
    """

    return None if (elem := elements[i]) <= boundary else elem
