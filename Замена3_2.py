import matplotlib.pyplot as plt
import numpy as np

sozivy = ["5-й созыв (2007-2011)", "6-й созыв (2011-2016)", "7-й созыв (2016-2021)", "8-й созыв (2021-2026)"]
parties = ["Единая Россия", "КПРФ", "ЛДПР", "Справедливая Россия", "Другие"]

seats = {
    "Единая Россия": [64.4, 52.6, 76.1, 72.2],
    "КПРФ": [11.6, 19.2, 11.5, 12.8],
    "ЛДПР": [8.1, 11.7, 10.3, 8.3],
    "Справедливая Россия": [7.7, 13.2, 6.2, 5.3],
    "Другие": [8.2, 3.3, 0, 1.4]
}

colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']


plt.figure(figsize=(12, 8))

x = np.arange(len(sozivy))
width = 0.7

bottom = np.zeros(len(sozivy))

for i, party in enumerate(parties):
    plt.bar(x, seats[party], width, bottom=bottom, label=party, color=colors[i])
    bottom += seats[party]

plt.xlabel("Созыв Государственной Думы")
plt.ylabel("Распределение мест (в процентах)")
plt.title("Распределение мест по партиям в Государственной Думе (стековый столбчатый график)")
plt.xticks(x, sozivy)
plt.ylim(0, 100)
plt.legend(loc="upper left")
plt.grid(True)
plt.show()