import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com", )
    parser.addoption("--tolerance", type=int, default=3)


@pytest.fixture
def browser(request):
    driver_base_path = '/Users/yuliamironova/drivers'
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    tolerance = request.config.getoption("--tolerance")
    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(service=Service(driver_base_path + "/chromedriver"), options=options)
    elif _browser == "opera":
        options = OperaOptions()
        if headless:
            options.headless = True
        driver = webdriver.Opera(executable_path=driver_base_path + "/operadriver", options=options)
    elif _browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(service=Service(driver_base_path + "/geckodriver"), options=options)

    if maximized:
        driver.maximize_window()

    request.addfinalizer(driver.quit)
    driver.t = tolerance
    driver.base_url = request.config.getoption("--url")

    def open(path=""):
        return driver.get(driver.base_url + path)

    driver.open = open

    return driver


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
