from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page


def test_user_login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open website page
    login = Login_page(driver)
    login.authorization()

password_list = [1234, '4fSR@@%/--', ' ', 'мирумир', 'capsLOOK']
user_list = ['Max', 'Gamer', 'user', '', ' ', ]












