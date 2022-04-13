# pylint: skip-file
from asyncore import write
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime
from itertools import count
from pprint import pprint
from string import ascii_uppercase
from typing import List, Optional

from faker import Faker
from faker.providers import person

from auto_increment import AutoIncrement
from icd import MedicalCondition, read_conditions_from_file
from insurance import InsuranceProvider, random_group, random_member_id
from operator import attrgetter

from main import insert_into

fake = Faker()
Faker.seed(0)
Counter = count()

auto_id = AutoIncrement()


def random_name() -> str:
    # TODO: Potentially add custom name building, to prevent prefixes and suffixes from happening,
    return fake.name()


def random_ssn() -> str:
    return fake.unique.ssn()


def random_address() -> str:
    # return fake.address().replace('\n', ' ')
    return fake.address()


def random_nurse_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="RN-####")


def random_dea_number() -> str:
    """https://en.wikipedia.org/wiki/DEA_number"""
    return f"{fake.bothify('?', letters='BM')}{fake.unique.bothify(text='?#######', letters=ascii_uppercase)}"


def random_physician_assistant_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="PA-####")


def random_physician_license() -> str:
    return fake.unique.bothify(text="GP-####")


def random_phone() -> str:
    return fake.unique.phone_number()


def random_file() -> str:
    return fake.file_name()


def random_email() -> str:
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


def random_gender() -> str:
    return fake.random_element(elements=gender_options)


def random_role() -> str:
    options = [
        "Physician General Practitioner",
        "Nurse",
        "Orderly",
        "Receptionist",
        "Physician Assistant",
    ]
    return fake.random_element(elements=options)


def business_slogan() -> str:
    return fake.bs()


IMMUNIZATION_TYPES = [
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


def random_immunization() -> str:
    return fake.random_element(elements=IMMUNIZATION_TYPES)


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


def random_notes(chance=60, sentences=3) -> Optional[str]:
    if fake.boolean(chance_of_getting_true=chance):
        return fake.paragraph(nb_sentences=sentences)
    return None


def random_blood_pressure():
    systolic = fake.random.randint(80, 160)
    diastolic = fake.random.randint(60, 100)
    return f"{systolic}/{diastolic}"


def random_covid_exam():
    options = ["PCR", "Antigen"]
    return fake.random_element(elements=options)


def random_blood_type():
    blood_types = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]
    return fake.random_element(elements=blood_types)


def random_blood_sugar():
    return fake.random.randint(70, 120)


def get_attributes(cls, excluded=None):
    if excluded is None:
        excluded = []
    return [
        attr for attr in dir(cls) if not attr.startswith("_") and attr not in excluded
    ]


def get_attribute_values(cls, attributes):
    return tuple(getattr(cls, attr) for attr in attributes)


@dataclass
class Patient:
    patient_id: int = field(default_factory=lambda: auto_id.next_id("Patient"))
    phone_number: str = field(default_factory=random_phone, repr=False)
    birthday: datetime = field(
        default_factory=lambda: date_between(start_date="-60y", end_date="-1y"),
        repr=False,
    )
    email: str = field(default_factory=random_email, repr=False)
    ssn: str = field(default_factory=random_ssn, repr=False)
    address: str = field(default_factory=random_address, repr=False)
    name: str = field(default_factory=random_name, repr=False)
    gender: str = field(default_factory=random_gender, repr=False)

    @property
    def columns(self) -> str:
        return f"{('patient_id', 'phone_number', 'birthday', 'email', 'ssn', 'address', 'name', 'gender')}"

    @property
    def row_values(self) -> str:
        return ""

    def example_function(self):
        return ""


