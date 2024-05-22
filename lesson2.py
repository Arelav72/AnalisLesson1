import pandas as pd

# Создание DataFrame
data = {
    'name': ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Екатерина", "Сергей", "Анна",
             "Владимир", "Наталья"],
    "school_subjects": ["Математика", "Русский язык", "История", "Физика", "Биология",
                        "Русский язык", "История", "Математика", "Биология", "Физика"],
    "school_grades": [5, 4, 5, 3, 5, 4, 5, 4, 5, 4]
}
df = pd.DataFrame(data)

# Вывод первых 5 строк DataFrame
print(df.head())

# Вывод статистики для числовых столбцов
print(df.describe())

# Фильтрация строк, где предмет "Математика"
math_grades = df[df['school_subjects'] == 'Математика']['school_grades']

# Вывод средней и медианной оценки по математике
print(f"Средняя оценка по математике - {math_grades.mean()}")
print(f"Медианная оценка по математике - {math_grades.median()}")

# Фильтрация строк, где предмет "Русский язык"
math_grades = df[df['school_subjects'] == 'Русский язык']['school_grades']

# Вывод средней и медианной оценки по Русскому языку
print(f"Средняя оценка по Русскому языку - {math_grades.mean()}")
print(f"Медианная оценка по Русскому языку - {math_grades.median()}")

# Фильтрация строк, где предмет "История"
math_grades = df[df['school_subjects'] == 'История']['school_grades']

# Вывод средней и медианной оценки по Истории
print(f"Средняя оценка по Истории - {math_grades.mean()}")
print(f"Медианная оценка по Истории - {math_grades.median()}")

# Фильтрация строк, где предмет "Физика"
math_grades = df[df['school_subjects'] == 'Физика']['school_grades']

# Вывод средней и медианной оценки по Физике
print(f"Средняя оценка по Физике - {math_grades.mean()}")
print(f"Медианная оценка по Физике - {math_grades.median()}")


# Фильтрация строк, где предмет "Биология"
math_grades = df[df['school_subjects'] == 'Биология']['school_grades']

# Вывод средней и медианной оценки по Биологии
print(f"Средняя оценка по Биологии - {math_grades.mean()}")
print(f"Медианная оценка по Биологии - {math_grades.median()}")

# Вычисление квартилей, стандартного отклонения и вывод этих значений
Q1 = df['school_grades'].quantile(0.25)
Q3 = df['school_grades'].quantile(0.75)

IQR = Q3 - Q1
# Нижняя и верхняя границы
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

std = df['school_grades'].std()

print(f"Первый квартиль оценок - {Q1}")
print(f"Третий квартиль оценок - {Q3}")
print(f"Межквартильный размах - {IQR}")
print(f"Нижняя граница - {downside}")
print(f"Верхняя граница - {upside}")
print(f"Стандартное отклонение оценки - {std}")
