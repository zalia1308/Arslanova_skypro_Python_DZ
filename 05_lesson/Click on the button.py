from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for _ in range(5):    driver.find_element(By.CSS_SELECTOR, "#content > div > button").click()
buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(buttons))
sleep(4)
driver.quit()