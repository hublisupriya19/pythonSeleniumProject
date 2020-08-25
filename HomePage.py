from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.navigateto_loginpage_id = 'nav-link-accountList'

    def click_signin(self):
        try:
            wait = WebDriverWait(self.driver,2000)
            nav_element = wait.until(EC.element_to_be_clickable((By.ID, 'nav-link-accountList')))
        except TimeoutException:
            print("Loading took too much time, could not find element to be clicked!")

        nav_element.click()
        title = self.driver.title

        return title


