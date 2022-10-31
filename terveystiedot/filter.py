"""Filtering for health related data"""

import csv
from pathlib import Path
import re


def read_data(location: str) -> tuple:
    """read data from file"""

    with open(location, encoding="latin-1") as file:
        reader = csv.reader(file, delimiter=";")

        field_names: str = ";".join(next(reader))[3:]   # read first row of column names without id field
        data_rows: list[str] = []
        faulty_data_rows: list[str] = []

        for row in reader:
            row = row[1:] # remove id column
            row = ";".join(row) # convert to str

            pattern = re.compile(r"^(\d+);[01];(\d|10);(\d,\d);(\d+);(\d\d|10);(\d+);[MN]$")
            if re.match(pattern, row):  # match with regex
                data_rows.append(row)
            else:
                faulty_data_rows.append(row)

        return (field_names, data_rows, faulty_data_rows)


def write_data(location: str, data: list, field_names: list) -> None:
    """write data to file"""

    with open(location, "w", encoding="latin-1") as file:
        file.write(field_names + "\n")

        for entry in data:
            file.write(entry + "\n")


PATH = Path(__file__).parent / "data"
FILE_NAME = "Terveys_v3.csv"

f_names, f_data, faulty = read_data(f"{PATH}/{FILE_NAME}")

write_data(f"{PATH}/filtered.csv", f_data, f_names)
write_data(f"{PATH}/faulty.csv", faulty, f_names)
