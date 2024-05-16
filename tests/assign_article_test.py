import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from basedb.clients import ClientsDB
from basedb.client_users import ClientUserDB
from tests.conftest import setup_driver
from pages.assign_article_page import login_admin, assign_article
from basedb.messages import MessagesDB


def test_assign_article(setup_driver):
    driver = setup_driver
    messages_ob = MessagesDB()
    driver.get("http://localhost:3000/reliance/users/sign_in")

    # login by ClientAdmin
    login_admin(driver, 'reliance_admin@email.com', 'password')

    # assign article to a author
    assign_article(driver, 'Assigned Article')

    res = messages_ob.get_last_message()

    assert res == 3
