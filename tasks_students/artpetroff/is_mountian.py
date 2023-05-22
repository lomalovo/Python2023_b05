def is_mountain(arr: list[int]) -> bool:
    if not arr:
        return False
    state, maxim = 0, arr[0]
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            state += 1
        if arr[i] < arr[i + 1] and state > 0:
            return False
        if arr[i + 1] > maxim:
            maxim = arr[i + 1]

    if state == 1 and maxim != arr[0]:
        return True

    return False


assert is_mountain([-3, -2, -1, 0, 1, 1, 1, 1, -5]) is True
assert is_mountain([-3, -2, -1, 0, -1, 1, 1, 1, -5]) is False
assert is_mountain([-3, -2, -1, 0, 1, 1, 1, 1, 1]) is False
assert is_mountain([-2, -2, -1, 0, 1, 1, 1, 1, -5]) is True
assert is_mountain([1, 1, 1, 0]) is False
