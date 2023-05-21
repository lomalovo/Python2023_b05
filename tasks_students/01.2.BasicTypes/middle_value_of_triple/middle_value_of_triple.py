def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    a1: int = a
    b1: int = b
    c1: int = c
    if a1 < b1:
        a1, b1 = b1, a1
    if c1 <= b1:
        return b1
    elif a1 >= c1:
        return c1
    else:
        return a1
