import types
import dis


def count_operations(source_code: types.CodeType) -> dict[str, int]:
    """Count byte code operations in given source code.

    :param source_code: the bytecode operation names to be extracted from
    :return: operation counts
    """
    dict_: dict[str, int] = {}
    for instr in dis.get_instructions(source_code):
        if (name := instr.opname) in dict_:
            dict_[name] += 1
        else:
            dict_[name] = 1
        if isinstance(instr.argval, types.CodeType):
            c = count_operations(instr.argval)
            for a in c.items():
                if a[0] in dict_:
                    dict_[a[0]] += a[1]
                else:
                    dict_[a[0]] = a[1]
    return dict_
