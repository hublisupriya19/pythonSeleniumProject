import unittest
from selenium import webdriver
from POM.Pages.HomePage import HomePage
from POM.Pages.EmailPage import EmailPage
from POM.Pages.PasswordPage import PasswordPage
from POM.Pages.SearchItemPage import SearchItemPage
from POM.Pages.ProductListPage import ProductListPage
from POM.Pages.SelectedProductPage import SelectedProductPage
from POM.Pages.ShoppingCartPage import ShoppingCartPage
from POM.Config_Reader import Config_Reader

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=Config_Reader.chrome_driver_path)
        cls.driver.implicitly_wait(2000)
        cls.driver.get(Config_Reader.website_to_automate)
        cls.driver.implicitly_wait(2000)
        cls.driver.fullscreen_window()

    def test01_navigation(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        home = HomePage(driver)
        driver.implicitly_wait(2000)
        title = home.click_signin()
        self.assertEqual(title,Config_Reader.assert01_value)

    def test02_invalid_email(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        email = EmailPage(driver)
        driver.implicitly_wait(2000)
        email.enter_email(Config_Reader.invalid_email_id)
        driver.implicitly_wait(2000)
        err_msg = email.invalid_emailid()
        self.assertEqual(err_msg,Config_Reader.assert02_value,"Wrong Error Message!!")

    def test03_valid_email(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        email = EmailPage(driver)
        driver.implicitly_wait(2000)
        email.enter_email(Config_Reader.valid_email_id)
        driver.implicitly_wait(2000)

        pwd = PasswordPage(driver)
        driver.implicitly_wait(2000)
        pwdlabel = pwd.get_password_label()
        self.assertEqual(pwdlabel,Config_Reader.assert03_value)

    def test04_invalid_password(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        pwd = PasswordPage(driver)
        driver.implicitly_wait(2000)
        pwd.enter_password(Config_Reader.invalid_password)
        driver.implicitly_wait(2000)
        password_err_msg = pwd.invalid_password()
        self.assertEqual(password_err_msg,Config_Reader.assert04_value)

    def test05_valid_password(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        pwd = PasswordPage(driver)
        driver.implicitly_wait(2000)
        pwd.enter_password(Config_Reader.valid_password)
        driver.implicitly_wait(20)

        searchpage = SearchItemPage(driver)
        searchpg_welcome_msg = searchpage.get_searchpg_msg()
        self.assertEqual(searchpg_welcome_msg,Config_Reader.assert05_value,"Login Error: Not navigated to the right page!!")

    def test06_searchforitem(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        searchpage = SearchItemPage(driver)
        driver.implicitly_wait(2000)
        searchpage.enter_search(Config_Reader.item_to_search)
        driver.implicitly_wait(20)

        productlist = ProductListPage(driver)
        productlistpg_result_msg = productlist.get_search_result_msg()
        self.assertEqual(productlistpg_result_msg,Config_Reader.assert06_value,'Error: Did not navigate to search results page!!')


    def test07_clicksearcheditem(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        productlist = ProductListPage(driver)
        driver.implicitly_wait(2000)
        productlist.scroll_and_click_item()
        driver.implicitly_wait(20)

        selectedproduct = SelectedProductPage(driver)
        selectedproduct_title = selectedproduct.get_selectedproduct_title()
        self.assertEqual(selectedproduct_title,Config_Reader.assert07_value)


    def test08_add_to_cart(self):
        driver = self.driver
        driver.implicitly_wait(2000)

        selectedproduct = SelectedProductPage(driver)
        driver.implicitly_wait(2000)
        selectedproduct.add_to_cart()
        driver.implicitly_wait(20)

        shopping_cart = ShoppingCartPage(driver)
        addedtocart_text = shopping_cart.verifyitem_added_to_cart()
        self.assertEqual(addedtocart_text,Config_Reader.assert08_value,'Error:Item not added to Cart!!')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.implicitly_wait(2000)
        cls.driver.close()
        cls.driver.quit()

if __name__ == 'main':
    unittest.main()