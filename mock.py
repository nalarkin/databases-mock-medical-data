# pylint: skip-file
from faker import Faker
from pprint import pprint
from string import ascii_uppercase
from dataclasses import dataclass, field
from datetime import datetime
from collections import OrderedDict
from itertools import count

fake = Faker()
Faker.seed(0)
Counter = count()

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

def physician_assistant_license()-> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text='PA-####')

def physician_license()-> str:
    return fake.unique.bothify(text='GP-####')

def phone()-> str:
    return fake.unique.phone_number()

def file()-> str:
    return fake.file_name()

def email()-> str:
    return fake.email()

def date_between(start_date = '-30y', end_date = 'today') -> datetime:
    return fake.date_between(start_date=start_date, end_date=end_date)

def build_gender_dict():
    options = [('Male', 0.4), ('Female', 0.4)]
    other_genders = ['Genderfluid', 'Nonbinary', 'Transgender']
    for option in other_genders:
        options.append((option, 0.2 / len(other_genders)))
    return options


gender_options = OrderedDict(build_gender_dict())

def gender() -> str:
    return fake.random_elements(elements=gender_options, unique=False, length=1)[0]


def role() -> str:
    options = ['Physician General Practitioner', 'Nurse', 'Orderly', 'Receptionist', 'Physician Assistant']
    return fake.random_elements(elements=options, length=1)[0]

@dataclass
class Patient:
    patient_id: int = field(default_factory=lambda: next(Counter)) 
    phone_number: str = field(default_factory=phone)
    birthday: datetime = field(default_factory=lambda: date_between(start_date='-60y', end_date='-1y'))
    my_email: str = field(default_factory=email)
    my_ssn: str = field(default_factory=ssn)
    my_address: str = field(default_factory=address)
    my_name: str = field(default_factory=name)
    my_gender: str = field(default_factory=gender)

@dataclass
class Employee:
    emp_id: int = field(default_factory=lambda: next(Counter)) 
    phone_number: str = field(default_factory=phone)
    birthday: datetime = field(default_factory=lambda: date_between(start_date='-60y', end_date='-20y'))
    my_email: str = field(default_factory=email)
    my_ssn: str = field(default_factory=ssn)
    my_address: str = field(default_factory=address)
    my_name: str = field(default_factory=name)
    my_gender: str = field(default_factory=gender)
    my_role: str = field(default_factory=role)
    salary: int = field(init=False)
    my_dea_number: str = field(init=False, default=None)
    my_medical_license_number: str = field(init=False, default=None)

    def __post_init__(self):
        """This logic assigns the salary and medical license based on the randomly assigned my_role attribute"""
        if self.my_role in ['Receptionist', 'Orderly']:
            self.salary = fake.random.randint(15_000, 80_000)
        elif self.my_role == 'Nurse':
            self.salary = fake.random.randint(54_000, 100_000)
            self.my_medical_license_number = nurse_license()
            self.my_dea_number = dea_number()
        elif self.my_role == 'Physician Assistant':
            self.salary = fake.random.randint(94_000, 130_000)
            self.my_medical_license_number = physician_assistant_license()
            self.my_dea_number = dea_number()
        elif self.my_role == 'Physician General Practitioner':
            self.salary = fake.random.randint(160_000, 260_000)
            self.my_medical_license_number = physician_license()
            self.my_dea_number = dea_number()
        else:
            raise ValueError(f'{self.my_role} does not fit into the possible roles.')
            
if __name__ == '__main__':
    patients = [Employee() for _ in range(10)] 
    for patient in patients:
        pprint(patient)
