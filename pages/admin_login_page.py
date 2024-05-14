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
xpath_client_is_active_btn = "//span[@id='client_active_status'][1]"


def login(driver, email, password):
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
    # new_client_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_new_client_btn)))
    # new_client_btn.click()

    client_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_client_name)))
    client_name_input.send_keys(name)

    client_sub_domain_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_sub_domain)))
    client_sub_domain_input.send_keys(sub_domain)

    client_save_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_client_save)))
    client_save_btn.click()


def toggle_client_sub_domain(driver, is_active):
    client_is_active_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_is_active_btn)))
    client_is_active_btn.click()
