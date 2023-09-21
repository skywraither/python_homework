
#Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
#Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


import pandas as pd

# Загрузите данные из CSV файла
data = pd.read_csv('california_housing_test.csv')

# Фильтрация данных: выбираем строки, где кол-во людей (population) от 0 до 500
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости дома (median_house_value) для отфильтрованных данных
average_house_value = filtered_data['median_house_value'].mean()

print(f"Средняя стоимость дома для количества людей от 0 до 500: ${average_house_value:.2f}")
