from types import FunctionType
from typing import Any

CO_VARARGS = 4
CO_VARKEYWORDS = 8

ERR_TOO_MANY_POS_ARGS = 'Too many positional arguments'
ERR_TOO_MANY_KW_ARGS = 'Too many keyword arguments'
ERR_MULT_VALUES_FOR_ARG = 'Multiple values for arguments'
ERR_MISSING_POS_ARGS = 'Missing positional arguments'
ERR_MISSING_KWONLY_ARGS = 'Missing keyword-only arguments'
ERR_POSONLY_PASSED_AS_KW = 'Positional-only argument passed as keyword argument'


def bind_args(func: FunctionType, *args: Any, **kwargs: Any) -> dict[str, Any]:
    """Bind values from `args` and `kwargs` to corresponding arguments of `func`

    :param func: function to be inspected
    :param args: positional arguments to be bound
    :param kwargs: keyword arguments to be bound
    :return: `dict[argument_name] = argument_value` if binding was successful,
             raise TypeError with one of `ERR_*` error descriptions otherwise
    """

    code = func.__code__
    co_flags = code.co_flags
    co_varnames = code.co_varnames
    co_argcount = code.co_argcount
    co_posonlyargcount = code.co_posonlyargcount
    co_kwonlyargcount = code.co_kwonlyargcount

    num_args = len(args)
    num_kwargs = len(kwargs)

    is_varargs = co_flags & CO_VARARGS
    is_varkeywords = co_flags & CO_VARKEYWORDS

    defaults = func.__defaults__ or ()
    defaults_count = len(defaults)
    kwdefaults = func.__kwdefaults__ or ()
    kwdefaults_count = len(kwdefaults)

    if co_kwonlyargcount != 0:
        if num_kwargs > co_kwonlyargcount:
            raise TypeError(ERR_TOO_MANY_KW_ARGS)
        if num_kwargs < co_kwonlyargcount:
            if num_args != 0:
                raise TypeError(ERR_TOO_MANY_POS_ARGS)
            if kwdefaults_count == 0:
                raise TypeError(ERR_MISSING_KWONLY_ARGS)

    if num_args > co_argcount:
        raise TypeError(ERR_TOO_MANY_POS_ARGS)
    if num_kwargs > co_argcount + co_kwonlyargcount:
        raise TypeError(ERR_TOO_MANY_KW_ARGS)
    if num_kwargs + num_args + defaults_count < co_argcount:
        raise TypeError(ERR_MISSING_POS_ARGS)

    bound_args = {}

    for i, arg_name in enumerate(co_varnames):
        if i < num_args:
            if arg_name in kwargs.keys():
                raise TypeError(ERR_MULT_VALUES_FOR_ARG)
            bound_args[arg_name] = args[i]
        elif arg_name in kwargs:
            bound_args[arg_name] = kwargs[arg_name]
        elif i < co_argcount - defaults_count:
            raise TypeError(ERR_MISSING_POS_ARGS)
        else:
            default_index = i - (co_argcount - defaults_count)
            bound_args[arg_name] = defaults[default_index]

    for arg_name in kwargs.keys():
        if arg_name not in co_varnames:
            raise TypeError(ERR_MISSING_POS_ARGS)

    if co_flags & CO_VARARGS:
        bound_args[co_varnames[co_argcount]] = args[co_argcount:]

    if co_flags & CO_VARKEYWORDS:
        for kwarg_name in kwargs:
            if kwarg_name not in bound_args:
                bound_args[kwarg_name] = kwargs[kwarg_name]
            else:
                raise TypeError(ERR_MULT_VALUES_FOR_ARG)

    return bound_args
