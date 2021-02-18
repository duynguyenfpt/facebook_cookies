import time
import os
import json

from selenium import webdriver


class FacebookAccount():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        opt = webdriver.ChromeOptions()
        # opt.headless = True
        opt.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROME_DRIVER_PATH"), chrome_options=opt)
        self.driver.get('https://www.facebook.com/login.php')

    def login(self):
        element_email = self.driver.find_element_by_id('email')
        element_password = self.driver.find_element_by_id('pass')

        element_email.send_keys(self.email)
        element_password.send_keys(self.password)

        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click()

        #wait for login success
        time.sleep(5)

    def get_cookies(self):
        return self.driver.get_cookies()

    def execute_script(self, file_path='get_token_script.txt', script=''):
        with open(str(os.path.join('.', 'resources', file_path)), 'r') as script_file:
            final_script = script or script_file.read()

        return final_script
        # return self.driver.execute_script(final_script) 
