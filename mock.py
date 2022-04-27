# pylint: skip-file
import random
import re
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from string import ascii_uppercase
from typing import List, Optional, Union

from faker import Faker

from auto_increment import AutoIncrement
from constants import (
    BLOOD_TYPES,
    DRUG_UNITS,
    EMPLOYEE_ROLES,
    GENDER_OPTION_CHANCE,
    IMMUNIZATION_TYPES,
    INSURANCE_COMPANY_NAMES,
    MEDICAL_SPECIALIZATIONS,
    PRESCRIPTION_DRUG_NAMES,
    RELATIVE_TYPES,
)
from data_dependency_graph import build_reverse_topological_sort, build_topological_sort
from icd import (
    build_condition_insert_statement,
    MedicalCondition,
    read_combined_conditions,
)
from writer import insert_into

fake = Faker()
Faker.seed(0)
random.seed(0)
auto_id = AutoIncrement()


def random_name() -> str:
    # TODO: Potentially add custom name building, to prevent prefixes and suffixes
    #  from happening,
    return fake.name()


def random_ssn() -> str:
    return fake.unique.ssn()


def random_address() -> str:
    # return fake.address().replace('\n', ' ')
    return fake.address()


def random_nurse_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="RN####")


def random_dea_number() -> str:
    """https://en.wikipedia.org/wiki/DEA_number"""
    return (
        f"{fake.bothify('?', letters='BM')}"
        f"{fake.unique.bothify(text='?#######', letters=ascii_uppercase)}"
    )


def random_physician_assistant_license() -> str:
    """https://madph.mylicense.com/eGov/custom/LN%20Formats.htm"""
    return fake.unique.bothify(text="PA####")


def random_physician_license() -> str:
    return fake.unique.bothify(text="GP####")


def random_phone(chance: Optional[int] = 100) -> Optional[str]:
    if fake.boolean(chance_of_getting_true=chance):
        return fake.unique.phone_number()
    return None


def random_file() -> str:
    return fake.file_name()


def random_email() -> str:
    return fake.email()


def format_date_no_time(date_time: datetime) -> str:
    return str(date_time).split()[0]


def format_date_with_time(date_time: datetime) -> str:
    return str(date_time).split(".")[0]


def date_time_between(
    start_date=timedelta(days=-30), end_date=None, simple=True
) -> str:
    if end_date is None:
        end_date = datetime.now()

    date_time = fake.date_time_between(start_date=start_date, end_date=end_date)
    if simple:
        return format_date_no_time(date_time)
    return format_date_with_time(date_time)


def random_company_name():
    return fake.company()


def random_insurance_name():
    return fake.random_element(elements=INSURANCE_COMPANY_NAMES)


def random_s3_id():
    return fake.unique.uuid4()


def random_gender() -> str:
    return fake.random_element(elements=GENDER_OPTION_CHANCE)


def random_role() -> str:
    return fake.random_element(elements=EMPLOYEE_ROLES)


def business_slogan() -> str:
    return fake.bs()


def random_immunization() -> str:
    return fake.random_element(elements=IMMUNIZATION_TYPES)


def random_specialization() -> str:
    return fake.random_element(elements=MEDICAL_SPECIALIZATIONS)


def random_relative_type():
    return fake.random_element(elements=RELATIVE_TYPES)


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
    return fake.random_element(elements=BLOOD_TYPES)


def random_blood_sugar():
    return f"{round(fake.random.uniform(70.0, 120.0), 2)} mg/dL"


def random_member_id() -> str:
    return fake.unique.bothify("???#########", letters=ascii_uppercase)


def random_group_number() -> str:
    return fake.bothify("######")


def random_policy_number() -> str:
    return fake.bothify("#####")


def random_in_network() -> str:
    return fake.boolean(chance_of_getting_true=80)


def random_drug_dose() -> str:
    return f"{fake.random.randint(2, 500)} {fake.random_element(elements=DRUG_UNITS)}"


