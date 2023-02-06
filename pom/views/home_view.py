from appium.webdriver.common.appiumby import AppiumBy
from pom.views.base_view import BaseView

class HomeView(BaseView):
    ECHO_BAR = (AppiumBy.ACCESSIBILITY_ID, "Echo Box")

    def nav_to_echo(self):
        self.wait_for(self.ECHO_BAR).click()