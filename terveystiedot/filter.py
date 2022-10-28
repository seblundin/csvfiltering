"""Filtering for health related data"""

import csv
from pathlib import Path


def read_data(location: str) -> tuple:
    """read data from file"""

    with open(location, encoding="latin-1") as file:
        reader = csv.reader(file, delimiter=";")

        field_names = None
        data_rows = []
        faulty_data_rows = []

        for row in reader:
            row = [e.replace(",", ".") for e in row]
            row = row[1:] # remove id column
            try:
                if reader.line_num == 1:
                    field_names = row
                elif (int(row[1]) in [0,1]          # 0 or 1
                    and int(row[2]) in range(1,11)  # from one to ten
                    and len(row[3]) == 3            # decimal with precision of 1
                    and int(row[5]) in range(101)   # 0-100
                    and row[7] in ["M","N"]         # m or n
                    and len(row) == 8):

                    for i in range(7):
                        if not row[i].isdigit():    # check if value is float or int.
                            float(row[i])

                    data_rows.append(row)
                else:
                    faulty_data_rows.append(row)
            except ValueError:
                faulty_data_rows.append(row)

        return (field_names, data_rows, faulty_data_rows)


def write_data(location: str, data: list, field_names: list) -> None:
    """write data to file"""

    with open(location, "w", encoding="latin-1") as file:
        file.write(";".join(field_names) + "\n")

        for entry in data:
            file.write(";".join(entry) + "\n")


PATH = Path(__file__).parent / "data"
FILE_NAME = "Terveys_v3.csv"
print(PATH)

f_names, f_data, faulty = read_data(f"{PATH}/{FILE_NAME}")

write_data(f"{PATH}/filtered.csv", f_data, f_names)
write_data(f"{PATH}/faulty.csv", faulty, f_names)
