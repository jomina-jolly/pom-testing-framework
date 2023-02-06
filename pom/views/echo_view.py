
from appium.webdriver.common.appiumby import AppiumBy
from pom.views.base_view import BaseView

class EchoView(BaseView):

    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'messageInput')
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'messageSaveBtn')
    SAVED_MESSAGE_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'savedMessage')

    def save_text(self, message='Hello'):
        
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.find(self.SAVE_BUTTON).click()

    def read_message(self):
        saved_txt_el = self.find(self.SAVED_MESSAGE_TEXT)
        saved_msg = saved_txt_el.text
        return saved_msg