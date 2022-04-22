"""Verifies the foregin key constraints of mock generated data."""
# pylint: disable=missing-function-docstring,missing-class-docstring

import unittest
from collections import Counter

from faker import Faker

from icd import MedicalCondition
from mock import MockGenerator, MockGeneratorConfig

mock_conditions = [MedicalCondition(f"{i}" * 3, f"A{i}") for i in range(5)] + [
    MedicalCondition(f"{i}" * 4, f"B{i}") for i in range(5)
]


class MockGeneratorTest(unittest.TestCase):
    def setUp(self):
        Faker.seed(0)

    def test_covered_by_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        provider_ids = set(
            provider.provider_id for provider in mock_gen.insurance_providers
        )
        patient_ids = set(patient.patient_id for patient in mock_gen.patients)
        for covered_by in mock_gen.insurance_covers:
            with self.subTest(covered_by=covered_by):
                self.assertIn(covered_by.patient_id, patient_ids)
                self.assertIn(covered_by.provider_id, provider_ids)

    def test_diagnoses_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        employees = set(employee.emp_id for employee in mock_gen.employees)
        patients = set(patient.patient_id for patient in mock_gen.patients)
        appointments = set(app.app_id for app in mock_gen.appointments)
        conditions = set(
            condition.icd_code for condition in mock_gen.medical_conditions
        )
        for diagnosis in mock_gen.diagnoses:
            with self.subTest(diag=diagnosis):
                self.assertIn(diagnosis.patient_id, patients)
                self.assertIn(diagnosis.emp_id, employees)
                self.assertIn(diagnosis.app_id, appointments)
                self.assertIn(diagnosis.icd_code, conditions)

    def test_lab_report_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        archived_files = set(f.file_id for f in mock_gen.archived_files)
        appointments = set(app.app_id for app in mock_gen.appointments)
        conditions = set(
            condition.icd_code for condition in mock_gen.medical_conditions
        )
        for report in mock_gen.lab_reports:
            with self.subTest(report=report):
                self.assertIn(report.app_id, appointments)
                self.assertIn(report.file_id, archived_files)
                self.assertIn(report.icd_code, conditions)

    def test_report_creator_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        reports = set(r.report_id for r in mock_gen.lab_reports)
        labs = set(lab.lab_id for lab in mock_gen.specialized_labs)
        for report_creator in mock_gen.report_creators:
            with self.subTest(report_creator=report_creator):
                self.assertIn(report_creator.report_id, reports)
                self.assertIn(report_creator.lab_id, labs)

    def test_appointment_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        patients = set(patient.patient_id for patient in mock_gen.patients)
        for app in mock_gen.appointments:
            with self.subTest(app=app):
                self.assertIn(app.patient_id, patients)

    def test_prescription_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        patients = set(patient.patient_id for patient in mock_gen.patients)
        employees = set(emp.emp_id for emp in mock_gen.employees)
        pharmacies = set(ph.pharmacy_address for ph in mock_gen.pharmacies)

        for prescription in mock_gen.prescriptions:
            with self.subTest(rx=prescription):
                self.assertIn(prescription.patient_id, patients)
                self.assertIn(prescription.emp_id, employees)
                self.assertIn(prescription.pharmacy_address, pharmacies)

    def test_app_medical_condition_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        appointments = set(appointment.app_id for appointment in mock_gen.appointments)
        conditions = set(
            condition.icd_code for condition in mock_gen.medical_conditions
        )

        for appointment_medical_condition in mock_gen.appointment_medical_conditions:
            with self.subTest(
                appointment_medical_conditions=appointment_medical_condition
            ):
                self.assertIn(appointment_medical_condition.app_id, appointments)
                self.assertIn(appointment_medical_condition.icd_code, conditions)

    def test_immunized_employee_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        immunizations = set(
            immunization.immunization_id for immunization in mock_gen.immunizations
        )
        employees = set(employee.emp_id for employee in mock_gen.employees)

        for immunized_employee in mock_gen.immunized_employees:
            with self.subTest(immunized_employee=immunized_employee):
                self.assertIn(immunized_employee.emp_id, employees)
                self.assertIn(immunized_employee.immun_id, immunizations)

    def test_immunized_patient_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        immunizations = set(
            immunization.immunization_id for immunization in mock_gen.immunizations
        )
        patients = set(patient.patient_id for patient in mock_gen.patients)
        for immunized_patient in mock_gen.immunized_patients:
            with self.subTest(immunized_patient=immunized_patient):
                self.assertIn(immunized_patient.patient_id, patients)
                self.assertIn(immunized_patient.immun_id, immunizations)

    def test_archived_file_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        employees = set(employee.emp_id for employee in mock_gen.employees)
        patients = set(patient.patient_id for patient in mock_gen.patients)
        for archived_file in mock_gen.archived_files:
            with self.subTest(archived_file=archived_file):
                self.assertIn(archived_file.patient_id, patients)
                self.assertIn(archived_file.emp_id, employees)


class MockGeneratorUniqueTest(unittest.TestCase):
    def setUp(self):
        Faker.seed(0)

    def test_medical_condition_uniqueness(self):
        mock_gen = MockGenerator(
            mock_conditions,
            MockGeneratorConfig(
                appointment_count=5, appointment_medical_conditions_count_max=250
            ),
        )
        mock_app_conditions = mock_gen.appointment_medical_conditions
        counter = Counter((mock.app_id, mock.icd_code) for mock in mock_app_conditions)
        for unique_pair, frequency in counter.items():
            with self.subTest(unique_pair=unique_pair, frequency=frequency):
                self.assertEqual(frequency, 1)

    def test_accepted_tests_uniqueness(self):
        mock_gen = MockGenerator(
            mock_conditions,
            MockGeneratorConfig(
                specialized_lab_count=5, test_count=5, accepted_test_count_max=50
            ),
        )
        mock_app_conditions = mock_gen.accepted_tests
        counter = Counter((mock.test_id, mock.lab_id) for mock in mock_app_conditions)
        for unique_pair, frequency in counter.items():
            with self.subTest(unique_pair=unique_pair, frequency=frequency):
                self.assertEqual(frequency, 1)


if __name__ == "__main__":
    unittest.main()
