from page_objects.AdminPage import AdminPage
from page_objects.MainPage import MainPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage
from page_objects.UserRegistrationPage import UserRegistrationPage


def test_admin_add_item(browser):
    admin_page = AdminPage(browser, True)
    admin_page.login_as_admin()
    admin_page.go_to_catalog()
    admin_page.go_to_product()
    admin_page.add_new_item()


def test_admin_delete_item(browser):
    admin_page = AdminPage(browser, True)
    admin_page.login_as_admin()
    admin_page.go_to_catalog()
    admin_page.go_to_product()
    admin_page.delete_product_item()


def test_user_registration(browser):
    main_page = MainPage(browser, True)
    main_page.go_to_register()
    register_page = UserRegistrationPage(browser, True)
    register_page.fill_in_register_form()


def test_currency_change(browser):
    main_page = MainPage(browser, True)
    main_page.change_currency()


def test_admin_page_elements(browser):
    admin_page = AdminPage(browser, True)
    admin_page.login_as_admin()
    admin_page.presence_of_elements()


def test_main_page_elements(browser):
    main_page = MainPage(browser, True)
    main_page.presence_of_elements()


def test_catalog_page_elements(browser):
    catalog_page = CatalogPage(browser, True)
    catalog_page.presence_of_element()


def test_product_page_elements(browser):
    product_page = ProductPage(browser, True)
    product_page.presence_of_element()
