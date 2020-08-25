class PasswordPage():
    def __init__(self,driver):
        self.driver = driver
        self.password_textbox_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input'
        self.password_sigin_btn = 'signInSubmit'
        self.invalid_password_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span'
        self.password_label_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/div[1]/div[1]/label'

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_id(self.password_sigin_btn).click()
        self.driver.implicitly_wait(2000)

    def invalid_password(self):
        password_element = self.driver.find_element_by_xpath(self.invalid_password_xpath)
        self.driver.implicitly_wait(2000)
        password_err_msg = password_element.text
        return password_err_msg

    def get_password_label(self):
        pwd_label = self.driver.find_element_by_xpath(self.password_label_xpath).text
        return pwd_label