from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

pole = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/input")

pole.send_keys(1000)
sleep(3)

pole.clear()
sleep(3)

pole.send_keys(999)