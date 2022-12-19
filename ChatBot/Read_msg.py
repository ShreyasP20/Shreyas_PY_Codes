from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

browser = webdriver.Chrome(
    executable_path='C:\\Users\\Shreyas\\Appdata\\Local\\Google\\Chrome\\User Data\\Wtsp')

browser.get('https://web.whatsapp.com/')

while True:
    search_xpath='//span[@aria-label="1 unread message"]'
    print(search_xpath)