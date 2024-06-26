from selenium.webdriver.common.by import By
import time

class YouTube:
    def __init__(self, browser, login, password):
        self.browser = browser
        self.login = login
        self.password = password

    def entrance(self, number):
        self.browser.get('https://accounts.google.com/ServiceLogin')
        user_login = self.browser.find_element(By.ID, 'identifierId')
        user_login.send_keys(self.login[number])
        
        button_next = self.browser.find_element(By.ID, 'identifierNext')
        button_next.click()

        time.sleep(2)

        user_password = self.browser.find_element(By.NAME, 'password')
        user_password.send_keys(self.password[number])

        button_next = self.browser.find_element(By.ID, 'passwordNext')
        button_next.click()

        time.sleep(5)

    def likes(self, link):
        self.browser.get(link)
        button_like = self.browser.find_element(By.CSS_SELECTOR, 'button[aria-label="I like this"]')
        button_like.click()
        time.sleep(10)
