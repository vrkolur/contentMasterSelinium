import time

from tests.conftest import setup_driver
from pages.client_admin_article_review_page import login_client_admin, create_artile, review_article_approve, review_article_reject
from basedb.articles import ArticlesDB
from basedb.messages import MessagesDB
def test_admin_scenario(setup_driver):
    driver = setup_driver
    articles_ob = ArticlesDB()
    messages_ob = MessagesDB()
    driver.get("http://localhost:3000/reliance/users/sign_in")

    # Should login into the page
    login_client_admin(driver,'reliance_admin@email.com', 'password')

    #Should create a new Article
    create_artile(driver,'Approve Article', 'This Article will be Approved')

    time.sleep(2)
    res = articles_ob.get_last_article()
    assert res == 'Approve Article'

    #Should approve the article
    review_article_approve(driver)
    time.sleep(2)
    res = articles_ob.get_last_article_status()
    assert res == True

    #should reject the article
    create_artile(driver, 'Reject Article', 'This article will be rejected and destroyed')
    review_article_reject(driver)

    time.sleep(2)
    res = articles_ob.get_article_by_title('Reject Article')
    assert None == res

    message = messages_ob.get_last_message_msg()

    assert message == ('Hey your article with title: Reject Article and Category: Category3 has been '
 'rejected and destroyed by your Admin')


