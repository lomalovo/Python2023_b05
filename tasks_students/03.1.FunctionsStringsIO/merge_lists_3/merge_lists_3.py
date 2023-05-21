import typing as tp
import heapq


def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    seq: list[list[int]] = []
    for stream in input_streams:
        cur_list = []
        for line in stream.readlines():
            cur_list.append(line.decode('utf-8'))
        seq.append(list(map(int, cur_list)))
    answer: list[int] = list(heapq.merge(*seq))
    output_stream.write(('\n'.join(map(str, answer))+"\n").encode('utf-8'))
