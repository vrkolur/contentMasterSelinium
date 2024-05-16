import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.client_admin_page import client_admin_login, create_new_client_user_details
from basedb.client_users import ClientUserDB
from basedb.client_users import ClientUserDB
from tests.conftest import setup_driver


def test_client_admin_scenario(setup_driver):
    driver = setup_driver
    client_users_ob = ClientUserDB()
    driver.get("http://localhost:3000/reliance/users/sign_in")
    client_admin_login(driver, 'reliance_admin@email.com', 'password')
    time.sleep(2)

    # Create a new Client User

    create_new_client_user_details(driver, 'Reliance Author 2134', 'reliance_author_new1234@email.com', 'password', 'password')
    time.sleep(1)


    # Here Check with the database

    res = client_users_ob.get_last_client_user()
    assert res == 2

    




