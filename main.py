# pylint: skip-file
from typing import Iterable
from pprint import pprint
from auto_increment import AutoIncrement

auto_inc = AutoIncrement()


def insert_into(table_name: str, column_names: Iterable[str], values: Iterable) -> str:
    combined = ",\n".join(values)
    columns = (f"{column}" for column in column_names)
    header = f"/* INSERT DATA INTO `{table_name}` TABLE */\n"
    return (
        header + f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{combined};"
    )


if __name__ == "__main__":
    pass
