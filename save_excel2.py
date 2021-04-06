import itertools
import pandas as pd


def read_lines(file_object) -> list:
    return [
        parse_line(line) for line in file_object.readlines() if line.strip()
    ]


def parse_line(line: str) -> list:
    return [
        i.split(":")[-1].replace("°C", "").replace("%RH", "")
        for i in line.strip().split()
        if i.startswith(("T1", "T2", "H1", "H2"))
    ]


def flatten(parsed_lines: list) -> list:
    return list(itertools.chain.from_iterable(parsed_lines))


def cut_into_pieces(flattened_lines: list, piece_size: int = 4) -> list:
    return [
        flattened_lines[i:i + piece_size] for i
        in range(0, len(flattened_lines), piece_size)
    ]


with open("SHT_on_Stream.txt") as data:
    df = pd.DataFrame(
        cut_into_pieces(flatten(read_lines(data))),
        columns=["T1", "H1", "T2", "H2"],
    )

    print(df)
    df.to_excel("New_datasheet.xlsx", index=False)