from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    ENTRY_PATH = '/'
    DROP_DOWN = (By.CSS_SELECTOR, '#top-links > .list-inline > .dropdown > a.dropdown-toggle')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a')
    EURO = (By.CSS_SELECTOR, '#form-currency > div > ul > li:nth-child(1) > button')
    POUND = (By.CSS_SELECTOR, '#form-currency > div > ul > li:nth-child(2) > button')
    DOLLAR = (By.CSS_SELECTOR, '#form-currency > div > ul > li:nth-child(3) > button')
    FORM_CURRENCY = (By.ID, 'form-currency')
    CART_TOTAL = (By.ID, 'cart-total')
    SEARCH = (By.ID, 'search')
    CART = (By.ID, 'cart')
    MENU = (By.ID, 'menu')

    def go_to_register(self):
        self._click(self.DROP_DOWN)
        self._click(self.REGISTER_BUTTON)

    def change_currency(self):
        self._click(self.FORM_CURRENCY)
        self._click(self.EURO)
        self._click(self.FORM_CURRENCY)
        self._click(self.POUND)
        self._click(self.FORM_CURRENCY)
        self._click(self.DOLLAR)

    def presence_of_elements(self):
        self._verify_element_presence(self.FORM_CURRENCY)
        self._verify_element_presence(self.CART_TOTAL)
        self._verify_element_presence(self.SEARCH)
        self._verify_element_presence(self.CART)
        self._verify_element_presence(self.MENU)
