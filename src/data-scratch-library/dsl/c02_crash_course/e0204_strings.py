def create_single_quoted_string():
    """
    Returns a string enclosed in single quotes.
    """
    return 'data science'


def create_double_quoted_string():
    """
    Returns a string enclosed in double quotes.
    """
    return "data science"


def get_tab_string_length():
    """
    Returns the length of a tab character.
    """
    tab_string = "\t"
    return len(tab_string)


def get_raw_tab_string_length():
    """
    Returns the length of a raw string representing the characters '\' and 't'.
    """
    not_tab_string = r"\t"
    return len(not_tab_string)


def create_multiline_string():
    """
    Returns a multiline string.
    """
    return """This is the first line.
and this is the second line
and this is the third line"""


def combine_names_with_fstring(first_name, last_name):
    """
    Combines first and last name using f-string formatting.
    """
    return f"{first_name} {last_name}"


def combine_names_with_addition(first_name, last_name):
    """
    Combines first and last name using string addition.
    """
    return first_name + " " + last_name


def combine_names_with_format(first_name, last_name):
    """
    Combines first and last name using string.format().
    """
    return "{0} {1}".format(first_name, last_name)
