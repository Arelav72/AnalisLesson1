import matplotlib.pyplot as plt
import numpy as np

# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
# линейный график
plt.hist(data, bins=6)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма")
plt.show()

# диаграмма рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​

x=np.random.rand(5)
y=np.random.rand(5)
plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")

plt.show()