import json
import sys
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1



@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name'), ignore_case = True), key = lambda let: let.lower())

@print_result
def f2(arg):
    return list(filter(lambda prog: (prog.lower()).startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda prog_py: prog_py + ' с опытом Python', arg))

@print_result
def f4(arg):
    m = list(gen_random(len(arg), 100000, 200000))
    return list(zip(arg, m))
