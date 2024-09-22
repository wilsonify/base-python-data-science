import re
from collections import defaultdict, Counter

from dsl.c02_crash_course.e0202_modules import (
    compile_regex,
    compile_regex_with_alias,


    create_defaultdict,
    create_counter,

)


def test_compile_regex():
    regex_obj = compile_regex("[0-9]+")
    assert isinstance(regex_obj, re.Pattern)


def test_compile_regex_with_alias():
    regex_obj = compile_regex_with_alias("[0-9]+")
    assert isinstance(regex_obj, re.Pattern)


def test_create_defaultdict():
    dd = create_defaultdict()
    assert isinstance(dd, defaultdict)
    assert dd['missing_key'] == 0  # defaultdict with int returns 0 by default


def test_create_counter():
    counter = create_counter()
    assert isinstance(counter, Counter)
    counter.update(['a', 'b', 'a'])
    assert counter['a'] == 2
    assert counter['b'] == 1
