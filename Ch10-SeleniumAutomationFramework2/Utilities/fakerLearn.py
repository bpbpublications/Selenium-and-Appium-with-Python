from faker import Faker
import datetime

fake = Faker()

name = fake.name()
print(name)

address = fake.address()
print(address)


phone_number = fake.phone_number()
print(phone_number)

dateFake = fake.date_time()
print(dateFake)

start_date = datetime.datetime.strptime('01-01-2022', '%d-%m-%Y').date()
end_date = datetime.datetime.strptime('31-12-2023', '%d-%m-%Y').date()

fake_date = fake.date_between_dates(date_start=start_date, date_end=end_date)

print(fake_date)