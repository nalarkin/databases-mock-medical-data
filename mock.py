# pylint: skip-file
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime
from itertools import count
from pprint import pprint
from string import ascii_uppercase
from faker.providers import person

from faker import Faker

from insurance import InsuranceProvider, group, member_id

fake = Faker()
Faker.seed(0)
Counter = count()


def name() -> str:
    # TODO: Potentially add custom name building, to prevent prefixes and suffixes from happening,
    return fake.name()


def ssn() -> str:
    return fake.unique.ssn()


def address() -> str:
    # return fake.address().replace('\n', ' ')
    return fake.address()


def nurse_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="RN-####")


def dea_number() -> str:
    """https://en.wikipedia.org/wiki/DEA_number"""
    return f"{fake.bothify('?', letters='BM')}{fake.unique.bothify(text='?#######', letters=ascii_uppercase)}"


def physician_assistant_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="PA-####")


def physician_license() -> str:
    return fake.unique.bothify(text="GP-####")


def phone() -> str:
    return fake.unique.phone_number()


def file() -> str:
    return fake.file_name()


def email() -> str:
    return fake.email()


def date_between(start_date="-30y", end_date="today") -> datetime:
    return fake.date_between(start_date=start_date, end_date=end_date)


def build_gender_dict():
    options = [("Male", 0.4), ("Female", 0.4)]
    other_genders = ["Genderfluid", "Nonbinary", "Transgender"]
    for option in other_genders:
        options.append((option, 0.2 / len(other_genders)))
    return options


def company():
    return fake.company()


gender_options = OrderedDict(build_gender_dict())


def gender() -> str:
    return fake.random_element(elements=gender_options)


def role() -> str:
    options = [
        "Physician General Practitioner",
        "Nurse",
        "Orderly",
        "Receptionist",
        "Physician Assistant",
    ]
    return fake.random_element(elements=options)


def increment_id() -> int:
    return next(Counter)


def business_slogan() -> str:
    return fake.bs()


def random_immunization() -> str:
    options = [
        "Tuberculosis",
        "Hepatitis B",
        "Poliovirus",
        "Diphtheria",
        "Tetanus",
        "Pertussis",
        "Haemophilus Influenza Type B",
        "Pneumococcal diseases",
        "Rotavirus",
        "Measles",
        "Mumps",
        "Rubella",
        "Human papillomavirus",
    ]
    return fake.random_element(elements=options)


def random_specialization() -> str:
    options = [
        "Allergy",
        "Anesthesia",
        "Bariatric Medicine/Surgery",
        "Burn/Trauma",
        "Cardiac Catheterization",
        "Cardiology",
        "Cardiovascular Surgery",
        "Colorectal Surgery",
        "Dermatology",
        "Electrophysiology",
        "Emergency Medicine",
        "Endocrinology",
        "Family Practice",
        "Gastroenterology",
        "General Surgery",
        "Geriatrics",
        "Gynecologic Oncology",
        "Hematology/Oncology",
        "Hepatobiliary",
        "Infectious Disease",
        "Internal Medicine",
        "Neonatology",
        "Nephrology",
        "Neurology",
        "Neurosurgery",
        "Nuclear Medicine",
        "Obstetrics & Gynecology",
        "Occupational Medicine",
        "Ophthalmology",
        "Oral Surgery",
        "Orthopedics",
        "Otolaryngology / Head & Neck Surgery",
        "Pain Management",
        "Palliative Care",
        "Pain Management",
        "Palliative Care",
        "Pathology: Surgical & Anatomic",
        "Pediatrics",
        "Pediatric Surgery",
        "Psychiatry",
    ]
    return fake.random_element(elements=options)


def random_relative_type():
    options = [
        "sister",
        "brother",
        "mother",
        "father",
        "grandmother",
        "grandfather",
        "aunt",
        "uncle",
        "great-grandmother",
        "great-grandfather",
    ]
    return fake.random_element(elements=options)


def random_notes(chance=60, sentences=3):
    if fake.boolean(chance_of_getting_true=chance):
        return fake.paragraph(nb_sentences=sentences)
    return None


@dataclass
class Patient:
    patient_id: int = field(default_factory=increment_id)
    phone_number: str = field(default_factory=phone)
    birthday: datetime = field(
        default_factory=lambda: date_between(start_date="-60y", end_date="-1y")
    )
    my_email: str = field(default_factory=email)
    my_ssn: str = field(default_factory=ssn)
    my_address: str = field(default_factory=address)
    my_name: str = field(default_factory=name)
    my_gender: str = field(default_factory=gender)


