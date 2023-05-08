# Задача 3 Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см.
# Объем выборки равен 27, среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

import numpy as np
import scipy.stats as stats

D = 25
n = 27
M = 174.2
p = 0.95
alpha = 1 - p

t1 = stats.norm.ppf(alpha/2)
t2 = stats.norm.ppf(1-alpha/2)
print(t1, t2)

l_border = M+t1*np.sqrt(D)/np.sqrt(n)
r_border = M+t2*np.sqrt(D)/np.sqrt(n)
print(f'Доверительный интервал = [{l_border}, {r_border}]')