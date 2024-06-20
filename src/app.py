import json
import time
import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from login_in.vk import VK


class App:
    def __init__(self):
        self.browser = webdriver.Chrome(service=ChromeService(executable_path=r'./webdriver/chromedriver.exe'))
        self.run()
        self.login_user = []
        self.password_user = []
        self.input_number_of_likes = 0
        self.link = ""

    def run_log(self, user_n):
        try:
            self.vk = VK(browser=self.browser, login=self.login_user, password=self.password_user)
            self.vk.entrance(user_n)  # Убедитесь, что индекс находится в пределах допустимого диапазона
            self.vk.likes(self.link)
        finally:
            self.browser.quit()

    def run(self):
        
        with open('json/users.json', 'r') as file:
            data = json.loads(file.read())

        self.login_user = [item['log'] for item in data['users']]
        self.password_user = [item['pass'] for item in data['users']]
        print("Загрузка...")
        for j in range(15):
            time.sleep(1)
        os.system("cls")  
        
        if 1 == int(input("Выберете коментарии <2> лайки <1>  >>> ")):
            self.input_number_of_likes = int(input("Количество лайков >>> "))
            while self.input_number_of_likes > len(self.login_user):
                self.input_number_of_likes = int(input("Количество лайков больше чем учетных записей >>> "))

            self.link = input("Введите ссылку >>> ")
            times = int(input("Введите время между лайками в секундах >>> "))
            while 1 == int(input(f"Общее время составит {self.input_number_of_likes*times} c. вас это устраивает? <1> да, <0> нет >>> ")):
                times = float(input("Введите время между лайками >>> "))
                print(int(input(f"Общее время составит {self.input_number_of_likes*times} c. вас это устраивает? <1> да, <0> нет >>> ")))

            for i in self.input_number_of_likes:
                time.sleep(times)
                self.run_log()

        


