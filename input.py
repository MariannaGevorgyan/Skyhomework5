from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

string = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/input")

string.send_keys(1000)
sleep(3)

string.clear()
sleep(3)

string.send_keys(999)