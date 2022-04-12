from dataclasses import dataclass, field
from itertools import count
from pprint import pprint
from string import ascii_uppercase

from faker import Faker

fake = Faker()
Counter = count()


def member_id() -> str:
    return fake.unique.bothify("???#########", letters=ascii_uppercase)


def group() -> str:
    return fake.bothify("######")


def name() -> str:
    return fake.company()


def policy_number() -> str:
    return fake.bothify("#####")


def in_network() -> str:
    return fake.boolean(chance_of_getting_true=80)


def increment_id():
    return next(Counter)


@dataclass
class InsuranceProvider:
    provider_id: int = field(default_factory=increment_id)
    insurance_name: str = field(default_factory=name)
    my_policy_number: str = field(default_factory=policy_number)
    is_in_network: bool = field(default_factory=in_network)


if __name__ == "__main__":
    for _ in range(10):
        pprint(InsuranceProvider())
