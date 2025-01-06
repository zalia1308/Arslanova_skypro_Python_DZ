from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/textinput")

search_box = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_box.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()