import time
import random
import numpy as np
import matplotlib.pyplot as plt


def f(n, iteration=1e5):
    iteration = int(iteration)
    result = np.array([0, 0, 0])
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    c = np.array([0, 0, 1])
    for i in range(iteration):
        n0 = n
        while True:
            if n0 <= 5:
                result += a
                break
            else:
                na = random.randint(1, 5)
                n0 -= na

            if n0 <= 5:
                result += b
                break
            else:
                nb = random.randint(1, 5)
                n0 -= nb

            if n0 <= 5:
                result += c
                break
            else:
                nc = random.randint(1, 5)
                n0 -= nc
    return result / iteration


n1_list = np.array(range(1, 41))
start = time.time()
rate1_list = np.array([f(i) for i in n1_list])
rate1_a = rate1_list[:, 0]
rate1_b = rate1_list[:, 1]
rate1_c = rate1_list[:, 2]
end = time.time()
print(f'cost = {end - start}')

fig = plt.figure(figsize=(10, 6))
plt.plot(n1_list, rate1_a, 'o-r', alpha=0.5)
plt.plot(n1_list, rate1_b, 'o-g', alpha=0.5)
plt.plot(n1_list, rate1_c, 'o-b', alpha=0.5)
plt.grid()
plt.xlabel('N')
plt.ylabel('rate')
plt.legend(['A', 'B', 'C'])
plt.title('figure 1')
fig.tight_layout()
plt.show()
