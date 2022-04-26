"""This module handles importing the medical conditions, and writing them to files"""
# pylint: disable=missing-function-docstring,missing-class-docstring
import csv
import math
from dataclasses import dataclass, field
from typing import List, Optional, Set

from writer import insert_into

CATEGORY_CODE, VARIANT, COMPLETE_CODE, NAME, COMPLETE_NAME, *_ = 0, 1, 2, 3, 4, 5


@dataclass(order=True)
class MedicalCondition:
    icd_code: str
    name: str = field(compare=False)
    parent_code: Optional[str] = field(default=None, init=False, compare=False)
    is_code: bool = field(default=False, compare=False)
    table_name: str = field(default="medical_conditions", init=False, compare=False)

    def __post_init__(self):
        if len(self.icd_code) < 3:
            raise ValueError(
                f"ICD code must be at least 3 characters; '{self.icd_code}' less than "
                f"3 characters"
            )
        if len(self.icd_code) == 3:
            return None
        self.parent_code = self.icd_code[: len(self.icd_code) - 1]
        return None

    @property
    def columns(self):
        return ("icd_code", "name", "parent_code", "is_code")

    @property
    def insert(self):
        return f"{(self.icd_code, self.name, self.parent_code, self.is_code)}"


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
                # pylint: disable=redefined-outer-name
                condition = MedicalCondition(row[COMPLETE_CODE], row[COMPLETE_NAME])
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
                # pylint: disable=redefined-outer-name
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


def build_condition_insert_statement(code_data: List[MedicalCondition]) -> str:
    columns = code_data[0].columns
    table_name = code_data[0].table_name
    data = (f"{code.insert}" for code in code_data)
    return insert_into(table_name, columns, map(str, data)).replace("None", "DEFAULT")


def write_conditions_to_file(code_data: List[MedicalCondition]):
    with open("insert_conditions.sql", "wt", encoding="utf-8") as file:
        print(f"BEGIN;\nTRUNCATE {code_data[0].table_name};", file=file)
        print(
            build_condition_insert_statement(code_data),
            file=file,
        )
        print("COMMIT;", file=file)


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


def mutate_is_code(medical_conditions: List[MedicalCondition]):
    parent_categories = set(condition.parent_code for condition in medical_conditions)
    # pylint: disable=redefined-outer-name
    for condition in medical_conditions:
        condition.is_code = condition.icd_code not in parent_categories


def read_combined_conditions(
    category_file_name: Optional[str] = None,
    condition_file_name: Optional[str] = None,
) -> List[MedicalCondition]:
    if category_file_name is None:
        category_file_name = "icd_categories_selected.csv"
    if condition_file_name is None:
        condition_file_name = "icd_codes_selected.csv"
    codes = read_conditions_from_file(filename=condition_file_name)
    codes.extend(read_categories_from_file(filename=category_file_name))
    unique_codes = remove_duplicates(codes)
    mutate_is_code(unique_codes)
    return unique_codes


# def write_update_names(conditions: List[MedicalCondition]):
#     statements = ['BEGIN;', 'update medical_conditions mc set', 'name = mc2.name,',
#     'from (values']
#     for condition in conditions:
#         statements.append(f"\t('{condition.icd_code}', '{condition.name}'),")
#     statements[-1] = statements[-1].rstrip(',')
#     statements.append(') as mc2(icd_code, name)')
#     statements.append('where mc2.icd_code = mc.icd_code')
#     statements.append('END;')
#     with open("update_condition_names.sql", "wt", encoding="utf-8") as file:
#         print('\n'.join(statements), file=file)


if __name__ == "__main__":
    conditions = read_combined_conditions()
    mutate_is_code(conditions)
    names = set()
    for condition in conditions:
        val = (condition.name, condition.parent_code)
        if val in names:
            raise ValueError(f"{val} already exists")
        names.add(val)
    # print(tuple(c.icd_code for c in conditions if c.is_code))
    conditions.sort()
    # write_conditions_to_file(conditions)
