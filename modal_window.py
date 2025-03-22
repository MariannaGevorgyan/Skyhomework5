from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/entry_ad")
wait = WebDriverWait(driver, 20)
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)")))

close_button.click()
driver.quit()