import sys
import typing as tp


def input_(prompt: tp.Optional[str] = None,
           inp: tp.Optional[tp.IO[str]] = None,
           out: tp.Optional[tp.IO[str]] = None) -> tp.Optional[str]:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    if prompt is not None:
        if out is not None:
            out.write(prompt)
        else:
            sys.stdout.write(prompt)
    try:
        if inp is not None:
            a = inp.readline().split("\n")[0]
        else:
            a = sys.stdin.readline().split("\n")[0]
    except EOFError:
        a = None
    if a == '':
        a = None
    return a
