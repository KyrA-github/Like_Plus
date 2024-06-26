# social/instagram.py
from selenium.webdriver.common.by import By
import time

class Instagram:
    def __init__(self, browser, login, password):
        self.browser = browser
        self.login = login
        self.password = password

    def entrance(self, number):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        
        user_login = self.browser.find_element(By.NAME, 'username')
        user_login.send_keys(self.login[number])
        
        user_password = self.browser.find_element(By.NAME, 'password')
        user_password.send_keys(self.password[number])

        button_login = self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button_login.click()

        time.sleep(5)

    def likes(self, link):
        self.browser.get(link)
        button_like = self.browser.find_element(By.CSS_SELECTOR, 'span[aria-label="Like"]')
        button_like.click()
        time.sleep(10)
