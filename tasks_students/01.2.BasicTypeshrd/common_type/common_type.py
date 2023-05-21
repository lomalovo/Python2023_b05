def get_common_type(type1: type, type2: type) -> type:
    """
    Calculate common type according to rule, that it must have the most adequate interpretation after conversion.
    Look in tests for adequacy calibration.
    :param type1: one of [bool, int, float, complex, list, range, tuple, str] types
    :param type2: one of [bool, int, float, complex, list, range, tuple, str] types
    :return: the most concrete common type, which can be used to convert both input values
    """
    if type1 == type2 == range:
        return tuple
    if type1 == bool == type2:
        return bool
    if type1 in [list, tuple, range] and type2 in [list, tuple, range]:
        if type1 == list or type2 == list:
            return list
        elif type1 == tuple or type2 == tuple:
            return tuple
        else:
            return range
    if type1 in [int, float, complex, bool] and type2 in [int, float, complex, bool]:
        if type1 == bool:
            return type2
        elif type2 == bool:
            return type1
        elif type1 == complex or type2 == complex:
            return complex
        elif type1 == float or type2 == float:
            return float
        else:
            return int

    return str

