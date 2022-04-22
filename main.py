# pylint: disable=missing-module-docstring
from mock import MockGeneratorConfig, generate_mock_data_and_write_to_file

if __name__ == "__main__":
    config = MockGeneratorConfig(
        patient_count=30, employee_count=15, appointment_count=50, pharmacy_count=8
    )
    generate_mock_data_and_write_to_file(config)
