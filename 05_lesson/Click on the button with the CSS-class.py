from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
search_field = ("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
driver.find_element(By.XPATH, search_field).click()
sleep(4)
driver.quit()