@dataclass
class Employee:
    emp_id: int = field(default_factory=lambda: auto_id.next_id("Employee"))
    phone_number: str = field(default_factory=random_phone, repr=False)
    birthday: datetime = field(
        default_factory=lambda: date_between(start_date="-60y", end_date="-20y"),
        repr=False,
    )
    email: str = field(default_factory=random_email, repr=False)
    ssn: str = field(default_factory=random_ssn)
    address: str = field(default_factory=random_address, repr=False)
    name: str = field(default_factory=random_name, repr=False)
    gender: str = field(default_factory=random_gender, repr=False)
    role: str = field(default_factory=random_role, repr=False)
    salary: int = field(init=False, repr=False)
    dea_number: str = field(init=False, default=None, repr=False)
    medical_license_number: str = field(init=False, default=None, repr=False)

    def __post_init__(self):
        """This logic assigns the salary and medical license based on the randomly assigned role attribute"""
        if self.role in ["Receptionist", "Orderly"]:
            self.salary = fake.random.randint(15_000, 80_000)
        elif self.role == "Nurse":
            self.salary = fake.random.randint(54_000, 100_000)
            self.medical_license_number = random_nurse_license()
            self.dea_number = random_dea_number()
        elif self.role == "Physician Assistant":
            self.salary = fake.random.randint(94_000, 130_000)
            self.medical_license_number = random_physician_assistant_license()
            self.dea_number = random_dea_number()
        elif self.role == "Physician General Practitioner":
            self.salary = fake.random.randint(160_000, 260_000)
            self.medical_license_number = random_physician_license()
            self.dea_number = random_dea_number()
        else:
            raise ValueError(f"{self.role} does not fit into the possible roles.")


@dataclass
class ArchivedFile:
    patient_id: int
    emp_id: int
    file_id: int = field(default_factory=lambda: auto_id.next_id("ArchivedFile"))
    file_name: str = field(default_factory=random_file)
    # TODO: Do we want to use mock blobs?
    file_blob: str = field(default=None)


def generate_archived_file(patient: Patient, employee: Employee) -> ArchivedFile:
    return ArchivedFile(patient_id=patient.patient_id, emp_id=employee.emp_id)


@dataclass
class SpecializedLab:
    lab_id: int = field(default_factory=lambda: auto_id.next_id("SpecializedLab"))
    phone_number: str = field(default_factory=random_phone)
    address: str = field(default_factory=random_address)


@dataclass
class Test:
    test_id: int = field(default_factory=lambda: auto_id.next_id("Test"))
    test_name: str = field(default_factory=business_slogan)


@dataclass
class TestAccepted:
    test_id: int
    lab_id: int


def generate_test_accepted(lab: SpecializedLab, test: Test) -> TestAccepted:
    return TestAccepted(test_id=test.test_id, lab_id=lab.lab_id)


@dataclass
class Pharmacy:
    pharmacy_address: str = field(default_factory=random_address)
    pharmacy_name: str = field(default_factory=company)


@dataclass
class Immunization:
    immunization_id: int = field(
        default_factory=lambda: auto_id.next_id("Immunization")
    )
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
    ref_doctor_id: int = field(
        default_factory=lambda: auto_id.next_id("ReferrableDoctor")
    )
    name: str = field(default_factory=random_name)
    specialization: str = field(default_factory=random_specialization)
    phone_number: str = field(default_factory=random_phone)


@dataclass
class Referral:
    emp_id: int
    ref_doctor_id: int
    patient_id: int
    ref_id: int = field(default_factory=lambda: auto_id.next_id("Referral"))


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
    member_id: str = field(default_factory=random_member_id)
    group_number: str = field(default_factory=random_group)
    policy_holder_name: str = field(default_factory=random_name)


def generate_covered_by(
    patient: Patient, insurance_provider: InsuranceProvider
) -> CoveredBy:
    policy_holder_name = (
        patient.name if fake.boolean(chance_of_getting_true=95) else random_name()
    )
    return CoveredBy(
        provider_id=insurance_provider.provider_id,
        patient_id=patient.patient_id,
        policy_holder_name=policy_holder_name,
    )


@dataclass
class Relative:
    patient_id: int
    relative_id: int = field(default_factory=lambda: auto_id.next_id("Relative"))
    relative_type: str = field(default_factory=random_relative_type)
    additional_notes: Optional[str] = field(default_factory=random_notes, repr=False)


def generate_relative(patient: Patient) -> CoveredBy:
    return Relative(patient_id=patient.patient_id)


@dataclass
class RelativeCondition:
    relative_id: int
    icd_code: str


def generate_relative_condition(
    relative: Relative, condition: MedicalCondition
) -> CoveredBy:
    return RelativeCondition(
        relative_id=relative.relative_id, icd_code=condition.icd_code
    )


