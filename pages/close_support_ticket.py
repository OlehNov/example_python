

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Close_ticket(Base):

    url = 'https://sfront.nuxbet.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Varibles

    # Locators
    close_button = '.ticketBtn'
    closed_text = '.ticketSingleInfo >:nth-child(2) span'

    # Getters

    def get_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.close_button)))


    # Actions

    def close_support(self):
        self.get_close_button().click()
        print('Click on Close button')



    #Methods

    def close_support_ticket(self):
        self.close_support()



