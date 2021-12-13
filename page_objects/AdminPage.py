from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    ENTRY_PATH = '/admin'
    LOGIN_ADMIN_BUTTON = (By.CLASS_NAME, 'btn.btn-primary')
    MENU_CATALOG = (By.ID, 'menu-catalog')
    GO_TO_PRODUCT = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
    ADD_ITEM = (By.CLASS_NAME, 'fa.fa-plus')
    INPUT_NAME = (By.ID, 'input-name1')
    INPUT_META_TITLE = (By.ID, 'input-meta-title1')
    SAVE_BUTTON = (By.CLASS_NAME, 'fa.fa-save')
    PRODUCT_NAME = (By.ID, 'input-name')
    BUTTON_FILTER = (By.ID, 'button-filter')
    SELECT_PRODUCT = (
    By.CSS_SELECTOR, '#form-product > div > table > tbody > tr > td:nth-child(1) > input[type=checkbox]')
    DANGER = (By.CSS_SELECTOR, '#content > div.page-header > div > div > button.btn.btn-danger')
    MISS_ALERT = (By.CSS_SELECTOR, '#content > div.container-fluid > div.alert.alert-danger.alert-dismissible')
    SETTINGS = (By.ID, 'button-setting')
    LOGO = (By.ID, 'header-logo')
    USER_PROFILE = (By.ID, 'user-profile')
    ZOOM_IN = (By.CLASS_NAME, 'jqvmap-zoomin')
    ZOOM_OUT = (By.CLASS_NAME, 'jqvmap-zoomout')

    def login_as_admin(self):
        self._click(self.LOGIN_ADMIN_BUTTON)

    def go_to_catalog(self):
        self._click(self.MENU_CATALOG)

    def go_to_product(self):
        self._click(self.GO_TO_PRODUCT)

    def add_new_item(self):
        self._click(self.ADD_ITEM)
        self._element(self.INPUT_NAME).send_keys('test product')
        self._element(self.INPUT_META_TITLE).send_keys('test meta tag')
        self._click(self.SAVE_BUTTON)

    def delete_product_item(self):
        self._element(self.PRODUCT_NAME).send_keys('product')
        self._click(self.BUTTON_FILTER)
        self._click(self.SELECT_PRODUCT)
        self._click(self.DANGER)
        confirm = self.browser.switch_to.alert
        confirm.accept()

    def presence_of_elements(self):
        selectors = [self.SETTINGS, self.LOGO, self.USER_PROFILE, self.ZOOM_IN, self.ZOOM_OUT]
        for selector in selectors:
            self._verify_element_presence(selector)
