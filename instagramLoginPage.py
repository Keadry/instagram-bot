from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstagramLogIn:
    def __init__(self,username,password,driver):
        self.browser = driver
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        nameInput = self.browser.find_element(By.NAME,'username')
        passInput = self.browser.find_element(By.NAME ,'password')
        nameInput.send_keys(self.username)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)