# pylint: disable=missing-module-docstring
from typing import Iterable


def insert_into(table_name: str, column_names: Iterable[str], values: Iterable) -> str:
    """Create a SQL insert statement"""
    combined = ",\n".join(values)
    columns = (f"{column}" for column in column_names)
    header = f"/* INSERT DATA INTO `{table_name}` TABLE */\n"
    return (
        header + f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{combined};"
    )


if __name__ == "__main__":
    pass
