from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from pages.login_page import Login_page
from pages.payment_page import Payment_page


@allure.description('Test manual deposit')
def test_manual_deposit(set_up, set_group):

    # print('Start test 1')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open website page

    login = Login_page(driver)

    login.authorization()

    tpa = Payment_page(driver)
    tpa.manual_payment()

    # print('Finish test 1')

    driver.quit()


@allure.description('Test now payment')
def test_now_payment(set_up, set_group):

    print('Start test 2')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open website page

    login = Login_page(driver)
    login.authorization()

    tpa = Payment_page(driver)
    tpa.now_payment_payment()

    print('Finish test 2')

    driver.quit()