@dataclass
class Prescription:
    pharmacy_address: str
    emp_id: int
    patient_id: int
    prescription_id: int = field(
        default_factory=lambda: auto_id.next_id("Prescription")
    )
    # TODO: come up with better drug name generator?
    drug_name: str = field(default_factory=company, repr=False)
    quantity: int = field(default_factory=lambda: fake.random.randint(1, 180))
    refills: int = field(default_factory=lambda: fake.random.randint(0, 7))
    instructions: Optional[str] = field(
        default_factory=lambda: random_notes(90, 5), repr=False
    )
    prescription_date: datetime = field(default_factory=lambda: date_between("-7y"))


def generate_prescription(
    pharmacy: Pharmacy, employee: Employee, patient: Patient
) -> Prescription:
    return Prescription(
        pharmacy_address=pharmacy.pharmacy_address,
        emp_id=employee.emp_id,
        patient_id=patient.patient_id,
    )


@dataclass
class Appointment:
    patient_id: int
    app_id: int = field(default_factory=lambda: auto_id.next_id("Appointment"))
    room_number: int = field(default_factory=lambda: fake.random.randint(0, 20))
    blood_pressure: str = field(default_factory=random_blood_pressure)
    weight: float = field(
        default_factory=lambda: round(fake.random.uniform(70.0, 400.0), 2)
    )
    height: float = field(
        default_factory=lambda: round(fake.random.uniform(50.0, 80.0), 2)
    )
    temperature: float = field(
        default_factory=lambda: round(fake.random.uniform(96.0, 106.0), 2)
    )
    notes: Optional[str] = field(default_factory=lambda: random_notes())


def generate_appointment(patient: Patient) -> Appointment:
    return Appointment(patient_id=patient.patient_id)


@dataclass
class LabReport:
    icd_code: str
    file_id: int
    app_id: int
    report_id: int = field(default_factory=lambda: auto_id.next_id("LabReport"))
    info: Optional[str] = field(default_factory=lambda: random_notes(80, 2))
    result_info: Optional[str] = field(default_factory=lambda: random_notes(80, 3))


def generate_lab_report(
    medical_condition: MedicalCondition,
    appointment: Appointment,
    file: ArchivedFile = None,
) -> LabReport:
    return LabReport(
        icd_code=medical_condition.icd_code,
        file_id=file.file_id if file else None,
        app_id=appointment.app_id,
    )


@dataclass
class Experiencing:
    app_id: int
    icd_code: str
    comment: Optional[str] = field(default_factory=lambda: random_notes(40, 2))


def generate_experiencing(
    appointment: Appointment, medical_condition: MedicalCondition
) -> Experiencing:
    return Experiencing(app_id=appointment.app_id, icd_code=medical_condition.icd_code)


@dataclass
class MedicalStaff:
    emp_id: int
    app_id: int


def generate_medical_staff(
    employee: Employee, appointment: Appointment
) -> MedicalStaff:
    return MedicalStaff(emp_id=employee.emp_id, app_id=appointment.app_id)


@dataclass
class Diagnosis:
    emp_id: int
    patient_id: int
    app_id: int
    icd_code: str
    comment: Optional[str] = field(default_factory=lambda: random_notes(90, 3))


def generate_diagnosis(
    employee: Employee,
    appointment: Appointment,
    patient: Patient,
    medical_condition: MedicalCondition,
) -> Diagnosis:
    return Diagnosis(
        emp_id=employee.emp_id,
        patient_id=patient.patient_id,
        app_id=appointment.app_id,
        icd_code=medical_condition.icd_code,
    )


@dataclass
class ConductedBy:
    report_id: int
    lab_id: int


def generate_conducted_by(
    report: LabReport, specialized_lab: SpecializedLab
) -> ConductedBy:
    return ConductedBy(report_id=report.report_id, lab_id=specialized_lab.lab_id)


@dataclass
class Exam:
    report_id: int
    app_id: int
    exam_id: int = field(default_factory=lambda: auto_id.next_id("Exam"))
    comment: Optional[str] = field(default_factory=lambda: random_notes(60, 2))


def generate_exam(report: LabReport, appointment: Appointment) -> Exam:
    return Exam(report_id=report.report_id, app_id=appointment.app_id)


