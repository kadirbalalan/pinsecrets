from PinSecrets import text_to_number, some_letters, new_password
import random
import pytest


def test_text_to_number():
    assert text_to_number("kadir") == 320781
def test_some_letters():
    random.seed(12345)
    assert some_letters("Test String") == "rTt"


@pytest.fixture
def set_seed():
    random.seed(42)

def test_new_password(set_seed):
    passw = "password"
    number = 123
    expected_output = ['password', '123', '!', '!', '-', '*']
    actual_output = new_password(passw, number)
    assert actual_output == expected_output


