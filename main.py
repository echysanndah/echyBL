import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Open Browser
driver = webdriver.Chrome()
#Go to URL
driver.get("https://www.bukalapak.com/")

#Click Login
element = driver.find_element_by_link_text("Login")
element.click()

#Fill Phone Number
driver.find_element_by_xpath('//*[@id="user_identity_textfield"]').send_keys("081234567890");

#Click Submit
element = driver.find_element_by_id("submit_button")
element.click()