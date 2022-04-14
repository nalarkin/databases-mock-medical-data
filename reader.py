from typing import List

from main import insert_into
from icd import (
    MedicalCondition,
    MedicalConditionCategory,
    read_categories_from_file,
    read_conditions_from_file,
)


def write_categories_to_file(code_data: List[MedicalConditionCategory]):
    # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
    category_input = set((code.category_code, code.category) for code in code_data)
    table_name = "category"
    columns = ["category_code", "category_name"]
    with open("insert_categories.sql", "wt", encoding="utf-8") as f:
        print(insert_into(table_name, columns, map(str, iter(category_input))), file=f)


def write_conditions_to_file(code_data: List[MedicalCondition]):
    columns = ["icd_code", "category_id", "condition_name"]
    table_name = "condition"
    data = ((code.icd_code, code.category_id, code.name) for code in code_data)
    with open("insert_conditions.sql", "wt", encoding="utf-8") as f:
        print(insert_into(table_name, columns, map(str, data)), file=f)


if __name__ == "__main__":
    codes = read_categories_from_file()
    # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
    largest = ""
    for code in codes:
        largest = max(largest, code.category_name, key=len)
    print(largest)
    print(len(largest))
    # write_categories_to_file(codes)
    # write_conditions_to_file(codes)
