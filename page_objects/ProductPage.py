from selenium.webdriver.common.by import By
from .BasePage import BasePage


class ProductPage(BasePage):
    ENTRY_PATH = '/index.php?route=product/product&product_id=40'
    ADD_BUTTON = (By.ID, 'button-cart')
    INPUT_QUANTITY = (By.ID, 'input-quantity')
    COMPARE = (By.CLASS_NAME, 'fa.fa-exchange')
    ADD_TO_WITH_LIST = (By.CLASS_NAME, 'fa.fa-heart')
    GO_BACK_HOME = (By.CLASS_NAME, 'fa.fa-home')

    def presence_of_element(self):
        self._verify_element_presence(self.ADD_BUTTON)
        self._verify_element_presence(self.INPUT_QUANTITY)
        self._verify_element_presence(self.COMPARE)
        self._verify_element_presence(self.ADD_TO_WITH_LIST)
        self._verify_element_presence(self.GO_BACK_HOME)
