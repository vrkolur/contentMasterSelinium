import pytest
from selenium import webdriver


@pytest.fixture
def setup_driver():

    driver = webdriver.Chrome()


    yield driver
    driver.quit()
