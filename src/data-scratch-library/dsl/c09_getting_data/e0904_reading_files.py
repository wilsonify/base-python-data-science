from collections import Counter
from typing import List
import re
import os

def get_file_path(file_name: str) -> str:
    """Returns the absolute path to the file."""
    path_to_here = os.path.abspath(os.path.dirname(__file__))
    path_to_data = os.path.abspath(f"{path_to_here}/../../../../data")
    return os.path.join(path_to_data, file_name)


def write_to_file(file_name: str, content: str) -> None:
    """Writes the content to a file."""
    file_path = get_file_path(file_name)
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_name: str, content: str) -> None:
    """Appends the content to a file."""
    file_path = get_file_path(file_name)
    with open(file_path, 'a') as file:
        file.write(content)


def read_file(file_name: str) -> List[str]:
    """Reads the file and returns its lines."""
    file_path = get_file_path(file_name)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def count_lines_starting_with_hash(file_name: str) -> int:
    """Counts lines starting with a '#' in a file."""
    count = 0
    lines = read_file(file_name)
    for line in lines:
        if re.match("^#", line):
            count += 1
    return count


def get_domain(email_address: str) -> str:
    """Splits the email on '@' and returns the domain."""
    return email_address.lower().split("@")[-1]


def count_email_domains(file_name: str) -> Counter:
    """Counts domains in email addresses from the file."""
    lines = read_file(file_name)
    return Counter(
        get_domain(line)
        for line in lines
        if "@" in line
    )


