from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()


element = WebDriverWait(driver, 16)
element.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content > p"), "Data loaded with AJAX get request.")
    )

txt = driver.find_element(By.CSS_SELECTOR, "#content > p").text

print(txt)

driver.quit()