import pytest
# import for Applitools Visual Verification
from applitools.selenium import Eyes
from test.automated_visual_verification.config.base import APPLITOOLS_API_KEY

# Applitools Visual Verification variables
APP_NAME='Google.com visual verification'


# Applitools Visual Verification Fixture
@pytest.fixture
def eyes():
    eyes = initialize_eyes()
    yield eyes

def initialize_eyes():
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY
    return eyes

def get_test_name():
    import inspect
    return inspect.stack()[3].function

def open_eyes(b, eyes):
    eyes.open(b, APP_NAME, test_name=get_test_name())

def close_eyes(eyes):
    eyes.close()

def validate_window(b, eyes, tag):
    open_eyes(b, eyes)
    eyes.check_window(tag=tag)
    eyes.close()