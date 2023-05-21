import typing as tp


def get_fizz_buzz(n: int) -> list[tp.Union[int, str]]:
    """
    If value divided by 3 - "Fizz",
       value divided by 5 - "Buzz",
       value divided by 15 - "FizzBuzz",
    else - value.
    :param n: size of sequence
    :return: list of values.
    """
    fizz_buzz_list: list[tp.Union[int, str]] = []
    for i in range(1, n + 1):
        k: int = 0
        if i % 3 == 0:
            k += 3
        if i % 5 == 0:
            k += 5
        if k == 0:
            fizz_buzz_list.append(i)
        if k == 3:
            fizz_buzz_list.append("Fizz")
        if k == 5:
            fizz_buzz_list.append("Buzz")
        if k == 8:
            fizz_buzz_list.append("FizzBuzz")
    return fizz_buzz_list
