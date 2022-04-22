"""Provides domain-specific options that are randomly selected from during data generation."""
from collections import OrderedDict

PRESCRIPTION_DRUG_NAMES = [
    "Atorvastatin",
    "Levothyroxine",
    "Lisinopril",
    "Metformin",
    "Metoprolol",
    "Amlodipine",
    "Albuterol",
    "Omeprazole",
    "Losartan",
    "Gabapentin",
    "Hydrochlorothiazide",
    "Sertraline",
    "Simvastatin",
    "Montelukast",
    "Hydrocodone",
    "Pantoprazole",
    "Furosemide",
    "Fluticasone",
    "Escitalopram",
    "Fluoxetine",
    "Rosuvastatin",
]

INSURANCE_COMPANY_NAMES = [
    "Health World",
    "Purple Shield",
    "Liberty Truth Medical",
    "World Market",
    "HealthMark",
    "Highland Sons Mutual",
]


MEDICAL_SPECIALIZATIONS = [
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

EMPLOYEE_ROLES = [
    "Physician General Practitioner",
    "Nurse",
    "Orderly",
    "Receptionist",
    "Physician Assistant",
]

RELATIVE_TYPES = [
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

GENDER_OPTION_CHANCE = OrderedDict(
    [
        ("Male", 0.4),
        ("Female", 0.4),
        ("Genderfluid", 0.06666666666666667),
        ("Nonbinary", 0.06666666666666667),
        ("Transgender", 0.06666666666666667),
    ]
)

BLOOD_TYPES = ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"]

DRUG_UNITS = ["mg", "mcg", "g", "mg/mL"]
