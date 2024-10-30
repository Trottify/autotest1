import pytest
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

# переход на нужную страницу
driver.get(url="https://www.saucedemo.com/")
driver.implicitly_wait(2)

time.sleep(2)

login = "standard_user"
password = "secret_sauce"
time.sleep(2)

# Вводим логин
text = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
text.send_keys(login)

# Вводим пароль
text = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
text.send_keys(password)

time.sleep(2)

# авторизация
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button").click()

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]").click()

# Проверка
assert driver.current_url == "https://www.saucedemo.com/"

time.sleep(5)

# закрыть
driver.close()
driver.quit()
