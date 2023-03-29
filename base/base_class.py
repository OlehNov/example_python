import datetime

class Base:

    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        print('Current url ' + self.driver.current_url)

    '''Method assert word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value world - " + value_word)

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('.\\Screen\\' + name_screen)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")





