import typing as tp
import argparse


def count_util(text: str, flags: tp.Optional[str] = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    answer: dict[str, int] = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', action='store_true', default=False)
    parser.add_argument('-l', action='store_true', default=False)
    parser.add_argument('-L', action='store_true', default=False)
    parser.add_argument('-w', action='store_true', default=False)
    parsed = parser.parse_args(flags)
    if parsed.m:
        answer["chars"] = len(text)
    if parsed.w:
        answer["words"] = len(text.split())
    if parsed.l:
        answer["lines"] = text.count("\n")
    if parsed.L:
        answer["longest_line"] = max(len(line) for line in text.split("\n"))
    return answer


