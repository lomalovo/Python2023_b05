import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    result: tp.Any = []
    for k, v in dct.items():
        new_prefix: tp.Any = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            result.extend(traverse_dictionary_immutable(v, new_prefix))
        else:
            result.append((new_prefix, v))
    return result


def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for k, v in dct.items():
        new_prefix: tp.Any = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            traverse_dictionary_mutable(v, result, new_prefix)
        else:
            result.append((new_prefix, v))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    stack: tp.Any = [(dct.items(), "")]
    result: tp.Any = []
    while stack:
        items, prefix = stack.pop()
        for k, v in items:
            new_prefix = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                stack.append((v.items(), new_prefix))
            else:
                result.append((new_prefix, v))
    return result
