import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pom.views.home_view import HomeView
from pom.views.echo_view import EchoView

@pytest.mark.tcid1
def test_echo_page(driver):
    home_view = HomeView(driver)
    echo_view = EchoView(driver)

    wait = WebDriverWait(driver, 10)
    home_view.nav_to_echo()

    MESSAGE_INPUT = 'Hello World'
    echo_view.save_text(MESSAGE_INPUT)
    saved_msg = echo_view.read_message()
    assert saved_msg == MESSAGE_INPUT, f"Message not saved correctly"

    #Back
    driver.back()

    home_view.nav_to_echo()
    saved_msg = echo_view.read_message()
    assert saved_msg == MESSAGE_INPUT, f"Message not displayed correctly"

