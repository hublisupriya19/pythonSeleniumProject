import configparser

class Config_Reader():

    config = configparser.ConfigParser()
    configFilePath = r'/Users/supriyahubli/PycharmProjects/pythonSeleniumProject/POM/Config.txt'
    config.read(configFilePath)

    chrome_driver_path = config.get('user_input','CHROME_DRIVER_PATH')
    website_to_automate = config.get('user_input','WEBSITE_TO_AUTOMATE')
    valid_email_id = config.get('user_input','VALID_SC_EMAIL_ID')
    invalid_email_id = config.get('user_input','INVALID_SC_EMAIL_ID')
    valid_password = config.get('user_input','VALID_SC_PASSWORD')
    invalid_password = config.get('user_input','INVALID_SC_PASSWORD')
    item_to_search = config.get('user_input','ITEM_TO_SEARCH')

    assert01_value = config.get('user_input','TEST01_ASSERT_VALUE')
    assert02_value = config.get('user_input','TEST02_ASSERT_VALUE')
    assert03_value = config.get('user_input','TEST03_ASSERT_VALUE')
    assert04_value = config.get('user_input','TEST04_ASSERT_VALUE')
    assert05_value = config.get('user_input','TEST05_ASSERT_VALUE')
    assert06_value = config.get('user_input','TEST06_ASSERT_VALUE')
    assert07_value = config.get('user_input','TEST07_ASSERT_VALUE')
    assert08_value = config.get('user_input','TEST08_ASSERT_VALUE')