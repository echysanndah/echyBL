from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Open Browser
driver = webdriver.Chrome()
#Go to URL
driver.get("https://www.bukalapak.com/")

#Type on search
element = driver.find_element_by_xpath('//*[@id="v-omnisearch__input"]').send_keys("sepeda")

#Click search
element = driver.find_element_by_xpath('//*[@id="v-omnisearch"]/button')
element.click()