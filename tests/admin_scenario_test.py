import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.admin_login_page import login, new_client, toggle_client_active_status, edit_client_sub_domain, \
    master_admin_logout
from basedb.clients import ClientsDB
from basedb.client_users import ClientUserDB
from tests.conftest import setup_driver

xpath_new_client_btn = "//button[text()='New Client']"


def test_admin_scenario(setup_driver):
    driver = setup_driver
    clients_ob = ClientsDB()

    login(driver, 'admin@email.com', 'password')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Save']")))

    # First admin_loin
    assert driver.current_url == 'http://localhost:3000/clients', ("The current URL does not match the expected URL "
                                                                   "after adding a new client")
    time.sleep(1)

    # Create and verify ClientAdmin
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='New Client']")))

    new_client_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_new_client_btn)))
    new_client_btn.click()
    time.sleep(1)

    new_client(driver, 'Test Client', 'testclient')

    expected_value = 'testclient'
    time.sleep(2)
    actual_value = clients_ob.get_client_by_sub_domain('testclient')
    assert actual_value == expected_value, f"Expected value {expected_value}, but got {actual_value}"
    time.sleep(1)

    # # Toggle Client Status for the first Client
    toggle_client_active_status(driver)
    time.sleep(1)
    res = clients_ob.get_client_status('reliance')
    assert False == res, "Silke"

    # Edit the client sub_domain for the first client
    time.sleep(1)
    edit_client_sub_domain(driver, 'reliance')

    # res = clients_ob.get_client_status('testclient')
    # assert res == False, "Silke1"

    # Logout of the page
    master_admin_logout(driver)
    time.sleep(2)
