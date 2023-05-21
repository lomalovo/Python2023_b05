import sys
import math
from typing import Any, Optional

PROMPT = '>>> '


def run_calc(context: Optional[dict[str, Any]] = None) -> None:
    """Run interactive calculator session in specified namespace"""
    while True:
        sys.stdout.write(PROMPT)
        try:
            expr = sys.stdin.readline()
        except EOFError:
            break
        try:
            sys.stdout.write(str(eval(expr, {'__builtins__': context or {}})) + "\n")
        except SyntaxError:
            sys.stdout.write("\n")
            break


if __name__ == '__main__':
    context = {'math': math}
    run_calc(context)
