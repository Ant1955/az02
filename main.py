# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
# - можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонение

import pandas as pd

data = {
    'Имя': ['Иван', 'Николай', 'Петр', 'Александр', 'Виктор', 'Анна','Ольга','Мария','Анастасия','Елена'],
    'Математика': [5, 4, 3, 1, 2, 5, 4, 3, 1, 2],
    'История': [10, 9, 8, 7, 6, 10, 9, 8, 7, 6],
    'География': [9, 8, 7, 6, 5, 9, 8, 7, 6, 5],
    'Физика': [8, 7, 6, 5, 4, 8, 7, 6, 5, 4],
    'Химия': [7, 6, 5, 4, 3, 7, 6, 5, 4, 3],
    'Биология': [6, 5, 4, 3, 2, 6, 5, 4, 3, 2],
}
df = pd.DataFrame(data)
print(df.head())
print(f"Средняя оценка по Математике- {df['Математика'].mean()}")
print(f"Медианная оценка по Математика - {df['Математика'].median()}")
print(f"Средняя оценка по Истории - {df['История'].mean()}")
print(f"Медианная оценка по Истории - {df['История'].median()}")
print(f"Средняя оценка по Географии- {df['География'].mean()}")
print(f"Медианная оценка по Географии - {df['География'].median()}")
print(f"Средняя оценка по Физике - {df['Физика'].mean()}")
print(f"Медианная оценка по Физике - {df['Физика'].median()}")
print(f"Средняя оценка по Химии - {df['Химия'].mean()}")
print(f"Медианная оценка по Химии - {df['Химия'].median()}")

Q1_math = df['Математика'].quantile(0.25)

Q3_math = df['Математика'].quantile(0.75)

print(f"по Математике Q1 {Q1_math}, Q3 {Q3_math}, IQR {Q3_math - Q1_math}")

print(f"Стандартное отклонение по Математике - {df['Математика'].std()}")