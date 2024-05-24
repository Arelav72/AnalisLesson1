from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Firefox()


# URL страницы
url = 'https://www.divan.ru/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Находим все элементы с ценами
prices = driver.find_elements(By.CLASS_NAME, 'ui-LD-ZU')

# Сохраняем цены в список
price_list = [price.text for price in prices]

# Закрываем драйвер
driver.quit()

# Создаем DataFrame и сохраняем в CSV
df = pd.DataFrame(price_list, columns=['Price'])
df.to_csv('prices.csv', index=False)

print('Цены успешно сохранены в prices.csv')