def square_sorted_array(list_: list[int]) -> list[int]:
    n = len(list_)
    if n == 0:
        return []
    result = [0] * n
    left = 0
    right = n - 1
    index = n - 1

    while left <= right:
        left_square = list_[left] ** 2
        right_square = list_[right] ** 2

        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1

        index -= 1

    return result


print(square_sorted_array([-4, -2, 0, 2, 3, 5]))
