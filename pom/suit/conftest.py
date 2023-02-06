import pytest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from os import path

CUR_DIR  = path.dirname(path.abspath(__file__))
SUIT_PARENT_DIR = path.dirname(CUR_DIR)
BASE_DIR = path.dirname(SUIT_PARENT_DIR)
APP = path.join(BASE_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

@pytest.fixture
def driver():
    
    CAPS = {
        'platformName': 'iOS',
        'platformVersion': '16.2',
        'deviceName': 'iPhone 14 Pro',
        'automationName': 'XCUITest',
        'app': APP,
    }
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )

    yield driver

    #Clean up
    driver.quit()