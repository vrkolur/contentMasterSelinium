import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.client_admin_page import client_admin_login

xpath_new_artile_link = "//a[@class='nav-link new-article-link']"
xpath_article_title_field = "//input[@id='article_title']"
xpath_category_select = "//select[@id='article_category_id' ]"
xpath_category_choose = "//option[@value='3' ]"
xpath_tag_choose = "//input[@id='article_tag_ids_' and @value='2']"
xpath_body_field = "//trix-editor[@id='article_body' and @class='form-control mb-3' and @role='textbox']"
xpath_submit_btn = "//input[@type='submit' ]"

xpath_review_articles_link = "//a[text()='Review Articles']"
xpath_approve_article_btn = "//button[@data-article-id and text()='Approve']"
xpath_reject_article_btn = "//button[@data-article-id and text()='Reject']"


def login_client_admin(driver, email, password):
    client_admin_login(driver, email, password)
    time.sleep(1)


def create_artile(driver, title, body):
    new_article_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_new_artile_link)))
    new_article_link.click()

    title_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_article_title_field)))
    title_field.send_keys(title)

    category_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_category_select)))
    category_select.click()

    category_choose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_category_choose)))
    category_choose.click()

    tag_choose = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_tag_choose)))
    tag_choose.click()

    body_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_body_field)))
    body_field.send_keys(body)

    create_article_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_submit_btn)))
    create_article_btn.click()
    time.sleep(2)


def review_article_approve(driver):
    review_article_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_review_articles_link)))
    review_article_link.click()

    approve_article_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_approve_article_btn)))
    approve_article_btn.click()
    time.sleep(1)



def review_article_reject(driver):
    review_article_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_review_articles_link)))
    review_article_link.click()

    reject_article_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_reject_article_btn)))
    reject_article_btn.click()
