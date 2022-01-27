import pytest
import logging
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com", )
    parser.addoption("--tolerance", type=int, default=3)
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="remote", choices=["local", "remote"])
    parser.addoption("--remote_executor_url", action="store", default="http://localhost:4444/wd/hub")
    parser.addoption("--bversion", action="store", default="95.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--mobile", action="store_true", default=False)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver_base_path = '/Users/yuliamironova/drivers'
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    tolerance = request.config.getoption("--tolerance")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    executor_url = request.config.getoption("--remote_executor_url")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")
    test_name = request.node.name

    logs = request.config.getoption("--logs")
    logger = logging.getLogger('driver')
    logger.addHandler(logging.FileHandler(f"logs/log.log"))
    logger.setLevel(level=log_level)
    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))
    logger.info("Browser:{}".format(browser))

    driver = None

    if executor == "local":
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(service=Service(driver_base_path + "/chromedriver"), options=options)
        elif browser == "opera":
            options = OperaOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(executable_path=driver_base_path + "/operadriver", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(service=Service(driver_base_path + "/geckodriver"), options=options)
    else:
        caps = {
            "browserName": browser,
            "browserVersion": version,
            "screenResolution": "1280x1024",
            "name": "Tester1",
            "selenoid:options": {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
        }

        if browser == "chrome" and mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}

        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=caps)

    if not mobile:
        driver.maximize_window()

    driver.test_name = test_name
    driver.log_level = log_level
    driver.executor = executor
    driver.t = tolerance
    driver.base_url = request.config.getoption("--url")

    def open(path=""):
        return driver.get(driver.base_url + path)

    driver.open = open

    def fin():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")
