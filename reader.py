import csv
from dataclasses import dataclass
from typing import List

from main import insert_into


@dataclass
class Code:
    category_code: str
    variant: int
    complete_code: str
    name: str
    name_duplicate: str
    category: str

    @property
    def insert(self):
        attributes = (self.complete_code, self.category_code, self.name)
        # return f"({', '.join(attributes)})"
        return attributes


def reader() -> List[Code]:
    filename = "icd_codes.csv"
    with open(filename, mode="rt", encoding="utf-8", newline="\n") as csv_file:
        code_reader = csv.reader(
            csv_file,
        )
        code_list = []
        for line_number, row in enumerate(code_reader, 1):
            # if line_number > 20:
            # break
            try:
                code_list.append(Code(*row))
            except ValueError as error:
                raise ValueError(
                    f"{filename} contains a non-integer value on line: {line_number}.\n"
                    + f"The line's values were '${row}'"
                ) from error
        return code_list


def write_categories_to_file(code_data: List[Code]):
    # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
    category_input = set((code.category_code, code.category) for code in code_data)
    table_name = "category"
    columns = ["category_code", "category_name"]
    with open("insert_categories.sql", "wt", encoding="utf-8") as f:
        print(insert_into(table_name, columns, map(str, iter(category_input))), file=f)


def write_conditions_to_file(code_data: List[Code]):
    columns = ["icd_code", "category_id", "condition_name"]
    table_name = "condition"
    data = (code.insert for code in code_data)
    with open("insert_conditions.sql", "wt", encoding="utf-8") as f:
        print(insert_into(table_name, columns, map(str, data)), file=f)


if __name__ == "__main__":
    codes = reader()
    # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
    largest = ""
    for code in codes:
        largest = max(largest, code.complete_code, key=len)
    print(largest)
    print(len(largest))
    # write_categories_to_file(codes)
    # write_conditions_to_file(codes)
