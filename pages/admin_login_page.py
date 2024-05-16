import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

xpath_admin_email = "//input[@id='user_email']"
xpath_admin_password = "//input[@id='user_password']"
xpath_admin_login = "//input[@type='submit' and @name='commit' and @value='Log in']"

xpath_new_client_btn = "//button[text()='New Client']"
xpath_client_name = "//input[@id='client_name']"
xpath_client_sub_domain = "//input[@id='client_sub_domain']"
xpath_client_save = "//input[@type='submit' and @value='Save']"

xpath_client_is_active_btn = "(//span[text()='Yes'])[1]"

xpath_client_edit_btn = "//a[@class='btn btn-primary btn-sm, edit-client' and @href='/clients/2/edit']"
xpath_client_edit_sub_domain_input = "//input[@id='client_sub_domain']"
xpath_client_edit_save_btn = "//input[@type='submit' and @name='commit' and @value='Save']"

xpath_client_log_out_btn = "//button[text()='Log Out']"


def login(driver, email, password):
    driver.get("http://localhost:3000/master/users/sign_in")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_admin_email)))
    email_field = driver.find_element(By.XPATH, xpath_admin_email)
    email_field.send_keys(email)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_admin_password)))
    password_field = driver.find_element(By.XPATH, xpath_admin_password)
    password_field.send_keys(password)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_admin_login)))
    login_button = driver.find_element(By.XPATH, xpath_admin_login)
    login_button.click()


def new_client(driver, name, sub_domain):
    client_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_client_name)))
    client_name_input.send_keys(name)

    client_sub_domain_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_sub_domain)))
    client_sub_domain_input.send_keys(sub_domain)

    client_save_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_client_save)))
    client_save_btn.click()


def toggle_client_active_status(driver):
    client_is_active_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_is_active_btn)))
    client_is_active_btn.click()


def edit_client_sub_domain(driver, edit_value):
    edit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_edit_btn))
    )
    edit_button.click()
    time.sleep(3)

    driver.implicitly_wait(10)

    sub_domain_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_edit_sub_domain_input))
    )
    driver.implicitly_wait(10)
    sub_domain_input.send_keys(edit_value)
    time.sleep(1)
    client_save_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_client_edit_save_btn)))
    client_save_btn.click()


def master_admin_logout(driver):
    log_out_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_log_out_btn))
    )
    log_out_btn.click()
