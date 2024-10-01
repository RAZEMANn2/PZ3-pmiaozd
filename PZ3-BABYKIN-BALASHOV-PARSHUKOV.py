import time
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Функция для замера времени выполнения
def time_fuzz(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# Измерение времени выполнения каждого метода
results = {}

results['fuzz.ratio'] = time_fuzz(fuzz.ratio, 'привет', "гамарджоба")
results['fuzz.partial_ratio (Привет мир, Люблю колбасу, Привет мир)'] = time_fuzz(fuzz.partial_ratio, 'Привет мир', 'Люблю колбасу, Привет мир')
results['fuzz.partial_ratio (Привет мир, Люблю колбасу, привет мир)'] = time_fuzz(fuzz.partial_ratio, 'Привет мир', 'Люблю колбасу, привет мир')
results['fuzz.token_sort_ratio (Привет наш мир, мир наш любимый Привет)'] = time_fuzz(fuzz.token_sort_ratio, 'Привет наш мир', 'мир наш любимый Привет')
results['fuzz.token_sort_ratio (1 2 Привет наш мир, 1 мир наш 2 ПриВЕт)'] = time_fuzz(fuzz.token_sort_ratio, '1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
results['fuzz.token_set_ratio'] = time_fuzz(fuzz.token_set_ratio, 'Привет наш мир', 'мир мир наш наш наш ПриВЕт')
results['fuzz.WRatio'] = time_fuzz(fuzz.WRatio, 'Привет наш мир', '!ПриВЕт наш мир!')

# Город
city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]

results['process.extract'] = time_fuzz(process.extract, "Саратов", city, limit=2)
results['process.extractOne'] = time_fuzz(process.extractOne, "Краногрск", city)

# Вывод результатов
for key, (result, elapsed_time) in results.items():
    print(f"{key} - Result: {result}, Time taken: {elapsed_time:.6f} seconds")

# Выводы о скорости и точности
print("\nВыводы о скорости и точности:\n")
sorted_results = sorted(results.items(), key=lambda x: x[1][1])  # Сортировка по времени выполнения
print("Сравнение методов по скорости:")
for key, (result, elapsed_time) in sorted_results:
    print(f"{key}: {elapsed_time:.6f} seconds")

print("\nТочность методов (оценка на основе результатов):")
for key, (result, elapsed_time) in results.items():
    if isinstance(result, str):
        print(f"{key}: Результат: {result} (можно оценить точность по значению)")
    else:
        print(f"{key}: Результат: {result} (можно оценить точность по значению)")
