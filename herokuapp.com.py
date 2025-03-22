from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for _ in range (5):
    add_element_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add_element_button.click()

for _ in range (5):
    delete_buttons: WebElement = driver.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    delete_buttons.click()

    print(
        f"Размер списка кнопок Delete: {len(delete_buttons)}")
sleep(20)





