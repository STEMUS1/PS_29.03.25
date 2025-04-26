import matplotlib.pyplot as plt
import numpy as np

subjects = ["Математический анализ", "Физика", "Химия", "История"]
num_grades = 5

grades = {}
for subject in subjects:
    grades[subject] = np.random.randint(2, 6, num_grades)  # randint(low, high, size)

colors = ['red', 'green', 'blue', 'orange']

plt.figure(figsize=(10, 6))

for i, subject in enumerate(subjects):
    plt.plot(grades[subject], marker='o', linestyle='-', color=colors[i], label=subject)

plt.xlabel("Номер оценки в семестре")
plt.ylabel("Оценка")
plt.title("Оценки по предметам за полугодие")
plt.ylim(2, 5)
plt.xticks(np.arange(num_grades))
plt.legend()
plt.show()