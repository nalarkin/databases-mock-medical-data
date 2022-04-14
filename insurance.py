from dataclasses import dataclass, field
from itertools import count
from pprint import pprint
from string import ascii_uppercase

from faker import Faker

fake = Faker()
Counter = count()


def random_member_id() -> str:
    return fake.unique.bothify("???#########", letters=ascii_uppercase)


def random_group() -> str:
    return fake.bothify("######")


def random_company_name() -> str:
    return fake.company()


def random_policy_number() -> str:
    return fake.bothify("#####")


def random_in_network() -> str:
    return fake.boolean(chance_of_getting_true=80)


def increment_id():
    return next(Counter)


@dataclass
class InsuranceProvider:
    provider_id: int = field(default_factory=increment_id)
    insurance_name: str = field(default_factory=random_company_name)
    my_policy_number: str = field(default_factory=random_policy_number)
    is_in_network: bool = field(default_factory=random_in_network)
    table_name: str = field(default="InsuranceProviders", init=False)


if __name__ == "__main__":
    for _ in range(10):
        pprint(InsuranceProvider())
