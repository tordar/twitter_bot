from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
import pyautogui
import sys

print("hello world")
print("cmd-c to quit")


driver = webdriver.Chrome(executable_path='/Users/tordartommervik/Desktop/chromedriver')
driver.get('https://twitter.com/login')
sleep(3)

driver.find_element_by_name('session[username_or_email]').send_keys("username goes here")
# insert username
driver.find_element_by_name('session[password]').send_keys('password goes here')
# insert password
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)
sleep(3)


tweet = driver.find_element_by_css_selector("br[data-text='true']")
# The element for the tweet field

tweet_button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
# tweet_gui_position = (711, 312)
# The actual tweet button

tweet.send_keys("this tweet was sent from a python bot")
# tweet.send_keys(Keys.RETURN)
sleep(3)
pyautogui.moveTo(715, 347, 2)
sleep(3)

pyautogui.click()

print(pyautogui.position())