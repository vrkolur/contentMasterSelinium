import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from pages.client_admin_page import client_admin_login

xpath_home_link = "//a[@class='navbar-brand']"
xpath_like_first_article = "(//button[@type='button' and contains(@class, 'btn btn-sm like-button') and @data-article-id and @data-client-name='reliance' and @id='likeButton'])[1]"
xpath_dislike_first_article = "(//button[@type='button' and contains(@class, 'btn btn-sm dislike-button') and @data-article-id  and @id='dislikeButton'])[1]"


def login(driver, email,password):
    client_admin_login(driver, email,password)

def like_article(driver):
    home_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_home_link)))
    home_page.click()

    # like_btn =