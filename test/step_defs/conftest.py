import json
import pytest
import selenium
from pytest_bdd import given
from selenium import webdriver


# Fixtures
@pytest.fixture
def config():
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values
    assert config['browser'] in ['Chrome', 'Headless Chrome', 'Firefox', 'Headless Firefox']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config
    return config


@pytest.fixture
def browser(config):
    # Initiation of instance
    if config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    elif config['browser'] == 'Headless Firefox':
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument('--headless')
        b = selenium.webdriver.Firefox(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]} is not supported')
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()


# Shared Given Steps
@given('the Google.com home page is displayed(english)')
def google_home(browser, config):
    browser.get(config["GOOGLE_HOME"])
