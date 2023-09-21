
#Задача 42: Узнать какая максимальная households в зоне минимального значения population.



import pandas as pd

# Загрузка данных из CSV файла
data = pd.read_csv('california_housing_test.csv')

# Находим минимальное значение "population"
min_population = data['population'].min()

# Фильтруем данные, чтобы выбрать только строки с минимальным "population"
min_population_data = data[data['population'] == min_population]

# Находим максимальное значение "households" в отфильтрованных данных
max_households_in_min_population = min_population_data['households'].max()

print(f"Максимальное количество households в зоне с минимальным population: {max_households_in_min_population}")
