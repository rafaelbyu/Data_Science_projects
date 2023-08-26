import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
from scipy import polyfit, polyval

df = pd.read_csv("dropped_human_csv.csv")

# def quadratic_approximation(x, y):
#     # Создаем матрицу A для нашей системы уравнений
#     A = np.vstack([x**2, x, np.ones(len(x))]).T
#     # Вычисляем вектор коэффициентов
#     a, b, c = np.linalg.lstsq(A, y, rcond=None)[0]
#     # Возвращаем функцию вида ax^2 + bx + c
#     return lambda x: a*x**2 + b*x + c


# Задаем нашу функцию

data_x = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S.%f')
data_x = data_x.astype('int64') // 10**9
data_x = data_x - 1690502400


data_y = df['Human'].values
x = data_x
y = data_y

# Аппроксимируем функцию
# f = quadratic_approximation(x, y)

a = np.polynomial.Chebyshev.fit(x, y, deg=10)
xx, yy = a.linspace()

# Строим графики исходной функции и аппроксимации
plt.plot(data_x, data_y, 'o', label='Data')
plt.plot(xx, yy, label='Polinomal approximation')
plt.legend()
plt.show()
