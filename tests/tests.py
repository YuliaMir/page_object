from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage
from page_objects.UserRegistrationPage import UserRegistrationPage


def test_admin_add_item(driver):
    admin_page = AdminPage(driver, 5, True)
    admin_page.login_as_admin()
    admin_page.go_to_catalog()
    admin_page.go_to_product()
    admin_page.add_new_item()


def test_admin_delete_item(driver):
    admin_page = AdminPage(driver, 5, True)
    admin_page.login_as_admin()
    admin_page.go_to_catalog()
    admin_page.go_to_product()
    admin_page.delete_product_item()


def test_user_registration(driver):
    main_page = MainPage(driver, 5, True)
    main_page.go_to_register()
    register_page = UserRegistrationPage(driver, 5, True)
    register_page.fill_in_register_form()


def test_currency_change(driver):
    main_page = MainPage(driver, 5, True)
    main_page.change_currency()


def test_admin_page_elements(driver):
    admin_page = AdminPage(driver, 5, True)
    admin_page.login_as_admin()
    admin_page.presence_of_elements()


def test_main_page_elements(driver):
    main_page = MainPage(driver, 5, True)
    main_page.presence_of_elements()


def test_catalog_page_elements(driver):
    catalog_page = CatalogPage(driver, 5, True)
    catalog_page.presence_of_element()


def test_product_page_elements(driver):
    product_page = ProductPage(driver, 5, True)
    product_page.presence_of_element()
