'''
Author: Konstantin
'''
import pandas as pd
import random

# Генерируем данные
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})

data['is_robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['is_human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

# Выводим результат
print(data.head())