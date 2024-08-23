from faker import Faker


def generate_random_data():
    fake = Faker()
    username = fake.user_name()
    password = fake.password()

    return username, password
