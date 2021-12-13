from selenium.webdriver.common.by import By
from .BasePage import BasePage


class UserRegistrationPage(BasePage):
    ENTRY_PATH = '/index.php?route=account/register'
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    CONFIRM_PASSWORD = (By.ID, 'input-confirm')
    CHECK_BOX = (By.CSS_SELECTOR, '#content > form > div > div > input[type=checkbox]:nth-child(2)')
    BUTTON = (By.CLASS_NAME, 'btn.btn-primary')

    def fill_in_register_form(self):
        self._element(self.FIRST_NAME).send_keys('Test First Name')
        self._element(self.LAST_NAME).send_keys('Test Last Name')
        self._element(self.EMAIL).send_keys('test458906@gmail.com')
        self._element(self.TELEPHONE).send_keys('79994445533')
        self._element(self.PASSWORD).send_keys('City1811')
        self._element(self.CONFIRM_PASSWORD).send_keys('City1811')
        self._click(self.CHECK_BOX)
        self._click(self.BUTTON)
