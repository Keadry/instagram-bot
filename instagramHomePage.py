from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstagramHome:
    def __init__(self,driver):
        self.browser = driver

    def getFollowers(self):
        time.sleep(5)
        self.browser.maximize_window()
        self.browser.get(f'https://www.instagram.com/{self.username}')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , '._ac2a')))
        followers_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, 'follower')
        followers_link.click()
        time.sleep(3)
        dialog = self.browser.find_element(By.CSS_SELECTOR , 'div._aano div:nth-child(1) [style*="display: flex; flex-direction: column;"]')
        follower_count = 0
        while True:
            dialog.click()
            self.browser.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", dialog)
            time.sleep(1) 

            newCount = self.browser.execute_script("return arguments[0].scrollHeight;", dialog)

            if follower_count == newCount:
                break
            
            follower_count = newCount

        followers = dialog.find_elements(By.CSS_SELECTOR,'.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')

        for follower in followers:
            username = follower.find_element(By.XPATH, './/a').get_attribute('href')
            print(username)