@dataclass
class ExamInterface:
    exam_id: int


@dataclass
class CovidExam(ExamInterface):
    # exam_id: int
    test_type: str = field(default_factory=random_covid_exam)
    is_positive: bool = field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=10)
    )


@dataclass
class BloodExam(ExamInterface):
    blood_type: str = field(default_factory=random_blood_type)
    blood_sugar: int = field(default_factory=random_blood_sugar)


@dataclass
class VaccineAdministration(ExamInterface):
    vaccine_type: str = field(default_factory=random_immunization)


@dataclass
class MockGeneratorConfig:
    # independent schema
    patient_count: int = field(default=5)
    employee_count: int = field(default=5)
    insurance_provider_count: int = field(default=5)
    test_count: int = field(default=5)
    specialized_lab_count: int = field(default=5)
    pharmacy_count: int = field(default=5)
    immunization_count: int = field(default=5)
    referrable_doctor_count: int = field(default=5)

    # all schema below are dependent schema
    covered_by_count: int = field(default=5)
    relative_count: int = field(default=5)
    prescription_count: int = field(default=5)
    immunized_by_count: int = field(default=5)
    emp_immunization_count: int = field(default=5)
    referral_count: int = field(default=5)
    appointment_count: int = field(default=5)

    # M-N relationships, partial participation
    lab_report_count: int = field(default=5)
    exam_count: int = field(default=5)
    archived_file_count: int = field(default=5)

    # M-N relationships, total participation
    medical_staff_count_max: int = field(default=3)
    test_accepted_count_max: int = field(default=3)
    diagnosis_count_max: int = field(default=2)
    experiencing_count_max: int = field(default=2)
    relative_condition_max: int = field(default=2)


