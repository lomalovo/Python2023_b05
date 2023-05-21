import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    answer: dict[str, list[str]] = {}
    for item in dct.items():
        if item[1] in answer.keys():
            curr_keys = answer[item[1]] + [item[0]]
            answer[item[1]] = curr_keys
        else:
            answer[item[1]] = [item[0]]
    return answer
