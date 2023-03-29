from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Support_page(Base):

    url = 'https://sfront.nuxbet.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Varibles
    title = 'I need help!'
    description = "I can't change my bet!!!"


    # Locators
    support_sidebar_button = '.sidebarMain >:nth-child(13)'
    create_ticket_button = '.mainBtn.ticketBtn'
    input_title_field = ".sectionContent >form >:nth-child(1) >:nth-child(2)"
    input_description_field = "//textarea[ @class = 'description']"
    submit_ticket_button = "//button[ @class = 'mainBtn']"


    # Getters

    def get_support_sidebar_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.support_sidebar_button)))

    def get_create_ticket_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.create_ticket_button)))

    def get_input_title_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.input_title_field)))

    def get_input_description_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_description_field)))

    def get_submit_ticket_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_ticket_button)))


    # Actions

    def support_sidebar(self):
        self.get_support_sidebar_button().click()
        print('Click on Sidebar button')


    def ticket_button(self):
        self.get_create_ticket_button().click()
        print('Click on create ticket button')


    def title_field(self, title_text):
        self.get_input_title_field().send_keys(title_text)
        print('Input title name')


    def description_field(self, discription_text):
        self.get_input_description_field().send_keys(discription_text)
        print('Input deposit text')


    def submit_ticket(self):
        self.get_submit_ticket_button().click()
        print('Click LogIn pop-up button')


    #Methods

    def create_support_message(self):
        self.driver.get(self.url)
        self.support_sidebar()
        self.ticket_button()
        self.title_field(self.title)
        self.description_field(self.description)
        self.submit_ticket()