@dataclass
class MockGenerator:
    medical_conditions: List[MedicalCondition]
    config: MockGeneratorConfig = field(repr=False)

    patients: List[Patient] = field(init=False)
    employees: List[Employee] = field(init=False)
    insurance_providers: List[InsuranceProvider] = field(init=False)
    tests: List[Test] = field(init=False)
    specialized_labs: List[SpecializedLab] = field(init=False)
    pharmacies: List[Pharmacy] = field(init=False)
    immunizations: List[Immunization] = field(init=False)
    referrable_doctors: List[ReferrableDoctor] = field(init=False)

    # all schema below are dependent schema
    appointments: List[Appointment] = field(init=False, default_factory=list)
    covered_bys: List[CoveredBy] = field(init=False, default_factory=list)
    relatives: List[Relative] = field(init=False, default_factory=list)
    prescriptions: List[Prescription] = field(init=False, default_factory=list)
    immunized_bys: List[ImmunizedBy] = field(init=False, default_factory=list)
    emp_immunizations: List[EmpImmunization] = field(init=False, default_factory=list)
    referrals: List[Referral] = field(init=False, default_factory=list)
    conducted_bys: List[ConductedBy] = field(init=False, default_factory=list)
    blood_exams: List[BloodExam] = field(init=False, default_factory=list)
    covid_exams: List[CovidExam] = field(init=False, default_factory=list)
    vaccine_administered: List[VaccineAdministration] = field(
        init=False, default_factory=list
    )

    # M-N relationships, partial participation
    lab_reports: List[LabReport] = field(init=False, default_factory=list)
    exams: List[Exam] = field(init=False, default_factory=list)
    archived_files: List[ArchivedFile] = field(init=False, default_factory=list)

    # M-N relationships, total participation
    medical_staff: List[MedicalStaff] = field(init=False, default_factory=list)
    tests_accepted: List[TestAccepted] = field(init=False, default_factory=list)
    diagnosis: List[Diagnosis] = field(init=False, default_factory=list)
    experiencing: List[Experiencing] = field(init=False, default_factory=list)
    relative_conditions: List[RelativeCondition] = field(
        init=False, default_factory=list
    )

    def __post_init__(self):
        self._generate_independent_schema()
        self._generate_appointments(self.config.appointment_count)
        self._generate_covered_bys()
        self._generate_relatives()
        self._generate_prescriptions()
        self._generate_immunizations()
        self._generate_referrals()
        self._generate_archived_files()
        self._generate_medical_staff()
        self._generate_tests_accepted()
        self._generate_experiencing()
        self._generate_relative_conditions()
        self._generate_diagnosis()
        self._generate_lab_reports()
        self._generate_conducted_bys()
        self._generate_exams()
        self._generate_exam_subclasses()

    def _generate_independent_schema(self):
        self.patients = [Patient() for _ in range(self.config.patient_count)]
        self.employees = [Employee() for _ in range(self.config.employee_count)]
        self.insurance_providers = [
            InsuranceProvider() for _ in range(self.config.insurance_provider_count)
        ]
        self.tests = [Test() for _ in range(self.config.test_count)]
        self.specialized_labs = [
            SpecializedLab() for _ in range(self.config.specialized_lab_count)
        ]
        self.pharmacies = [Pharmacy() for _ in range(self.config.pharmacy_count)]
        self.immunizations = [
            Immunization() for _ in range(self.config.immunization_count)
        ]
        self.referrable_doctors = [
            ReferrableDoctor() for _ in range(self.config.referrable_doctor_count)
        ]

    def _generate_appointments(self, count: int):
        random_patients = fake.random_choices(elements=self.patients, length=count)
        self.appointments.extend(
            generate_appointment(patient) for patient in random_patients
        )

    def _generate_covered_bys(self):
        # TODO: Ensure there are no duplicates in this table, can possibly make covered by frozen, and use set
        quantity = self.config.covered_by_count
        self.covered_bys = [
            generate_covered_by(patient, provider)
            for patient, provider in self._random_selector(
                self.patients, self.insurance_providers, quantity=quantity
            )
        ]

    def _generate_relatives(self):
        random_patients = fake.random_choices(
            elements=self.patients, length=self.config.relative_count
        )
        self.relatives = [generate_relative(patient) for patient in random_patients]

    def _generate_prescriptions(self):
        quantity = self.config.prescription_count
        self.prescriptions = [
            generate_prescription(pharmacy, employee, patient)
            for pharmacy, employee, patient in self._random_selector(
                self.pharmacies, self.employees, self.patients, quantity=quantity
            )
        ]

    def _random_selector(self, *args, quantity=None) -> zip:
        if quantity is None:
            raise ValueError("Must specify quantity")
        return zip(
            *(iter(fake.random_choices(elements=arg, length=quantity)) for arg in args)
        )

    def _generate_immunizations(self):
        self.immunized_bys = [
            generate_immunized_by(immunization, patient)
            for immunization, patient in self._random_selector(
                self.immunizations,
                self.patients,
                quantity=self.config.immunized_by_count,
            )
        ]
        self.emp_immunizations = [
            generate_emp_immunization(immunization, employee)
            for immunization, employee in self._random_selector(
                self.immunizations,
                self.employees,
                quantity=self.config.immunized_by_count,
            )
        ]

    def _generate_referrals(self):
        self.referrals = [
            generate_referrel(employee, referrable, patient)
            for employee, referrable, patient in self._random_selector(
                self.employees,
                self.referrable_doctors,
                self.patients,
                quantity=self.config.referral_count,
            )
        ]

    def _generate_archived_files(self):
        self.archived_files = [
            generate_archived_file(patient, employee)
            for patient, employee in self._random_selector(
                self.patients, self.employees, quantity=self.config.archived_file_count
            )
        ]

    def _generate_medical_staff(self):
        """Every appointment must have at least 1 medical staff"""
        medical_staff = []
        for app in self.appointments:
            random_length = fake.random.randint(1, self.config.medical_staff_count_max)
            for employee in fake.random_elements(
                elements=self.employees, unique=True, length=random_length
            ):
                medical_staff.append(generate_medical_staff(employee, app))
        self.medical_staff = medical_staff

    def _generate_tests_accepted(self):
        """Every appointment must have at least 1 medical staff"""
        tests_accepted = []
        for lab in self.specialized_labs:
            random_length = fake.random.randint(1, self.config.test_accepted_count_max)
            for test in fake.random_elements(
                elements=self.tests, unique=True, length=random_length
            ):
                tests_accepted.append(generate_test_accepted(lab, test))
        self.tests_accepted = tests_accepted

    def _generate_experiencing(self):
        experiencing = []
        for app in self.appointments:
            random_length = fake.random.randint(1, self.config.experiencing_count_max)
            for condition in fake.random_elements(
                elements=self.medical_conditions, unique=True, length=random_length
            ):
                experiencing.append(generate_experiencing(app, condition))
        self.experiencing = experiencing

    def _generate_relative_conditions(self):
        relative_conditions = []
        for relative in self.relatives:
            random_length = fake.random.randint(1, self.config.relative_condition_max)
            for condition in fake.random_elements(
                elements=self.medical_conditions, unique=True, length=random_length
            ):
                relative_conditions.append(
                    generate_relative_condition(relative, condition)
                )
        self.relative_conditions = relative_conditions

    def _generate_diagnosis(self):
        diagnosis = []
        for app in self.appointments:
            random_length = fake.random.randint(0, self.config.diagnosis_count_max)
            random_employee = fake.random_element(elements=self.employees)
            for condition in fake.random_elements(
                elements=self.medical_conditions, unique=True, length=random_length
            ):
                diagnosis.append(
                    generate_diagnosis(
                        random_employee, app, Patient(app.patient_id), condition
                    )
                )
        self.diagnosis = diagnosis

    def _generate_lab_reports(self):
        self.lab_reports = [
            generate_lab_report(con, app, f)
            for con, app, f in self._random_selector(
                self.medical_conditions,
                self.appointments,
                self.archived_files,
                quantity=self.config.lab_report_count,
            )
        ]

    def _generate_conducted_bys(self):
        self.conducted_bys = [
            generate_conducted_by(report, lab)
            for report, lab in zip(
                self.lab_reports,
                fake.random_elements(
                    elements=self.specialized_labs, length=len(self.lab_reports)
                ),
            )
        ]

    def _generate_exams(self):
        self.exams = [
            generate_exam(report, app)
            for report, app in self._random_selector(
                self.lab_reports, self.appointments, quantity=self.config.exam_count
            )
        ]

    def _generate_exam_subclasses(self):
        arrays = [self.blood_exams, self.covid_exams, self.vaccine_administered]
        exam_types: List[ExamInterface] = [BloodExam, CovidExam, VaccineAdministration]
        for exam in self.exams:
            random_selection_idx = fake.random.randint(0, len(exam_types) - 1)
            arrays[random_selection_idx].append(
                exam_types[random_selection_idx](exam.exam_id)
            )


