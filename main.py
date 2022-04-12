# pylint: skip-file
from typing import Iterable
import mock
import insurance
from pprint import pprint


def insert_into(table_name: str, column_names: Iterable[str], values: Iterable) -> str:
    combined = ",\n\n".join(values)
    columns = (f"`{column}`" for column in column_names)
    return f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES\n\n{combined};"


if __name__ == "__main__":
    examples = [
        mock.address,
        mock.email,
        mock.name,
        mock.phone,
        mock.ssn,
        mock.dea_number,
        mock.date_between,
        mock.file,
        mock.physician_license,
        mock.physician_assistant_license,
        mock.phone,
        insurance.group,
        insurance.member_id,
        insurance.name,
        insurance.in_network,
        insurance.policy_number,
    ]
    print_quantity = 5
    for example in examples:
        print("=" * 30)
        print(f"{example.__name__}() random results....")
        for _ in range(print_quantity):
            pprint(example())
