import pytest
from utilities.env_reader import read_env_variable
from utilities.general_utils import generate_random_email

SIGN_UP_FIRST_NAME = "James"
SIGN_UP_LAST_NAME = "BOND"


@pytest.fixture(scope="module")
def item_specs():
    specs = {
        "size": "M",
        "color": "Blue",
        "qty": 2
    }
    return specs