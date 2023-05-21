import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    queue: heapq = []
    for lst in seq:
        for elem in lst:
            heapq.heappush(queue, elem)
    answer: list[int] = []
    for i in range(len(queue)):
        answer.append(heapq.heappop(queue))
    return answer
