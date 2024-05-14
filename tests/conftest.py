import pytest
from selenium import webdriver


@pytest.fixture
def setup_driver():

    driver = webdriver.Chrome()

    driver.get("http://localhost:3000/master/users/sign_in")
    yield driver
    driver.quit()
