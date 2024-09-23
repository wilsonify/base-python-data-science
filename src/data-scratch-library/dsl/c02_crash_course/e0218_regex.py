import re


def re_starts_with_a(word_str: str):
    # word_str doesn't start with 'a'
    return re.match("a", word_str)


def re_has_an_a(word_str: str):
    # word_str has an 'a' in it
    return re.search("a", word_str)


def re_has_a_c(word_str: str):
    # word_str has a 'c' in it
    return re.search("c", word_str)


def re_count_ab(word_str: str):
    # Split on a or b
    return len(re.split("[ab]", word_str))


def re_digits_to_dashes(word_str: str):
    # Replace digits with dashes
    return re.sub("[0-9]", "-", word_str)
