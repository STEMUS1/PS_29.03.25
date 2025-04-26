class ValueList:
    def __init__(self):
        self._values = []
        self._sum = 0
        self._sum_of_squares = 0
        self._count = 0

    def getElem(self, ind):
        if 0 <= ind < self._count:
            return self._values[ind]
        else:
            raise IndexError("Индекс вне диапазона")

    def setElem(self, ind, val):
        if 0 <= ind < self._count:
            old_value = self._values[ind]
            self._values[ind] = val
            self._sum += (val - old_value)
            self._sum_of_squares += (val**2 - old_value**2)
        else:
            raise IndexError("Индекс вне диапазона")

    def newElem(self, val):
        self._values.append(val)
        self._sum += val
        self._sum_of_squares += val**2
        self._count += 1

    def getAvg(self):
        if self._count == 0:
            return 0
        return self._sum / self._count

    def getSD(self):
        if self._count == 0:
            return 0
        mean = self.getAvg()
        variance = (self._sum_of_squares / self._count) - (mean ** 2)
        return variance ** 0.5

vl = ValueList()
vl.newElem(10)
vl.newElem(20)
vl.newElem(30)

print("Элемент по индексу 1:", vl.getElem(1))
print("Среднее:", vl.getAvg())
print("Среднеквадратичное отклонение:", vl.getSD())