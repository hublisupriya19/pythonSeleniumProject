from selenium.webdriver.common.action_chains import ActionChains

class ProductListPage():
    def __init__(self,driver):
        self.driver = driver
        self.search_link_bytext = 'Airpods Case, Airpods Protective Hard Case Cover with Keychain Compatible with AirPods 2/1 Cute Girls Men Durable Shockproof Anti Lost Case for AirPods Charging Case (Ice Blue Marble)'
        self.search_result_msg_xpath = '/html/body/div[1]/div[2]/span/div/span/h1/div/div[1]/div/div/span[3]'

    def get_search_result_msg(self):
        msg = self.driver.find_element_by_xpath(self.search_result_msg_xpath)
        self.driver.implicitly_wait(2000)
        productlistpg_result_msg = msg.text
        return productlistpg_result_msg

    def scroll_and_click_item(self):
        itemlink = self.driver.find_element_by_link_text(self.search_link_bytext)
        self.driver.implicitly_wait(2000)
        ActionChains(self.driver).move_to_element(itemlink).perform()
        self.driver.implicitly_wait(2000)
        itemlink.click()


