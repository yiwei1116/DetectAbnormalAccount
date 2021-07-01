from faker import Faker
import uuid
import random
import time
from enum import Enum
fake = Faker()


class EventType(Enum):
    CLICK = 'Click'
    PURCHASE = 'Purchase'
    LOGIN = 'Login'
    LOGOUT = 'Logout'
    DELETE_ACCOUNT = 'Delete account'
    CREATE_ACCOUNT = 'Create account'
    UPDATE_SETTING = 'Update setting'
    OTHER = 'Other'


class Country(Enum):
    USA = 'Usa'
    IN = 'India'
    CN = 'China'
    UK = 'United Kingdom'
    CA = 'Canada'
    JP = 'Japen'
    FR = 'France'
    OTHER = 'Other'


def get_server_log():
    return {
        "ID": str(uuid.uuid4()),
        "AccountID": random.randrange(1000),
        "EventType": str(random.choice(list(EventType))),
        "Country": str(random.choice(list(Country))),
        "TimeStamp":  time.mktime(time.gmtime())
        # "name": fake.name(),
        # "address": fake.address(),
        # "created_at": fake.year()
    }


if __name__ == '__main__':
    print(get_server_log())


# userAcc = UserAccountInformation(
#     uuid.uuid4(),
#     random.randrange(1000),
#     random.choice(list(EventType)),
#     random.choice(list(Country)),
#     time.mktime(time.gmtime()))
