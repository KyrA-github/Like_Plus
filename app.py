import json
import time
import os
from flask import Flask, request, render_template, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from social.vk import VK
from social.twitter import Twitter
from social.instagram import Instagram
from social.youtube import YouTube

app = Flask(__name__)
options = Options()
options.add_argument("--headless")  # Безголовый режим для работы без интерфейса браузера

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join('json', 'users.json'))
    return redirect(url_for('index'))

@app.route('/start_promotion', methods=['POST'])
def start_promotion():
    social_network = request.form['social_network']
    promotion_type = request.form['promotion_type']
    link = request.form['link']
    times = int(request.form['times'])

    with open('json/users.json', 'r') as file:
        data = json.loads(file.read())

    login_user = [item['log'] for item in data['users']]
    password_user = [item['pass'] for item in data['users']]

    browser = webdriver.Chrome(service=ChromeService(executable_path=r'./webdriver/chromedriver.exe'), options=options)

    if social_network == 'vk':
        for i in range(len(login_user)):
            vk = VK(browser=browser, login=login_user, password=password_user)
            vk.entrance(i)
            if promotion_type == 'likes':
                vk.likes(link)
            time.sleep(times)

    elif social_network == 'twitter':
        for i in range(len(login_user)):
            twitter = Twitter(browser=browser, login=login_user, password=password_user)
            twitter.entrance(i)
            if promotion_type == 'likes':
                twitter.likes(link)
            time.sleep(times)

    elif social_network == 'instagram':
        for i in range(len(login_user)):
            instagram = Instagram(browser=browser, login=login_user, password=password_user)
            instagram.entrance(i)
            if promotion_type == 'likes':
                instagram.likes(link)
            time.sleep(times)

    elif social_network == 'youtube':
        for i in range(len(login_user)):
            youtube = YouTube(browser=browser, login=login_user, password=password_user)
            youtube.entrance(i)
            if promotion_type == 'likes':
                youtube.likes(link)
            time.sleep(times)

    browser.quit()
    return redirect(url_for('index'))

@app.route('/report')
def report():
    # Здесь можно реализовать функционал отчета
    return "Отчет пока не реализован."

if __name__ == '__main__':
    app.run(debug=True)