def build_insert_statement(cls_array):
    first = cls_array[0]
    attrs = get_attributes(first, ["example_function", "columns", "row_values"])
    table_name = type(first).__name__
    values = (get_attribute_values(cls, attrs) for cls in cls_array)
    return insert_into(
        column_names=attrs, table_name=table_name, values=map(str, values)
    )


def build_all_insert_statements(cls_arrays):
    insert_statements = []
    for cls_array in cls_arrays:
        if not cls_array:
            # no generated mock data for this attribute
            continue
        insert_statements.append(build_insert_statement(cls_array))
    return insert_statements


def write_insert_statement(statements: List[str]):
    with open("example.sql", "wt", encoding="utf-8") as f:
        for statement in statements:
            print(statement, file=f, end="\n\n")


if __name__ == "__main__":
    config = MockGeneratorConfig(prescription_count=3)
    conditions = read_conditions_from_file()
    mock = MockGenerator(conditions, config)
    pprint(mock.exams)
    pprint(mock.blood_exams)
    pprint(mock.covid_exams)
    pprint(mock.vaccine_administered)

    patient_1 = mock.patients[0]
    pprint(patient_1)
    pprint(patient_1.columns)
    # attrs = get_attributes(patient_1, ['example_function', 'columns', 'row_values'])
    tables_to_insert = get_attributes(mock, ["medical_conditions", "config"])
    pprint(tables_to_insert)
    table_values_to_insert = get_attribute_values(mock, tables_to_insert)
    pprint(table_values_to_insert)
    write_insert_statement(build_all_insert_statements(table_values_to_insert))
    # pprint(tables_to_insert)
    # pprint(attrs)
    # pprint(get_attribute_values(patient_1, attrs))
    # pprint(build_insert_statement(mock.patients))
