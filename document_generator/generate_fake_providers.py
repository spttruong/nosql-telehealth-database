import json
from faker import Faker

fake = Faker()

providers = []

for i in range(50):
    provider = {
        "_id": "provider" + str(i).zfill(3),
        "npi": fake.random_number(digits=10),
        "name": fake.name(),
        "date_employed": fake.date_between(start_date='-10y', end_date='today'),
        "date_of_birth": fake.date_of_birth(minimum_age=25, maximum_age=65),
        "email": fake.email(),
        "primary_phone": str(fake.random_number(digits=10)),
        "credentialed_skills": [fake.random_element(elements=("Internal Medicine", "Cardiology", "Oncology", "Pediatrics"))],
        "appointments": ["appointment" + str(fake.random_int(min=1, max=50)).zfill(3) for j in range(fake.random_int(min=1, max=4))],
        "last_appointment": "appointment" + str(fake.random_int(min=1, max=50)).zfill(3)
    }
    providers.append(provider)

with open('output/providers.json', 'w') as f:
    json.dump(providers, f, indent=4, default=str)