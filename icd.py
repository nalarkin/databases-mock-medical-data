from dataclasses import dataclass


@dataclass
class MedicalCondition:
    category_code: str
    icd_code: str
    name: str


@dataclass
class MedicalConditionCategory:
    category_code: str
    category_name: str
