from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/login")


search_box1 = driver.find_element(By.CSS_SELECTOR, "#username")
search_box1.send_keys("tomsmith")
sleep(2)


search_box2 = driver.find_element(By.CSS_SELECTOR, "#password")
search_box2.send_keys("SuperSecretPassword!")
sleep(2)


driver.find_element(By.CSS_SELECTOR, "#login > button > i").click()
sleep(2)

driver.quit()