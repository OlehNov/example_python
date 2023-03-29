from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base


class Payment_page(Base):

    url = 'https://sfront.nuxbet.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    amount = 100
    wallet = 'st79keW46g6ft45hy'
    transaction_number = 'f567654fg4d565g'


    # Locators

    deposit_button = ".userBlock.flexCenter.bold >:nth-child(2)"

# manual deposit
    manual_deposit_button = '.depMethodWrap >:nth-child(7) >.depMethodItem'
    deposit_amount = "//input[@type='number']"
    wallet_number = '.depSelected >:nth-child(7) >:nth-child(2)'
    transaction_id = '.depSelected >:nth-child(9) >:nth-child(2)'

# NowPayment
    now_payment_button = '.depMethodWrap >:nth-child(3) >.depMethodItem'
    now_payment_amount = "//input[@type='number']"

    continue_button = "//button[@class = 'mainBtn']"

    # Getters

    def get_deposit_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.deposit_button)))

    def get_now_payment(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.now_payment_button)))

    def get_manual_deposit_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.manual_deposit_button)))

    def get_now_payment_amount(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.now_payment_amount)))

    def get_deposit_amount(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.deposit_amount)))

    def get_wallet_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.wallet_number)))

    def get_transaction_id(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.transaction_id)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    # Actions

    def deposit(self):
        self.get_deposit_button().click()
        print('Click Deposit in header menu')


    def manual_deposit(self):
        self.get_manual_deposit_button().click()
        print('Click manual button')


    def now_payment_deposit(self):
        self.get_now_payment().click()
        print('Click now payment button')


    def input_amount(self, amount):
        self.get_deposit_amount().send_keys(amount)
        print('Input amount')


    def input_wallet(self, wallet_number):
        self.get_wallet_number().send_keys(wallet_number)
        print('Input wallet_id')


    def transaction(self, id_transaction):
        self.get_transaction_id().send_keys(id_transaction)
        print('Input transaction_id')


    def continue_btn(self):
        self.get_continue_button().click()
        print('Click continue button')


    #Methods

    def manual_payment(self):
        with allure.step('manual_payment'):
            self.driver.get(self.url)
            self.deposit()
            self.manual_deposit()
            self.input_amount(self.amount)
            self.input_wallet(self.wallet)
            self.transaction(self.transaction_number)
            self.continue_btn()

    def now_payment_payment(self):
        with allure.step('now_payment_payment'):
            self.driver.get(self.url)
            self.deposit()
            self.now_payment_deposit()
            self.input_amount(self.amount)
            self.continue_btn()


