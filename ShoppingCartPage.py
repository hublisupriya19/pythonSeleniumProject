class ShoppingCartPage():
    def __init__(self,driver):
        self.driver = driver
        self.added_to_cart_xpath = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/h1'

    def verifyitem_added_to_cart(self):
        self.driver.implicitly_wait(2000)
        addedtocart_text = self.driver.find_element_by_xpath(self.added_to_cart_xpath).text
        return addedtocart_text



