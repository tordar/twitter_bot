from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
import pyautogui
import sys

print("hello world")


driver = webdriver.Chrome(executable_path='/Users/tordartommervik/Desktop/chromedriver')
driver.get('https://twitter.com/login')
sleep(3)

driver.find_element_by_name('session[username_or_email]').send_keys("****")
# insert username
driver.find_element_by_name('session[password]').send_keys('****')
# insert password
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)

lines = []
with open("text.txt") as f:
    text = f.readlines()
count = 0
for lines in text:
    if lines == "\n":
        continue
    count += 1
    print(f'line {count}: {lines}')
    pyautogui.moveTo(456, 268, 1)
    pyautogui.click()
    pyautogui.write(lines)
    pyautogui.hotkey('command', 'enter')
    # switch command out with enter for windows
    sleep(3)
    # increase sleep seconds if you don't want your twitter account blocked

f.close()

# To force quit program, drag mouse to far end of a corner
