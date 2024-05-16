import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

xpath_client_admin_email = "//input[@id='user_email']"
xpath_client_admin_password = "//input[@id='user_password']"
xpath_client_admin_login = "//input[@type='submit' and @name='commit' and @value='Log in']"

xpath_create_client_user_btn = "//a[text()='Create Client User']"
xpath_client_user_name_field = "//input[@id='client_user_name']"
xpath_client_user_email_field = "//input[@id='client_user_email']"
xpath_client_user_role_select = "//select[@id='client_user_role_id']"
xpath_client_user_role_select_choose = "//select[@id='client_user_role_id']/option[@value='3']"
xpath_client_user_password_field = "//input[@id='client_user_password']"
xpath_client_user_password_confirmation_field = "//input[@id='client_user_password_confirmation']"
xpath_client_user_create_btn = "//input[@type='submit']"


def client_admin_login(driver, email, password):
    driver.get("http://localhost:3000/reliance/users/sign_in")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_client_admin_email)))
    email_field = driver.find_element(By.XPATH, xpath_client_admin_email)
    email_field.send_keys(email)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_client_admin_password)))
    password_field = driver.find_element(By.XPATH, xpath_client_admin_password)
    password_field.send_keys(password)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_client_admin_login)))
    login_button = driver.find_element(By.XPATH, xpath_client_admin_login)
    login_button.click()


def create_new_client_user_details(driver, name, email, password, password_confirmation):
    new_client_user_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_create_client_user_btn)))
    new_client_user_btn.click()

    name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_client_user_name_field)))
    name_field.send_keys(name)

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_email_field)))
    email_field.send_keys(email)

    role_select_drop_down = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_role_select)))
    role_select_drop_down.click()

    role_select_role = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_role_select_choose)))
    role_select_role.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_password_field)))
    password_field.send_keys(password)

    password_confirmation_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_password_confirmation_field)))
    password_confirmation_field.send_keys(password_confirmation)

    create_user_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_client_user_create_btn)))
    create_user_btn.click()