def random_drug_name() -> str:
    return fake.random_element(elements=PRESCRIPTION_DRUG_NAMES)


def generate_random_appointment_date() -> str:
    start_dates = OrderedDict(
        [
            (timedelta(weeks=(-52)), 0.2),
            (timedelta(weeks=(-12)), 0.3),
            (timedelta(days=(-3)), 0.5),
        ]
    )
    return date_time_between(
        start_date=fake.random_element(elements=start_dates),
        simple=False,
    )


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
    birthday: str = field(
        default_factory=lambda: date_time_between(
            start_date=timedelta(weeks=(-60 * 12)), end_date=timedelta(weeks=(-1 * 12))
        ),
        repr=False,
    )
    email: str = field(default_factory=random_email, repr=False)
    ssn: str = field(default_factory=random_ssn, repr=False)
    address: str = field(default_factory=random_address, repr=False)
    name: str = field(default_factory=random_name, repr=False)
    gender: str = field(default_factory=random_gender, repr=False)
    table_name: str = field(default="patients", init=False)


@dataclass
class EmergencyContact:
    patient_id: int
    name: str = field(default_factory=random_name)
    phone_1: str = field(default_factory=random_phone)
    phone_2: str = field(default_factory=lambda: random_phone(40))
    table_name: str = field(default="emergency_contacts", init=False)

    @property
    def primary_key(self):
        return (self.patient_id, self.name)


def generate_emergency_contact(patient: Patient) -> EmergencyContact:
    return EmergencyContact(patient_id=patient.patient_id)


