from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    ENTRY_PATH = '/index.php?route=product/category&path=20'
    TOTAL_COMPARE = (By.ID, 'compare-total')
    LIST_VIEW = (By.CLASS_NAME, 'fa.fa-th-list')
    ADD_TO_WISH = (By.CLASS_NAME, 'fa.fa-heart')
    SHOPPING_CART = (By.CLASS_NAME, 'fa.fa-shopping-cart')
    INPUT_LIMIT = (By.ID, 'input-limit')

    def presence_of_element(self):
        self._verify_element_presence(self.TOTAL_COMPARE)
        self._verify_element_presence(self.LIST_VIEW)
        self._verify_element_presence(self.ADD_TO_WISH)
        self._verify_element_presence(self.SHOPPING_CART)
        self._verify_element_presence(self.INPUT_LIMIT)
