from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SearchItemPage():
    def __init__(self,driver):
        self.driver = driver
        self.search_textbox_id = 'twotabsearchtextbox'
        self.welcome_msg_id = 'nav-your-amazon'

    def get_searchpg_msg(self):
        try:
            msg = self.driver.find_element_by_id(self.welcome_msg_id)
            self.driver.implicitly_wait(2000)
            searchpg_welcome_msg = msg.text
        except NoSuchElementException:
            print("Welcome message element not found!")
        return searchpg_welcome_msg

    def enter_search(self,item_to_search):
        searchbox = self.driver.find_element_by_id(self.search_textbox_id)
        self.driver.implicitly_wait(2000)
        searchbox.click()
        self.driver.implicitly_wait(2000)
        searchbox.send_keys(item_to_search)
        self.driver.implicitly_wait(2000)
        searchbox.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(2000)


