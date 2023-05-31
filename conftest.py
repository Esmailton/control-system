from selenium.webdriver import Chrome
from pytest import fixture


@fixture(scope='session')
def browser():
    browser = Chrome()
    yield browser
    browser.quit()