import matplotlib.pyplot as plt
import numpy as np

num_initial_points = 5

num_shifted_points = 10

initial_x = np.random.rand(num_initial_points) * 10
initial_y = np.random.rand(num_initial_points) * 10

shifted_x_data = []
shifted_y_data = []
central_x = []
central_y = []

for i in range(num_initial_points):

    sx = initial_x[i] + (np.random.rand(num_shifted_points) - 0.5) * 2
    sy = initial_y[i] + (np.random.rand(num_shifted_points) - 0.5) * 2

    sx_data.append(sx)
    sy_data.append(sy)

    central_x.append(np.mean(sx))
    central_y.append(np.mean(sy))

colors = ['r', 'g', 'b', 'c', 'm']
markers = ['o', 's', '^', 'v', 'D']

plt.figure(figsize=(10, 8))

for i in range(num_initial_points):
    plt.scatter(shifted_x_data[i], shifted_y_data[i], c=colors[i], marker=markers[i],)

x_err = [np.max(np.abs(x - m)) for x, m in zip(sx_data, central_x)]
y_err = [np.max(np.abs(y - m)) for y, m in zip(sy_data, central_y)]

plt.errorbar(central_x, central_y, xerr=x_err, yerr=y_err, fmt='k*', markersize=10,)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Смещенные и центральные точки")
plt.show()