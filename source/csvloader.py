import csv
from typing import List


def load_sheet(url: str, delimiter: str = ","):
    with open(url) as file:
        sheet = csv.reader(file, delimiter=delimiter)
        array = []

        for row in sheet:
            array.append(row)

    return array


def load_column(url, column_nr: int, delimiter: str=","):
    array = load_sheet(url, delimiter=delimiter)
    column = get_column_of_sheet(array, column_nr)

    return column


def get_column_of_sheet(sheet, column_nr: int):
    column: List = []

    for row in sheet:
        column.append(row[column])

    return column


def float_list(to_float: List) -> List[float]:
    outlist: List[float] = []

    for entry in to_float:
        outlist.append(float(entry))

    return outlist
