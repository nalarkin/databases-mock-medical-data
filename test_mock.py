from typing import List
import unittest
from faker import Faker
from icd import MedicalCondition
from insurance import InsuranceProvider
from mock import MockGeneratorConfig, MockGenerator

mock_conditions = [MedicalCondition(f"{i}", f"A{i}", f"Test{i}") for i in range(5)]


class MockGeneratorTest(unittest.TestCase):
    def setUp(self):
        Faker.seed(0)

    def test_covered_by_relationships(self):
        mock_gen = MockGenerator(mock_conditions, MockGeneratorConfig())
        provider_ids = set(
            provider.provider_id for provider in mock_gen.insurance_providers
        )
        patient_ids = set(patient.patient_id for patient in mock_gen.patients)
        for covered_by in mock_gen.covered_bys:
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

        for diag in mock_gen.diagnosis:
            with self.subTest(diag=diag):
                self.assertIn(diag.patient_id, patients)
                self.assertIn(diag.emp_id, employees)
                self.assertIn(diag.app_id, appointments)
                self.assertIn(diag.icd_code, conditions)


if __name__ == "__main__":
    unittest.main()
