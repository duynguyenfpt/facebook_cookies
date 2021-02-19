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
        self.driver = webdriver.Chrome(executable_path="C:/Users/duynguyen/Documents/chrome_driver/chromedriver.exe", chrome_options=opt)
        self.driver.get('https://www.facebook.com/login.php')

    def nomralize_cookies(self, cookies):
        result = {}
        for cookie in cookies:
            result[cookie["name"]] = cookie["value"]
        return result

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
        return self.nomralize_cookies(self.driver.get_cookies())

    def access_personal_page(self, cookies):
        self.driver.get("https://m.facebook.com/" + cookies["c_user"])

    def execute_script(self, file_path='get_token_script.txt', script=''):
        _dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(_dir, 'resources', file_path), 'r') as script_file:
            final_script = script or script_file.read()

        return self.driver.execute_script(final_script)
