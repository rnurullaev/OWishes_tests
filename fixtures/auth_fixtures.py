import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "name": fake.first_name(),
        "password": "Password123!",
    }
