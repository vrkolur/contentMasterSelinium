import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from pages.client_admin_page import client_admin_login

xpath_assign_article_link = "//a[text()='Assign Articles']"
xpath_title_field = "//input[@id='title']"
xpath_select_category = "//select[@id='category_id']"
xpath_choose_category = "//option[text()='Category2']"
xpath_select_author = "//select[@id='author_id']"
xpath_choose_author = "//option[text()='reliance_author_1@email.com']"
xpath_submit_assign_article = "//input[@type='submit']"


def login_admin(driver, email, password):
    client_admin_login(driver, email, password)


def assign_article(driver, title):
    assign_article_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_assign_article_link)))
    assign_article_link.click()

    title_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_title_field)))
    title_field.send_keys(title)

    select_category = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_select_category)))
    select_category.click()

    choose_category = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_choose_category)))
    choose_category.click()

    select_author = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_select_author)))
    select_author.click()

    choose_author = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_choose_author)))
    choose_author.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_submit_assign_article))).click()
