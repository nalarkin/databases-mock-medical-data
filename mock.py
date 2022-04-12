# pylint: skip-file
from faker import Faker
from pprint import pprint
from string import ascii_uppercase
from dataclasses import dataclass
from datetime import datetime

fake = Faker()
Faker.seed(0)

def name() -> str:
    return fake.name()

def ssn() -> str:
    return fake.unique.ssn()

def address() -> str:
    # return fake.address().replace('\n', ' ')
    return fake.address()

def nurse_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text='RN-####')

def dea_number()-> str:
    """https://en.wikipedia.org/wiki/DEA_number"""
    return f"{fake.bothify('?', letters='BM')}{fake.unique.bothify(text='?#######', letters=ascii_uppercase)}"

def physician_assistant()-> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text='PA-####')

def physician()-> str:
    return fake.unique.bothify(text='GP-####')

def phone()-> str:
    return fake.unique.phone_number()

def file()-> str:
    return fake.file_name()

def email()-> str:
    return fake.email()

def date_between(start_date = '-30y', end_date = 'today') -> datetime:
    return fake.date_between(start_date=start_date, end_date=end_date)


if __name__ == '__main__':
    for _ in range(10):
        pprint(address())
