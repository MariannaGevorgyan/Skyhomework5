from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

pole_username = driver.find_element(By.CSS_SELECTOR, "#username")
pole_username.send_keys("tomsmith")
sleep(5)

pole_password = driver.find_element(By.CSS_SELECTOR, "#password")
pole_password.send_keys("SuperSecretPassword!")
sleep(5)

Login_button = driver.find_element(By.CSS_SELECTOR, "button")
Login_button.click()

sleep(3)
driver.quit()