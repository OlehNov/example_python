
from base.base_class import Base


class Finish(Base):

    url = 'https://sfront.nuxbet.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Varibles

    # Locators

    # Getters

    # Actions

    #Methods

    def finish_screen(self):
        self.get_current_url()
        # self.assert_url('https://sfront.nuxbet.com/tickets/')
        self.get_screenshot()



