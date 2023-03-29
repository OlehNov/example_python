
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.close_support_ticket import Close_ticket
from pages.finish import Finish
from pages.login_page import Login_page
from pages.support_page import Support_page


def test_user_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open website page

    login = Login_page(driver)
    login.authorization()

    cst = Support_page(driver)
    cst.create_support_message()

    close_ticket = Close_ticket(driver)
    close_ticket.close_support_ticket()

    f = Finish(driver)
    f.finish_screen()