@dataclass
class Employee:
    emp_id: int = field(default_factory=lambda: auto_id.next_id("Employee"))
    phone_number: str = field(default_factory=random_phone, repr=False)
    birthday: str = field(
        default_factory=lambda: date_time_between(
            start_date=timedelta(weeks=(-60 * 12)), end_date=timedelta(weeks=(-20 * 12))
        ),
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
    table_name: str = field(default="employees", init=False)

    def __post_init__(self):
        """This logic assigns the salary and medical license based on the randomly
        assigned role attribute"""
        if self.role in ["Receptionist", "Orderly"]:
            # multiply by 100 to store salary as integer instead of float by storing
            # in base unit (cents)
            self.salary = fake.random.randint(15_000 * 100, 80_000 * 100)
        elif self.role == "Nurse":
            self.salary = fake.random.randint(54_000 * 100, 100_000 * 100)
            self.medical_license_number = random_nurse_license()
            self.dea_number = random_dea_number()
        elif self.role == "Physician Assistant":
            self.salary = fake.random.randint(94_000 * 100, 130_000 * 100)
            self.medical_license_number = random_physician_assistant_license()
            self.dea_number = random_dea_number()
        elif self.role == "Physician General Practitioner":
            self.salary = fake.random.randint(160_000 * 100, 260_000 * 100)
            self.medical_license_number = random_physician_license()
            self.dea_number = random_dea_number()
        else:
            raise ValueError(f"{self.role} does not fit into the possible roles.")


@dataclass
class InsuranceProvider:
    provider_id: int = field(
        default_factory=lambda: auto_id.next_id("InsuranceProvider")
    )
    insurance_name: str = field(default_factory=random_insurance_name)
    policy_number: str = field(default_factory=random_policy_number)
    in_network: bool = field(default_factory=random_in_network)
    table_name: str = field(default="insurance_providers", init=False)


@dataclass
class ArchivedFile:
    patient_id: int
    emp_id: int
    file_id: int = field(default_factory=lambda: auto_id.next_id("ArchivedFile"))
    file_name: str = field(default_factory=random_file)
    s3_id: str = field(default_factory=random_s3_id)
    table_name: str = field(default="archived_files", init=False)


def generate_archived_file(patient: Patient, employee: Employee) -> ArchivedFile:
    return ArchivedFile(patient_id=patient.patient_id, emp_id=employee.emp_id)


@dataclass
class SpecializedLab:
    lab_id: int = field(default_factory=lambda: auto_id.next_id("SpecializedLab"))
    phone_number: str = field(default_factory=random_phone)
    address: str = field(default_factory=random_address)
    table_name: str = field(default="specialized_labs", init=False)


@dataclass
class Test:
    test_id: int = field(default_factory=lambda: auto_id.next_id("Test"))
    test_name: str = field(default_factory=business_slogan)
    table_name: str = field(default="tests", init=False)


@dataclass
class AcceptedTest:
    test_id: int
    lab_id: int
    table_name: str = field(default="accepted_tests", init=False)

    @property
    def primary_key(self):
        return (self.test_id, self.lab_id)


def generate_test_accepted(lab: SpecializedLab, test: Test) -> AcceptedTest:
    return AcceptedTest(test_id=test.test_id, lab_id=lab.lab_id)


@dataclass
class Pharmacy:
    pharmacy_address: str = field(default_factory=random_address)
    pharmacy_name: str = field(default_factory=random_company_name)
    table_name: str = field(default="pharmacies", init=False)


@dataclass
class Immunization:
    immunization_id: int = field(
        default_factory=lambda: auto_id.next_id("Immunization")
    )
    immunization_type: str = field(default_factory=random_immunization)
    table_name: str = field(default="immunizations", init=False)


@dataclass
class ImmunizedEmployee:
    immun_id: int
    emp_id: int
    table_name: str = field(default="immunized_employees", init=False)

    @property
    def primary_key(self):
        return (self.immun_id, self.emp_id)


def generate_immunized_employees(
    immunization: Immunization, employee: Employee
) -> ImmunizedEmployee:
    return ImmunizedEmployee(
        immun_id=immunization.immunization_id, emp_id=employee.emp_id
    )


@dataclass
class ImmunizedPatient:
    immun_id: int
    patient_id: int
    table_name: str = field(default="immunized_patients", init=False)

    @property
    def primary_key(self):
        return (self.immun_id, self.patient_id)


def generate_immunized_patients(
    immunization: Immunization, patient: Patient
) -> ImmunizedPatient:
    return ImmunizedPatient(
        immun_id=immunization.immunization_id, patient_id=patient.patient_id
    )


@dataclass
class ReferrableDoctor:
    ref_doctor_id: int = field(
        default_factory=lambda: auto_id.next_id("ReferrableDoctor")
    )
    name: str = field(default_factory=random_name)
    specialization: str = field(default_factory=random_specialization)
    phone_number: str = field(default_factory=random_phone)
    table_name: str = field(default="referrable_doctors", init=False)


@dataclass
class Referral:
    emp_id: int
    ref_doctor_id: int
    patient_id: int
    ref_id: int = field(default_factory=lambda: auto_id.next_id("Referral"))
    table_name: str = field(default="referrals", init=False)


def generate_referrel(
    employee: Employee, referrable: ReferrableDoctor, patient: Patient
) -> Referral:
    return Referral(
        emp_id=employee.emp_id,
        ref_doctor_id=referrable.ref_doctor_id,
        patient_id=patient.patient_id,
    )


@dataclass
class InsuranceCover:
    provider_id: int
    patient_id: int
    member_id: str = field(default_factory=random_member_id)
    group_number: str = field(default_factory=random_group_number)
    policy_holder_name: str = field(default_factory=random_name)
    table_name: str = field(default="insurance_covers", init=False)

    @property
    def primary_key(self):
        return (self.provider_id, self.patient_id)


def generate_insurance_covers(
    patient: Patient, insurance_provider: InsuranceProvider
) -> InsuranceCover:
    policy_holder_name = (
        patient.name if fake.boolean(chance_of_getting_true=95) else random_name()
    )
    return InsuranceCover(
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
    table_name: str = field(default="relatives", init=False)


def generate_relative(patient: Patient) -> InsuranceCover:
    return Relative(patient_id=patient.patient_id)


@dataclass
class RelativeCondition:
    relative_id: int
    icd_code: str
    table_name: str = field(default="relative_conditions", init=False)

    @property
    def primary_key(self):
        return (self.relative_id, self.icd_code)


def generate_relative_condition(
    relative: Relative, condition: MedicalCondition
) -> InsuranceCover:
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
    drug_name: str = field(default_factory=random_drug_name, repr=False)
    quantity: int = field(default_factory=lambda: fake.random.randint(1, 180))
    dose: str = field(default_factory=random_drug_dose)
    refills: int = field(default_factory=lambda: fake.random.randint(0, 7))
    instructions: Optional[str] = field(
        default_factory=lambda: random_notes(90, 5), repr=False
    )
    prescription_date: str = field(
        default_factory=lambda: date_time_between(
            timedelta(weeks=(-60 * 12)), simple=False
        )
    )
    table_name: str = field(default="prescriptions", init=False)


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
    date: str = field(default_factory=generate_random_appointment_date)
    table_name: str = field(default="appointments", init=False)


def generate_appointment(patient: Patient) -> Appointment:
    return Appointment(patient_id=patient.patient_id)


@dataclass
class LabReport:
    icd_code: str
    file_id: int
    app_id: int
    exam_id: int
    report_id: int = field(default_factory=lambda: auto_id.next_id("LabReport"))
    # info: Optional[str] = field(default_factory=lambda: random_notes(80, 2))
    result_info: Optional[str] = field(default_factory=lambda: random_notes(80, 3))
    table_name: str = field(default="lab_reports", init=False)


def generate_lab_report(
    medical_condition: MedicalCondition,
    appointment: Appointment,
    exam: Union["BloodExam", "CovidExam", "AdministeredVaccine", None] = None,
    file: ArchivedFile = None,
) -> LabReport:
    return LabReport(
        icd_code=medical_condition.icd_code,
        file_id=file.file_id if file else None,
        exam_id=exam.exam_id if exam else None,
        app_id=appointment.app_id,
    )


@dataclass
class AppointmentMedicalCondition:
    app_id: int
    icd_code: str
    comment: Optional[str] = field(default_factory=lambda: random_notes(40, 2))
    table_name: str = field(default="appointment_medical_conditions", init=False)

    @property
    def primary_key(self):
        return (self.app_id, self.icd_code)


def generate_appointment_medical_conditions(
    appointment: Appointment, medical_condition: MedicalCondition
) -> AppointmentMedicalCondition:
    return AppointmentMedicalCondition(
        app_id=appointment.app_id, icd_code=medical_condition.icd_code
    )


@dataclass
class AppointmentEmployee:
    emp_id: int
    app_id: int
    table_name: str = field(default="appointment_employees", init=False)

    @property
    def primary_key(self):
        return (self.emp_id, self.app_id)


def generate_appointment_employees(
    employee: Employee, appointment: Appointment
) -> AppointmentEmployee:
    return AppointmentEmployee(emp_id=employee.emp_id, app_id=appointment.app_id)


@dataclass
class Diagnosis:
    emp_id: int
    patient_id: int
    app_id: int
    icd_code: str
    comment: Optional[str] = field(default_factory=lambda: random_notes(90, 3))
    table_name: str = field(default="diagnoses", init=False)

    @property
    def primary_key(self):
        return (self.emp_id, self.patient_id, self.app_id, self.icd_code)


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
class ReportCreator:
    report_id: int
    lab_id: int
    table_name: str = field(default="report_creators", init=False)

    @property
    def primary_key(self):
        return (self.report_id, self.lab_id)


def generate_report_creator(
    report: LabReport, specialized_lab: SpecializedLab
) -> ReportCreator:
    return ReportCreator(report_id=report.report_id, lab_id=specialized_lab.lab_id)


@dataclass
class Exam:
    app_id: int
    exam_id: int = field(default_factory=lambda: auto_id.next_id("Exam"))
    comment: Optional[str] = field(default_factory=lambda: random_notes(60, 2))
    table_name: str = field(default="exams", init=False)


def generate_exam(appointment: Appointment) -> Exam:
    return Exam(app_id=appointment.app_id)


@dataclass
class ExamInterface:
    exam_id: int


@dataclass
class CovidExam(ExamInterface):
    test_type: str = field(default_factory=random_covid_exam)
    is_positive: bool = field(
        default_factory=lambda: fake.boolean(chance_of_getting_true=10)
    )
    table_name: str = field(default="covid_exams", init=False)


@dataclass
class BloodExam(ExamInterface):
    blood_type: str = field(default_factory=random_blood_type)
    blood_sugar: str = field(default_factory=random_blood_sugar)
    table_name: str = field(default="blood_exams", init=False)


@dataclass
class AdministeredVaccine(ExamInterface):
    vaccine_type: str = field(default_factory=random_immunization)
    table_name: str = field(default="administered_vaccines", init=False)


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
    insurance_cover_count: int = field(default=5)
    relative_count: int = field(default=5)
    prescription_count: int = field(default=5)
    immunized_patient_count: int = field(default=5)
    immunized_employee_count: int = field(default=5)
    referral_count: int = field(default=5)
    appointment_count: int = field(default=5)

    # M-N relationships, partial participation
    lab_report_count: int = field(default=5)
    exam_count: int = field(default=5)
    archived_file_count: int = field(default=5)

    # M-N relationships, total participation
    appointment_employee_count_max: int = field(default=3)
    accepted_test_count_max: int = field(default=3)
    diagnosis_count_max: int = field(default=2)
    appointment_medical_conditions_count_max: int = field(default=2)
    relative_condition_max: int = field(default=2)
    emergency_contact_max: int = field(default=3)


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
    insurance_covers: List[InsuranceCover] = field(init=False, default_factory=list)
    relatives: List[Relative] = field(init=False, default_factory=list)
    prescriptions: List[Prescription] = field(init=False, default_factory=list)
    immunized_patients: List[ImmunizedPatient] = field(init=False, default_factory=list)
    immunized_employees: List[ImmunizedEmployee] = field(
        init=False, default_factory=list
    )
    referrals: List[Referral] = field(init=False, default_factory=list)
    report_creators: List[ReportCreator] = field(init=False, default_factory=list)
    blood_exams: List[BloodExam] = field(init=False, default_factory=list)
    covid_exams: List[CovidExam] = field(init=False, default_factory=list)
    administered_vaccines: List[AdministeredVaccine] = field(
        init=False, default_factory=list
    )

    # M-N relationships, partial participation
    lab_reports: List[LabReport] = field(init=False, default_factory=list)
    exams: List[Exam] = field(init=False, default_factory=list)
    archived_files: List[ArchivedFile] = field(init=False, default_factory=list)

    # M-N relationships, total participation
    appointment_employees: List[AppointmentEmployee] = field(
        init=False, default_factory=list
    )
    accepted_tests: List[AcceptedTest] = field(init=False, default_factory=list)
    diagnoses: List[Diagnosis] = field(init=False, default_factory=list)
    appointment_medical_conditions: List[AppointmentMedicalCondition] = field(
        init=False, default_factory=list
    )
    relative_conditions: List[RelativeCondition] = field(
        init=False, default_factory=list
    )
    emergency_contacts: List[EmergencyContact] = field(init=False, default_factory=list)

    def __post_init__(self):
        self._generate_independent_schema()
        self._generate_appointments(self.config.appointment_count)
        self._generate_insurance_covers()
        self._generate_relatives()
        self._generate_prescriptions()
        self._generate_immunizations()
        self._generate_referrals()
        self._generate_archived_files()
        self._generate_medical_staff()
        self._generate_accepted_tests()
        self._generate_medical_conditions()
        self._generate_relative_conditions()
        self._generate_emergency_contacts()
        self._generate_diagnosis()
        self._generate_report_creators()
        self._generate_exams()
        self._generate_exam_subclasses()
        self._generate_lab_reports()

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

    def _generate_insurance_covers(self):
        # TODO: Ensure there are no duplicates in this table, can possibly make
        #  covered by frozen, and use set
        quantity = self.config.insurance_cover_count
        self.insurance_covers = [
            generate_insurance_covers(patient, provider)
            for patient, provider in self._random_selector(
                self.patients, self.insurance_providers, quantity=quantity
            )
        ]
        self.insurance_covers = self._get_uniques(self.insurance_covers)

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

    def _get_uniques(self, array):
        if array:
            assert hasattr(array[0], "primary_key")
        seen = set()
        uniques = []
        for cls in array:
            primary_key = cls.primary_key
            if primary_key not in seen:
                seen.add(primary_key)
                uniques.append(cls)
        return uniques

    def _generate_immunizations(self):
        self.immunized_patients = [
            generate_immunized_patients(immunization, patient)
            for immunization, patient in self._random_selector(
                self.immunizations,
                self.patients,
                quantity=self.config.immunized_patient_count,
            )
        ]
        self.immunized_patients = self._get_uniques(self.immunized_patients)
        self.immunized_employees = [
            generate_immunized_employees(immunization, employee)
            for immunization, employee in self._random_selector(
                self.immunizations,
                self.employees,
                quantity=self.config.immunized_patient_count,
            )
        ]
        self.immunized_employees = self._get_uniques(self.immunized_employees)

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
            random_length = fake.random.randint(
                1, self.config.appointment_employee_count_max
            )
            for employee in fake.random_elements(
                elements=self.employees, unique=True, length=random_length
            ):
                medical_staff.append(generate_appointment_employees(employee, app))
        self.appointment_employees = self._get_uniques(medical_staff)

    def _generate_emergency_contacts(self):
        """Every appointment must have at least 1 medical staff"""
        emergency_contacts = []
        for patient in self.patients:
            random_length = fake.random.randint(0, self.config.emergency_contact_max)
            for _ in range(random_length):
                emergency_contacts.append(generate_emergency_contact(patient))
        self.emergency_contacts = self._get_uniques(emergency_contacts)

    def _generate_accepted_tests(self):
        """Every appointment must have at least 1 medical staff"""
        tests_accepted = []
        for lab in self.specialized_labs:
            random_length = fake.random.randint(1, self.config.accepted_test_count_max)
            for test in fake.random_elements(
                elements=self.tests, unique=True, length=random_length
            ):
                tests_accepted.append(generate_test_accepted(lab, test))
        self.accepted_tests = self._get_uniques(tests_accepted)

    def _generate_medical_conditions(self):
        conditions = []
        medical_condition_codes = [
            condition for condition in self.medical_conditions if condition.is_code
        ]
        # print(f"{len(medical_condition_codes)=}")
        for app in self.appointments:
            random_length = fake.random.randint(
                0, self.config.appointment_medical_conditions_count_max
            )
            for condition in fake.random_elements(
                elements=medical_condition_codes, unique=True, length=random_length
            ):
                conditions.append(
                    generate_appointment_medical_conditions(app, condition)
                )
        self.appointment_medical_conditions = self._get_uniques(conditions)

    def _generate_relative_conditions(self):
        relative_conditions = []
        medical_condition_codes = [
            condition for condition in self.medical_conditions if condition.is_code
        ]
        for relative in self.relatives:
            random_length = fake.random.randint(1, self.config.relative_condition_max)
            for condition in fake.random_elements(
                elements=medical_condition_codes, unique=True, length=random_length
            ):
                relative_conditions.append(
                    generate_relative_condition(relative, condition)
                )
        self.relative_conditions = self._get_uniques(relative_conditions)

    def _generate_diagnosis(self):
        diagnosis = []
        medical_condition_codes = [
            condition for condition in self.medical_conditions if condition.is_code
        ]
        for app in self.appointments:
            random_length = fake.random.randint(0, self.config.diagnosis_count_max)
            random_employee = fake.random_element(elements=self.employees)
            for condition in fake.random_elements(
                elements=medical_condition_codes, unique=True, length=random_length
            ):
                diagnosis.append(
                    generate_diagnosis(
                        random_employee, app, Patient(app.patient_id), condition
                    )
                )
        self.diagnoses = self._get_uniques(diagnosis)

    def _generate_lab_reports(self):
        medical_condition_codes = [
            condition for condition in self.medical_conditions if condition.is_code
        ]
        combined_exams = (
            self.blood_exams + self.covid_exams + self.administered_vaccines
        )
        self.lab_reports = [
            generate_lab_report(con, app, file=f, exam=exam)
            for con, app, f, exam in self._random_selector(
                medical_condition_codes,
                self.appointments,
                self.archived_files,
                combined_exams,
                quantity=self.config.lab_report_count,
            )
        ]

    def _generate_report_creators(self):
        self.report_creators = [
            generate_report_creator(report, lab)
            for report, lab in zip(
                self.lab_reports,
                fake.random_elements(
                    elements=self.specialized_labs, length=len(self.lab_reports)
                ),
            )
        ]
        self.report_creators = self._get_uniques(self.report_creators)

    def _generate_exams(self):
        self.exams = [
            generate_exam(app)
            for app in fake.random_elements(
                elements=self.appointments, length=self.config.exam_count
            )
        ]

    def _generate_exam_subclasses(self):
        arrays = [self.blood_exams, self.covid_exams, self.administered_vaccines]
        exam_types: List[ExamInterface] = [BloodExam, CovidExam, AdministeredVaccine]
        for exam in self.exams:
            random_selection_idx = fake.random.randint(0, len(exam_types) - 1)
            arrays[random_selection_idx].append(
                exam_types[random_selection_idx](exam.exam_id)
            )


def build_insert_statement(cls_array):
    first = cls_array[0]
    attrs = get_attributes(first, ["format_date", "table_name", "primary_key"])
    table_name = first.table_name
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
            print(statement, file=f, end="\n")


# matches strings which contain a date that has specified time
# example: matches: '2010-11-12 04:26:21' but not '2010-11-12'.
timestamp_re = re.compile(r"'[1-2][\d]{3}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}'")


def add_timestamp_keyword(statement: str) -> str:
    def add_timestamp(matchobj: re.Match) -> str:
        return f"TIMESTAMP {matchobj.group(0)}"

    return timestamp_re.sub(add_timestamp, statement)


def convert_to_postgres(insert_statements: List[str]) -> List[str]:
    res = []
    for statement in insert_statements:
        res.append(add_timestamp_keyword(statement.replace("None", "DEFAULT")))
    return res


def build_auto_increment_statements(mock: MockGenerator) -> List[str]:
    """
    These statements are necessary to set the autoincrement generator to begin
    at the correct place after mock data is inserted.
    """
    auto_increment_tables = [
        (mock.patients, "patient_id"),
        (mock.insurance_providers, "provider_id"),
        (mock.employees, "emp_id"),
        (mock.prescriptions, "prescription_id"),
        (mock.relatives, "relative_id"),
        (mock.referrals, "ref_id"),
        (mock.immunizations, "immunization_id"),
        (mock.appointments, "app_id"),
        (mock.tests, "test_id"),
        (mock.archived_files, "file_id"),
        (mock.lab_reports, "report_id"),
        (mock.exams, "exam_id"),
        (mock.specialized_labs, "lab_id"),
        (mock.referrable_doctors, "ref_doctor_id"),
    ]
    statements = ["/* UPDATE AUTOINCREMENT START VALUES BASED ON MOCK DATA INSERTS */"]
    for table, table_id_name in auto_increment_tables:
        if table:
            assert hasattr(table[0], table_id_name)
            table_size = len(table)
            table_name = table[0].table_name
            table_sequence_name = f"{table_name}_{table_id_name}_seq"
            statements.append(f"select setval('{table_sequence_name}', {table_size});")
    return statements


def build_intro_delete_statements(mock: MockGenerator):
    table_names = [
        attr[0].table_name
        for attr in get_attribute_values(mock, get_attributes(mock, ["config"]))
        if attr
    ]
    return [f"DELETE FROM {table_name};" for table_name in table_names]


def dependency_sort(tables: List[str]) -> List[str]:
    order = {table_name: idx for idx, table_name in enumerate(build_topological_sort())}
    return list(sorted(tables, key=lambda table_name: order.get(table_name, -1)))


def reverse_dependency_sort(tables: List[str]) -> List[str]:
    order = {
        table_name: idx
        for idx, table_name in enumerate(build_reverse_topological_sort())
    }
    return list(sorted(tables, key=lambda table_name: order.get(table_name, -1)))


def build_truncate_statement(mock: MockGenerator):
    tables_to_insert = reverse_dependency_sort(get_attributes(mock, ["config"]))
    return f"TRUNCATE {', '.join(table_name for table_name in tables_to_insert)};\n"


def build_drop_table_statement():
    config = MockGeneratorConfig(prescription_count=3)
    conditions = read_combined_conditions()
    mock = MockGenerator(conditions, config)
    tables_to_insert = reverse_dependency_sort(get_attributes(mock, ["config"]))
    statements = [
        f"TRUNCATE {', '.join(table_name for table_name in tables_to_insert)};\n"
    ]
    statements.extend(
        f"DROP TABLE {', '.join(table_name for table_name in tables_to_insert)};\n"
    )
    return "".join(statements)


def print_table_sizes(tables_values_to_insert):
    tables = {
        table[0].table_name: len(table) for table in tables_values_to_insert if table
    }
    for table_name, count in sorted(
        tables.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"{table_name:<22} size: {count}")
    print(f"Total Rows: {sum(tables.values())}")


def generate_mock_data_and_write_to_file(config: Optional[MockGeneratorConfig] = None):
    if config is None:
        config = MockGeneratorConfig(prescription_count=3)
    conditions = read_combined_conditions()
    mock = MockGenerator(conditions, config)
    tables_to_insert = get_attributes(mock, ["medical_conditions", "config"])
    ordered_tables_to_insert = dependency_sort(tables_to_insert)
    table_values_to_insert = get_attribute_values(mock, ordered_tables_to_insert)
    print_table_sizes(table_values_to_insert)
    insert_statements = ["BEGIN;", build_truncate_statement(mock)]
    insert_statements.append(build_condition_insert_statement(conditions))
    insert_statements.extend(build_all_insert_statements(table_values_to_insert))
    insert_statements.extend(build_auto_increment_statements(mock))
    insert_statements.append("COMMIT;")
    postgres_statements = convert_to_postgres(insert_statements)
    write_insert_statement(postgres_statements)


if __name__ == "__main__":
    # print(build_drop_table_statement())
    generate_mock_data_and_write_to_file(
        MockGeneratorConfig(
            appointment_count=1750,
            appointment_medical_conditions_count_max=2,
            archived_file_count=30,
            diagnosis_count_max=1,
            employee_count=200,
            insurance_cover_count=50,
            prescription_count=1500,
            insurance_provider_count=15,
            test_count=40,
            lab_report_count=60,
            exam_count=60,
            specialized_lab_count=10,
            patient_count=400,
            referrable_doctor_count=10,
            referral_count=15,
            relative_count=20,
            immunization_count=10,
            immunized_employee_count=20,
            immunized_patient_count=80,
            appointment_employee_count_max=2,
            relative_condition_max=1,
            emergency_contact_max=1,
        )
    )