@dataclass
class Employee:
    emp_id: int = field(default_factory=increment_id)
    phone_number: str = field(default_factory=phone)
    birthday: datetime = field(
        default_factory=lambda: date_between(start_date="-60y", end_date="-20y")
    )
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
        if self.my_role in ["Receptionist", "Orderly"]:
            self.salary = fake.random.randint(15_000, 80_000)
        elif self.my_role == "Nurse":
            self.salary = fake.random.randint(54_000, 100_000)
            self.my_medical_license_number = nurse_license()
            self.my_dea_number = dea_number()
        elif self.my_role == "Physician Assistant":
            self.salary = fake.random.randint(94_000, 130_000)
            self.my_medical_license_number = physician_assistant_license()
            self.my_dea_number = dea_number()
        elif self.my_role == "Physician General Practitioner":
            self.salary = fake.random.randint(160_000, 260_000)
            self.my_medical_license_number = physician_license()
            self.my_dea_number = dea_number()
        else:
            raise ValueError(f"{self.my_role} does not fit into the possible roles.")


@dataclass
class ArchivedFile:
    patient_id: int
    emp_id: int
    file_id: int = field(default_factory=increment_id)
    file_name: str = field(default_factory=file)
    # TODO: Do we want to use mock blobs?
    file_blob: str = field(default=None)


def generate_archived_file(patient: Patient, employee: Employee) -> ArchivedFile:
    return ArchivedFile(patient_id=patient.patient_id, emp_id=employee.emp_id)


@dataclass
class SpecializedLab:
    lab_id: int = field(default_factory=increment_id)
    phone_number: str = field(default_factory=phone)
    my_address: str = field(default_factory=address)


@dataclass
class Test:
    test_id: int = field(default_factory=increment_id)
    test_Name: str = field(default_factory=business_slogan)


@dataclass
class TestAccepted:
    test_id: int
    lab_id: int


def generate_test_accepted(lab: SpecializedLab, test: Test) -> TestAccepted:
    return TestAccepted(test_id=test.test_id, lab_id=lab.lab_id)


@dataclass
class Pharmacy:
    pharmacy_address: str = field(default_factory=address)
    pharmacy_name: str = field(default_factory=company)


@dataclass
class Immunization:
    immunization_id: int = field(default_factory=increment_id)
    immunization_type: str = field(default_factory=random_immunization)


@dataclass
class EmpImmunization:
    immunization_id: int
    emp_id: int


def generate_emp_immunization(
    immunization: Immunization, employee: Employee
) -> EmpImmunization:
    return EmpImmunization(
        immunization_id=immunization.immunization_id, emp_id=employee.emp_id
    )


@dataclass
class ImmunizedBy:
    immunization_id: int
    patient_id: int


def generate_immunized_by(immunization: Immunization, patient: Patient) -> ImmunizedBy:
    return ImmunizedBy(
        immunization_id=immunization.immunization_id, patient_id=patient.patient_id
    )


@dataclass
class ReferrableDoctor:
    ref_doctor_id: int = field(default_factory=increment_id)
    my_name: str = field(default_factory=name)
    specialization: str = field(default_factory=random_specialization)
    phone_number: str = field(default_factory=phone)


@dataclass
class Referral:
    emp_id: int
    ref_doctor_id: int
    patient_id: int
    ref_id: int = field(default_factory=increment_id)


def generate_referrel(
    employee: Employee, referrable: ReferrableDoctor, patient: Patient
) -> Referral:
    return Referral(
        emp_id=employee.emp_id,
        ref_doctor_id=referrable.ref_doctor_id,
        patient_id=patient.patient_id,
    )


@dataclass
class CoveredBy:
    provider_id: int
    patient_id: int
    my_member_id: str = field(default_factory=member_id)
    group_number: str = field(default_factory=group)
    policy_holder_name: str = field(default_factory=name)


def generate_covered_by(
    patient: Patient, insurance_provider: InsuranceProvider
) -> CoveredBy:
    policy_holder_name = (
        patient.my_name if fake.boolean(chance_of_getting_true=95) else name()
    )
    return CoveredBy(
        provider_id=insurance_provider.provider_id,
        patient_id=patient.patient_id,
        policy_holder_name=policy_holder_name,
    )


@dataclass
class Relative:
    patient_id: int
    relative_id: int = field(default_factory=increment_id)
    relative_type: str = field(default_factory=random_relative_type)
    additional_notes: str = field(default_factory=random_notes, repr=False)


def generate_relative(patient: Patient) -> CoveredBy:
    return Relative(patient_id=patient.patient_id)


@dataclass
class Prescription:
    pharmacy_address: str
    emp_id: int
    patient_id: int
    prescription_id: int = field(default_factory=increment_id)
    # TODO: come up with better drug name generator?
    drug_name: str = field(default_factory=company)
    quantity: int = field(default_factory=lambda: fake.random.randint(1, 180))
    refills: int = field(default_factory=lambda: fake.random.randint(0, 7))
    instructions: str = field(default_factory=lambda: random_notes(90, 5), repr=False)
    prescription_date: datetime = field(default_factory=lambda: date_between("-7y"))


def generate_prescription(
    pharmacy: Pharmacy, employee: Employee, patient: Patient
) -> Prescription:
    return Prescription(
        pharmacy_address=pharmacy.pharmacy_address,
        emp_id=employee.emp_id,
        patient_id=patient.patient_id,
    )


if __name__ == "__main__":
    for _ in range(5):
        pprint(generate_prescription(Pharmacy(), Employee(), Patient()))
