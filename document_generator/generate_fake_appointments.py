import json
from faker import Faker
import random

fake = Faker()

appointments = []

for i in range(50):
    appointment = {
        "_id": "appointment" + str(i).zfill(3),
        "patient_id": "patient" + str(random.randint(0, 49)).zfill(3),
        "provider_id": "provider" + str(random.randint(0, 49)).zfill(3),
        "date_scheduled": fake.date_between(start_date='today', end_date='+1y'),
        "date_of_visit": fake.date_between(start_date='today', end_date='+1y'),
        "telehealth_device": fake.random_element(elements=("Zoom", "Skype", "Google Meet", "Microsoft Teams")),
        "confirmed_phone": str(fake.random_number(digits=10)),
        "confirmed_email": fake.email(),
        "disposition": fake.random_element(elements=("completed", "rescheduled", "cancelled", "no-show")),
        "billing_disposition": fake.random_element(elements=("billed", "not billed"))
    }
    appointments.append(appointment)

with open('output/appointments.json', 'w') as f:
    json.dump(appointments, f, indent=4, default=str)