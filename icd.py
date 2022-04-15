import csv
from dataclasses import dataclass, field
import math
from typing import List, Optional, Set

from reader import insert_into


CATEGORY_CODE, VARIANT, COMPLETE_CODE, NAME, *_ = 0, 1, 2, 3, 4, 5


@dataclass(order=True)
class MedicalCondition:
    icd_code: str
    name: str = field(compare=False)
    parent_code: Optional[str] = field(default=None, init=False, compare=False)
    table_name: str = field(default="medical_conditions", init=False, compare=False)

    def __post_init__(self):
        if len(self.icd_code) < 3:
            raise ValueError(
                f"ICD code must be at least 3 characters; '{self.icd_code}' less than 3 characters"
            )
        if len(self.icd_code) == 3:
            return None
        self.parent_code = self.icd_code[: len(self.icd_code) - 1]

    @property
    def columns(self):
        return ("icd_code", "name", "parent_code")

    @property
    def insert(self):
        return (self.icd_code, self.name, self.parent_code)


def read_conditions_from_file(
    filename: Optional[str] = "icd_codes.csv",
    max_size: float = math.inf,
    letter_prefix: Optional[str] = None,
) -> List[MedicalCondition]:
    with open(filename, mode="rt", encoding="utf-8", newline="\n") as csv_file:
        code_reader = csv.reader(
            csv_file,
        )
        code_list = []
        for line_number, row in enumerate(code_reader, 1):
            if line_number > max_size:
                break
            try:
                condition = MedicalCondition(row[COMPLETE_CODE], row[NAME])
                if letter_prefix and not condition.icd_code.startswith(letter_prefix):
                    continue
                code_list.append(condition)
            except ValueError as error:
                raise ValueError(
                    f"{filename} contains a non-integer value on line: {line_number}.\n"
                    + f"The line's values were '${row}'"
                ) from error
        return code_list


def read_categories_from_file(
    filename: Optional[str] = "icd_categories.csv",
    max_size: float = math.inf,
    letter_prefix: Optional[str] = None,
) -> List[MedicalCondition]:
    with open(filename, mode="rt", encoding="utf-8", newline="\n") as csv_file:
        code_reader = csv.reader(
            csv_file,
        )
        code_list = []
        for line_number, row in enumerate(code_reader, 1):
            if line_number > max_size:
                break
            try:
                condition = MedicalCondition(row[0], row[1])
                if letter_prefix and not condition.icd_code.startswith(letter_prefix):
                    continue
                code_list.append(condition)
            except ValueError as error:
                raise ValueError(
                    f"{filename} contains a non-integer value on line: {line_number}.\n"
                    + f"The line's values were '${row}'"
                ) from error
        return code_list


# def write_categories_to_file(code_data: List[Code]):
#     # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
#     category_input = set((code.category_code, code.category) for code in code_data)
#     table_name = "category"
#     columns = ["category_code", "category_name"]
#     with open("insert_categories.sql", "wt", encoding="utf-8") as f:
#         print(insert_into(table_name, columns, map(str, iter(category_input))), file=f)


def write_conditions_to_file(code_data: List[MedicalCondition]):
    columns = code_data[0].columns
    table_name = code_data[0].table_name
    data = (code.insert for code in code_data)
    with open("insert_conditions.sql", "wt", encoding="utf-8") as f:
        print(
            insert_into(table_name, columns, map(str, data)).replace("None", "DEFAULT"),
            file=f,
        )


def remove_duplicates(codes: List[MedicalCondition], seen_set: Optional[Set] = None):
    if seen_set is None:
        seen_set = set()
    res = []
    seen_set_add = seen_set.add
    for code in codes:
        if code.icd_code not in seen_set:
            seen_set_add(code.icd_code)
            res.append(code)
    return res


def read_combined_conditions() -> List[MedicalCondition]:
    codes = read_conditions_from_file(filename="icd_codes_selected.csv")
    codes.extend(read_categories_from_file(filename="icd_categories_selected.csv"))
    return remove_duplicates(codes)


if __name__ == "__main__":
    uniques = read_combined_conditions()
    print(len(uniques))
    # uniques.sort()
    # write_conditions_to_file(uniques)
    # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv

    # write_categories_to_file(codes)
    # write_conditions_to_file(codes)
