import csv
from typing import List, Dict

def read_tab_delimited_file(file_name: str) -> List[List[str]]:
    """Reads a tab-delimited file and returns a list of rows."""
    with open(file_name, 'r') as f:
        tab_reader = csv.reader(f, delimiter='\t')
        return [row for row in tab_reader]


def read_colon_delimited_file(file_name: str) -> List[Dict[str, str]]:
    """Reads a colon-delimited file and returns a list of dictionaries with the headers as keys."""
    with open(file_name, 'r') as f:
        colon_reader = csv.DictReader(f, delimiter=':')
        return [dict_row for dict_row in colon_reader]


def write_comma_delimited_file(file_name: str, data: Dict[str, float]) -> None:
    """Writes a dictionary to a comma-delimited CSV file."""
    with open(file_name, 'w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=',')
        for stock, price in data.items():
            csv_writer.writerow([stock, price])


def write_bad_csv_file(file_name: str, data: List[List[str]]) -> None:
    """Writes a list of rows to a CSV file incorrectly, risking errors with extra commas."""
    with open(file_name, 'w') as f:
        for row in data:
            f.write(",".join(map(str, row)))
            f.write("\n")




