class EmailPage():
    def __init__(self,driver):
        self.driver = driver
        self.email_textbox_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]'
        self.email_continuebtn_id = 'continue'
        self.invalid_emailid_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span'

    def get_siginpg_title(self):
        signin_pg_title = self.driver.title
        return signin_pg_title

    def enter_email(self,emailid):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(emailid)
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_id(self.email_continuebtn_id).click()
        self.driver.implicitly_wait(2000)

    def invalid_emailid(self):
        email_element = self.driver.find_element_by_xpath(self.invalid_emailid_xpath)
        self.driver.implicitly_wait(2000)
        email_err_msg = email_element.text
        self.driver.implicitly_wait(2000)
        return email_err_msg