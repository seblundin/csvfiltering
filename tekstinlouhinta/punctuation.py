from pathlib import Path
import string

def read_data(location: str) -> list:
    """read data from file"""

    with open(location, encoding="UTF-8") as file:
        data = []
        for row in file:
            for character in row:
                if character not in (string.ascii_letters or string.whitespace) and character not in data:
                    data.append(character)

        return data


def write_data(location: str, data: list) -> None:
    """write data to file"""

    with open(location, "w", encoding="UTF-8") as file:

        for entry in data:
            file.write(entry)


PATH = Path(__file__).parent / "data"

FILE_NAMES = ['stoker_snakes_pass.txt']

for name in FILE_NAMES:
    data = read_data(f"{PATH}/{name}")

    write_data(f"{PATH}/{name[:-4]}_punctuation.txt", data)