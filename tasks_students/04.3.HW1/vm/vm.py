"""
Simplified VM code which works for some cases.
You need extend/rewrite code to pass all cases.
"""

import builtins
import dis
import operator
import sys
import types
import typing as tp

import six


class Frame:
    """
    Frame header in cpython with description
        https://github.com/python/cpython/blob/3.9/Include/frameobject.h#L17

    Text description of frame parameters
        https://docs.python.org/3/library/inspect.html?highlight=frame#types-and-members
    """

    def __init__(self,
                 frame_code: types.CodeType,
                 frame_builtins: dict[str, tp.Any],
                 frame_globals: dict[str, tp.Any],
                 frame_locals: dict[str, tp.Any]) -> None:
        self.trans = False
        self.index = 0
        self.code = frame_code
        self.builtins = frame_builtins
        self.globals = frame_globals
        self.locals = frame_locals
        self.data_stack: tp.Any = []
        self.return_value = None

    def top(self) -> tp.Any:
        return self.data_stack[-1]

    def pop(self, i=0) -> tp.Any:
        return self.data_stack.pop(-1 - i)

    def push(self, *values: tp.Any) -> None:
        self.data_stack.extend(values)

    def popn(self, n: int) -> tp.Any:
        """
        Pop a number of values from the value stack.
        A list of n values is returned, the deepest value first.
        """
        if n > 0:
            returned = self.data_stack[-n:]
            self.data_stack[-n:] = []
            return returned
        else:
            return []

    def peek(self, n):
        """Get a value `n` entries down in the stack, without changing the stack."""
        return self.data_stack[-n]

    def jump(self, num_str) -> None:
        self.index = num_str
        self.trans = True

    def jump_forward_op(self, jump):
        self.jump(jump)

    def jump_absolute_op(self, jump):
        self.jump(jump)

    def pop_jump_if_true_op(self, jump):
        val = self.pop()
        if val:
            self.jump(jump)

    def pop_jump_if_false_op(self, jump):
        val = self.pop()
        if not val:
            self.jump(jump)

    def jump_if_true_or_pop_op(self, jump):
        val = self.top()
        if val:
            self.jump(jump)
        else:
            self.pop()

    def jump_if_false_or_pop_op(self, jump):
        val = self.top()
        if not val:
            self.jump(jump)
        else:
            self.pop()

    def run(self) -> tp.Any:
        list_of_instructions = list(dis.get_instructions(self.code))
        d = dict()
        for i in range(len(list_of_instructions)):
            d[list_of_instructions[i].offset] = i
        i = 0
        while i < len(list_of_instructions):
            if self.trans:
                self.trans = False
                i = d[self.index]
            instruction = list_of_instructions[i]
            if instruction.opname.startswith('UNARY_'):
                self.unaryOperator(instruction.opname[6:])
            elif instruction.opname.startswith('BINARY_'):
                self.binaryOperator(instruction.opname[7:])
            elif instruction.opname.startswith('INPLACE_'):
                self.inplaceOperator(instruction.opname[8:])
            elif 'SLICE+' in instruction.opname:
                self.sliceOperator(instruction.opname)
            else:
                getattr(self, instruction.opname.lower() + "_op")(instruction.argval)
            i += 1
        return self.return_value

    def call_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-CALL_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3496
        """
        arguments = self.popn(arg)
        f = self.pop()
        self.push(f(*arguments))

    def load_name_op(self, arg: str) -> None:
        """
        Partial realization

        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2416
        """
        if arg in self.locals:
            val = self.locals[arg]
        elif arg in self.globals:
            val = self.globals[arg]
        elif arg in self.builtins:
            val = self.builtins[arg]
        else:
            raise NameError("name '%s' is not defined" % arg)
        self.push(val)

    def load_global_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_GLOBAL

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2480
        """

        if arg in self.globals:
            val = self.globals[arg]
        elif arg in self.builtins:
            val = self.builtins[arg]
        else:
            raise NameError("global name '%s' is not defined" % arg)
        self.push(val)

    def load_const_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-LOAD_CONST

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1346
        """
        self.push(arg)

    def return_value_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-RETURN_VALUE

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1911
        """
        self.return_value = self.pop()

    def pop_top_op(self, arg: tp.Any) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-POP_TOP

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L1361
        """
        self.pop()

    def dup_top_op(self, name):
        self.push(self.top())

    def dup_topx_op(self, count):
        items = self.popn(count)
        for i in [1, 2]:
            self.push(*items)

    def dup_top_two_op(self, name):
        # Py3 only
        a, b = self.popn(2)
        self.push(a, b, a, b)

    def rot_two_op(self, name):
        a, b = self.popn(2)
        self.push(b, a)

    def rot_three_op(self, name):
        a, b, c = self.popn(3)
        self.push(c, a, b)

    def rot_four_op(self):
        a, b, c, d = self.popn(4)
        self.push(d, a, b, c)

    def make_function_op(self, arg: int) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-MAKE_FUNCTION

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L3571

        Parse stack:
            https://github.com/python/cpython/blob/3.9/Objects/call.c#L671

        Call function in cpython:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L4950
        """

        name = self.pop()  # the qualified name of the function (at TOS)  # noqa
        code = self.pop()  # the code associated with the function (at TOS1)

        # TODO: use arg to parse function defaults

        def f(*args: tp.Any, **kwargs: tp.Any) -> tp.Any:
            # TODO: parse input arguments using code attributes such as co_argcount

            parsed_args: dict[str, tp.Any] = {}
            f_locals = dict(self.locals)
            f_locals.update(parsed_args)

            frame = Frame(code, self.builtins, self.globals, f_locals)  # Run code in prepared environment
            return frame.run()

        self.push(f)

    def load_closure_op(self, name):
        pass

    def load_deref_op(self, name):
        pass

    def make_closure_op(self, argc):
        pass

    def call_function_var_op(self, arg):
        pass

    def call_function_kw_op(self, arg):
        pass

    def call_function_var_kw_op(self, arg):
        pass

    def call_method_op(self, name):
        pass

    def store_name_op(self, arg: str) -> None:
        """
        Operation description:
            https://docs.python.org/release/3.9.7/library/dis.html#opcode-STORE_NAME

        Operation realization:
            https://github.com/python/cpython/blob/3.9/Python/ceval.c#L2280
        """
        const = self.pop()
        self.locals[arg] = const

    def delete_name_op(self, name):
        del self.locals[name]

    def load_fast_op(self, name):
        if name in self.locals:
            val = self.locals[name]
        else:
            raise UnboundLocalError(
                "local variable '%s' referenced before assignment" % name
            )
        self.push(val)

    def store_fast_op(self, name):
        self.locals[name] = self.pop()

    def delete_fast_op(self, name):
        del self.locals[name]

    def store_global_op(self, name):
        self.globals[name] = self.pop()

    def load_locals_op(self):
        self.push(self.locals)

    def get_iter_op(self, a):
        self.push(iter(self.pop()))

    def for_iter_op(self, jump):
        iterobj = self.top()
        try:
            v = next(iterobj)
            self.push(v)
        except StopIteration:
            self.pop()
            self.jump(jump)

    BINARY_OPERATORS = {
        'POWER': pow,
        'MULTIPLY': operator.mul,
        'DIVIDE': getattr(operator, 'div', lambda x, y: None),
        'FLOOR_DIVIDE': operator.floordiv,
        'TRUE_DIVIDE': operator.truediv,
        'MODULO': operator.mod,
        'ADD': operator.add,
        'SUBTRACT': operator.sub,
        'SUBSCR': operator.getitem,
        'LSHIFT': operator.lshift,
        'RSHIFT': operator.rshift,
        'AND': operator.and_,
        'XOR': operator.xor,
        'OR': operator.or_,
    }

    def binaryOperator(self, op):
        x, y = self.popn(2)
        self.push(self.BINARY_OPERATORS[op](x, y))

    def inplaceOperator(self, op):
        x, y = self.popn(2)
        if op == 'POWER':
            x **= y
        elif op == 'MULTIPLY':
            x *= y
        elif op in ['DIVIDE', 'FLOOR_DIVIDE']:
            x //= y
        elif op == 'TRUE_DIVIDE':
            x /= y
        elif op == 'MODULO':
            x %= y
        elif op == 'ADD':
            x += y
        elif op == 'SUBTRACT':
            x -= y
        elif op == 'LSHIFT':
            x <<= y
        elif op == 'RSHIFT':
            x >>= y
        elif op == 'AND':
            x &= y
        elif op == 'XOR':
            x ^= y
        elif op == 'OR':
            x |= y
        self.push(x)

    def sliceOperator(self, op):
        start = 0
        end = None  # we will take this to mean end
        op, count = op[:-2], int(op[-1])
        if count == 1:
            start = self.pop()
        elif count == 2:
            end = self.pop()
        elif count == 3:
            end = self.pop()
            start = self.pop()
        l = self.pop()
        if end is None:
            end = len(l)
        if op.startswith('STORE_'):
            l[start:end] = self.pop()
        elif op.startswith('DELETE_'):
            del l[start:end]
        else:
            self.push(l[start:end])

    def contains_op_op(self, op):
        ans = False
        x, y = self.popn(2)
        if op == 0:
            ans = x in y
        if op == 1:
            ans = x not in y
        self.push(ans)

    def is_op_op(self, op):
        ans = False
        x, y = self.popn(2)
        if op == 'is':
            ans = x is y
        if op == 'is not':
            ans = x is not y
        self.push(ans)

    def compare_op_op(self, op):
        ans = False
        x, y = self.popn(2)
        if op == '==':
            ans = x == y
        if op == '<':
            ans = x < y
        if op == '>':
            ans = x > y
        if op == '<=':
            ans = x <= y
        if op == '>=':
            ans = x >= y
        if op == 'issubclass':
            ans = issubclass(x, Exception) and issubclass(x, y)
        self.push(ans)

    UNARY_OPERATORS = {
        'POSITIVE': operator.pos,
        'NEGATIVE': operator.neg,
        'NOT': operator.not_,
        'CONVERT': repr,
        'INVERT': operator.invert,
    }

    def unaryOperator(self, op: str):
        x = self.pop()
        self.push(self.UNARY_OPERATORS[op](x))

    def build_tuple_op(self, count):
        ans = self.popn(count)
        self.push(tuple(ans))

    def build_list_op(self, count):
        ans = self.popn(count)
        self.push(ans)

    def list_extend_op(self, count):
        pass

    def build_set_op(self, count):
        ans = self.popn(count)
        self.push(set(ans))

    def build_map_op(self, size):
        self.push({})

    def store_map_op(self):
        map_, val, key = self.popn(3)
        map_[key] = val
        self.push(map_)

    def unpack_sequence_op(self, count):
        seq = self.pop()
        for x in reversed(seq):
            self.push(x)

    def build_slice_op(self, count):
        if count == 2:
            x, y = self.popn(2)
            self.push(slice(x, y))
        elif count == 3:
            x, y, z = self.popn(3)
            self.push(slice(x, y, z))

    def list_append_op(self, count):
        val = self.pop()
        the_list = self.peek(count)
        the_list.append(val)

    def set_add_op(self, count):
        val = self.pop()
        the_set = self.peek(count)
        the_set.add(val)

    def map_add_op(self, count):
        val, key = self.popn(2)
        the_map = self.peek(count)
        the_map[key] = val

    def print_item_op(self):
        item = self.pop()
        self.print_item(item)

    def print_item_to_op(self):
        to = self.pop()
        item = self.pop()
        self.print_item(item, to)

    def print_newline_op(self):
        self.print_newline()

    def print_newline_to_op(self):
        to = self.pop()
        self.print_newline(to)

    def print_item(self, item, to=None):
        if to is None:
            to = sys.stdout
        if to.softspace:
            print(" ", end="", file=to)
            to.softspace = 0
        print(item, end="", file=to)
        if isinstance(item, str):
            if (not item) or (not item[-1].isspace()) or (item[-1] == " "):
                to.softspace = 1
        else:
            to.softspace = 1

    def print_newline(self, to=None):
        if to is None:
            to = sys.stdout
        print("", file=to)
        to.softspace = 0

    def extended_arg_op(self, a):
        pass

    def import_name_op(self, name):
        level, fromlist = self.popn(2)
        self.push(
            __import__(name, self.globals, self.locals, fromlist, level)
        )

    def import_star_op(self):
        mod = self.pop()
        for attr in dir(mod):
            if attr[0] != '_':
                self.locals[attr] = getattr(mod, attr)

    def import_from_op(self, name):
        mod = self.top()
        self.push(getattr(mod, name))

    def load_assertion_error_op(self, name):
        pass

    def raise_varargs_op(self, name):
        pass

    def load_attr_op(self, attr):
        obj = self.pop()
        val = getattr(obj, attr)
        self.push(val)

    def store_attr_op(self, name):
        val, obj = self.popn(2)
        setattr(obj, name, val)

    def delete_attr_op(self, name):
        obj = self.pop()
        delattr(obj, name)

    def store_subscr_op(self, name):
        val, obj, subscr = self.popn(3)
        obj[subscr] = val

    def delete_subscr_op(self, name):
        obj, subscr = self.popn(2)
        del obj[subscr]


    def build_const_key_map_op(self, name):
        pass

    def load_method_op(self, name):
        pass



class VirtualMachine:
    def run(self, code_obj: types.CodeType) -> None:
        """
        :param code_obj: code for interpreting
        """
        globals_context: dict[str, tp.Any] = {}
        frame = Frame(code_obj, builtins.globals()['__builtins__'], globals_context, globals_context)
        return frame.run()
