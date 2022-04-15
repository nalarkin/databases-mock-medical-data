from typing import Iterable, List


def insert_into(table_name: str, column_names: Iterable[str], values: Iterable) -> str:
    combined = ",\n".join(values)
    columns = (f"{column}" for column in column_names)
    header = f"/* INSERT DATA INTO `{table_name}` TABLE */\n"
    return (
        header + f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{combined};"
    )


# def write_categories_to_file(code_data: List[MedicalConditionCategory]):
#     # TODO: Instead of reading categories from icd_code.csv, read it from icd_categories.csv
#     category_input = set((code.category_code, code.category) for code in code_data)
#     table_name = "category"
#     columns = ["category_code", "category_name"]
#     with open("insert_categories.sql", "wt", encoding="utf-8") as f:
#         print(insert_into(table_name, columns, map(str, iter(category_input))), file=f)


# def write_conditions_to_file(code_data: List[MedicalCondition]):
#     columns = ["icd_code", "category_id", "condition_name"]
#     table_name = "condition"
#     data = ((code.icd_code, code.category_id, code.name) for code in code_data)
#     with open("insert_conditions.sql", "wt", encoding="utf-8") as f:
#         print(insert_into(table_name, columns, map(str, data)), file=f)


if __name__ == "__main__":
    pass
