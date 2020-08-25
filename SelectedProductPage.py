class SelectedProductPage():
    def __init__(self,driver):
        self.driver = driver
        self.add_to_cartbtn_id = 'add-to-cart-button'
        self.selected_product_title_id = 'productTitle'

    def get_selectedproduct_title(self):
        selectedproduct_title = self.driver.find_element_by_id(self.selected_product_title_id).text
        return selectedproduct_title

    def add_to_cart(self):
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_id(self.add_to_cartbtn_id).click()
        self.driver.implicitly_wait(2000)



