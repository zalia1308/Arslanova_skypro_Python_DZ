from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")


search_box = driver.find_element(By.CSS_SELECTOR, "input[type=number]")
search_box.send_keys("1000")
sleep(2)


search_box.clear()
sleep(2)


search_box = driver.find_element(By.CSS_SELECTOR, "input[type=number]")
search_box.send_keys("999")
sleep(2)

driver.quit()