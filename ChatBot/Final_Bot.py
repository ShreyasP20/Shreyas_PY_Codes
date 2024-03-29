from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

def reminder():
    browser = webdriver.Chrome(
    executable_path='C:\\Users\\Shreyas\\Appdata\\Local\\Google\\Chrome\\User Data\\Wtsp') 
#LINUX:/Users/akjasim/chromedriver/chromedriver


    browser.get('https://web.whatsapp.com/')

    with open('ChatBot\group.txt', 'r', encoding='utf8') as f:
        groups = [group.strip() for group in f.readlines()]

    with open('E:\PY projects\Py\ChatBot\msg.txt ', 'r', encoding='utf8') as f:
        msg = f.read()

    for group in groups:
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )

        search_box.clear()

        time.sleep(1)

        pyperclip.copy(group)

        search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

        time.sleep(2)

        group_xpath = f'//span[@title="{group}"]'
        group_title = browser.find_element("xpath", group_xpath)

        group_title.click()

        time.sleep(1)

        input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
        input_box = browser.find_element("xpath", input_xpath)

        pyperclip.copy(msg)
        input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
        input_box.send_keys(Keys.ENTER)

        time.sleep(2)
        

if __name__ == '__main__':
    reminder()