import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.likes_page import like_article, dislike_article, login
from tests.conftest import setup_driver
from basedb.likes import LikesDB


def test_client_admin_scenario(setup_driver):
    driver = setup_driver
    driver.get("http://localhost:3000/reliance/users/sign_in")

    login(driver, 'reliance_admin@email.com', 'password')

    likes_ob = LikesDB()
    # like Article
    like_article(driver)
    time.sleep(2)
    res = likes_ob.get_last_like_status()
    assert True == res
    time.sleep(2)
    res = likes_ob.get_last_like_user_id()
    assert 2 == res

    # dislike_article
    dislike_article(driver)
    time.sleep(2)
    res = likes_ob.get_last_like_status()
    assert False == res
    time.sleep(2)
    res = likes_ob.get_last_like_user_id()
    assert res == 2