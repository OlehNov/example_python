import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = 'https://sfront.nuxbet.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    user_name = 'gamer@mail.com'
    user_password = 'rf35+/-g'
    i = 0  # index


    # Locators

    log_in_header_menu = "//a[@class = 'loginBtn']"
    name = '.fieldWrap>input'
    password = '.passWrap>input'
    log_in_pop_up = '.btnWrap >:nth-child(2)'
    main_world = '.footerBlock.playNow h4'

    # Getters

    def get_log_in_header_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.log_in_header_menu)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.name)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_log_in_pop_up(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.log_in_pop_up)))

    def get_main_world(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.main_world)))


    # Actions

    def log_in_header(self):
        self.get_log_in_header_menu().click()
        print('Click LogIn header menu')


    def input_name(self, name):
        self.get_name().send_keys(name)
        print('Input User name')


    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input User name')


    def log_in_button(self):
        self.get_log_in_pop_up().click()
        print('Click LogIn pop-up button')


    #Methods

    def authorization(self):
        with allure.step('Authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.log_in_header()
            self.input_name('gamer@mail.com')
            self.input_password('rf35+/-g')
            self.log_in_button()
            # time.sleep(3)
            # error_message = self.driver.find_element(By.XPATH, "//div[@class = 'error']")
            # print(error_message.text)
            # self.assert_word(self.get_main_world(), 'Play now')
            # Logger.add_end_step(url=self.driver.current_url, method='authorization')


    # def try_autorization(self, list_user, list_password):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.log_in_header()
    #     while self.i < len(list_user):
    #         self.input_name(list_user[self.i])
    #         for index in list_password:
    #             self.input_password(list_password[index])
    #             self.log_in_button()
    #             time.sleep(1
    #             if self.driver.find_element(By.CSS_SELECTOR, ".footerBlock.playNow h4" == 'Play now'):
    #                 print(True)
    #             else:

            # self.log_in_button()
            # except TimeoutError:
            #     print('Sad story')









