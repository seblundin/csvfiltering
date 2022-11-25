"""Filtering for text files"""

from pathlib import Path
import re


def read_data(location: str) -> list:
    """read data from file"""

    with open(location, encoding="UTF-8") as file:
        data = []
        for row in file:
            if str.isspace(row):
                continue
            row = re.sub('[!?()&*%_<>,.=+:;"”“—}{]', ' ', row)
            row = re.sub('[’‘]', "'", row)
            row = row.replace("--", " ")
            row = ' '.join(row.split())
            row = row + ' '
            row = str.lower(row)
            data.append(row)

        return data


def write_data(location: str, data: list) -> None:
    """write data to file"""

    with open(location, "w", encoding="UTF-8") as file:

        for entry in data:
            file.write(entry)


PATH = Path(__file__).parent / "data"

FILE_NAMES = ['stoker_snakes_pass.txt', 'lovecraft_dunwitch_horror.txt', 'lovecraft_the_colour_out_of_space.txt']

for name in FILE_NAMES:
    data = read_data(f"{PATH}/{name}")

    write_data(f"{PATH}/{name[:-4]}_filtered.txt", data)
