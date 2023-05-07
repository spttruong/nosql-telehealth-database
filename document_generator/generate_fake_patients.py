import json
from faker import Faker

fake = Faker()

patients = []

for i in range(50):
    patient = {
        "_id": "patient" + str(i).zfill(3),
        "patient_chart": {
            "height_in": fake.random_int(min=50, max=80),
            "weight": fake.random_int(min=100, max=300),
            "blood_pressure": str(fake.random_int(min=90, max=140)) + "/" + str(fake.random_int(min=50, max=90)),
            "blood_sugar": fake.random_int(min=70, max=150),
            "icd_10_codes": [fake.random_element(elements=("E11.9", "F41.1", "I10", "E78.5"))],
            "notes": fake.sentence(nb_words=6),
            "last_appointment_id": "appointment" + str(fake.random_int(min=1, max=50)).zfill(3)
        },
        "name": fake.name(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "address": fake.address(),
        "primary_phone": str(fake.random_number(digits=10)),
        "email": fake.email(),
        "medical_group": fake.company(),
        "insurance_id": fake.random_number(digits=12),
        "insurance_payer_id": fake.random_number(digits=12),
        "languages": [fake.random_element(elements=("English", "Spanish", "French"))],
        "appointments": ["appointment" + str(fake.random_int(min=1, max=50)).zfill(3) for j in range(fake.random_int(min=1, max=4))]
    }
    patients.append(patient)

with open('output/patients.json', 'w') as f:
    json.dump(patients, f, indent=4, default=str)