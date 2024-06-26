from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self, browser, login, password):
        self.browser = browser
        self.login = login
        self.password = password

    def entrance(self):
        self.browser.get('https://twitter.com/login')
        user_login = self.browser.find_element(By.NAME, 'session[username_or_email]')
        user_login.send_keys(self.login)
        
        user_password = self.browser.find_element(By.NAME, 'session[password]')
        user_password.send_keys(self.password)

        button_login = self.browser.find_element(By.CSS_SELECTOR, 'div[data-testid="LoginForm_Login_Button"]')
        button_login.click()

        time.sleep(5)

    def likes(self, link):
        self.browser.get(link)
        button_like = self.browser.find_element(By.CSS_SELECTOR, 'div[data-testid="like"]')
        button_like.click()
        time.sleep(10)
