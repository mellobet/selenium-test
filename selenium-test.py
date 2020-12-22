#!/usr/bin/env python3

from selenium import webdriver

URL = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

driver =  webdriver.Chrome()
driver.get(URL)


# Get and insert a string on a field.
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hallo')

showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()



# Drag and drop
from selenium.webdriver.common.action_chains import ActionChains

driver =  webdriver.Chrome()
driver.maximize_window()
URL = 'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver.get(URL)

source = driver.find_element_by_xpath('//*[@id="box1"]')
dest = driver.find_element_by_xpath('//*[@id="box101"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()


