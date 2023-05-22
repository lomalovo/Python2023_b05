import typing as tp


def find_median(nums1: tp.Sequence[int], nums2: tp.Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    m: tp.Any = len(nums1)
    n: tp.Any = len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    i_min: int = 0
    i_max: int = m
    half_len: int = (m + n + 1) // 2
    while i_min <= i_max:
        i: int = (i_min + i_max) // 2
        j: int = half_len - i
        if i < m and nums2[j - 1] > nums1[i]:
            i_min = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            i_max = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])
            if (m + n) % 2 == 1:
                return float(max_of_left)
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return float((max_of_left + min_of_right) / 2)
    return 0.0
