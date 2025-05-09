# PS_29.03.25
**Задание 1**
Описание: Программа для создания графика траектории движения тела, брошенного под углом к горизонту
Физические форрмулы: 
*   **Горизонтальное перемещение:**
    x(t) = v_0 \cdot t \cdot \cos(\theta)
*   **Вертикальное перемещение:**
    y(t) = v_0 \cdot t \cdot \sin(\theta) - \frac{1}{2} \cdot g \cdot t^2
    
    где:
    *   \(v_0\) - начальная скорость,
    *   \(t\) - время,
    *   \(\theta\) - угол броска,
    *   \(g\) - ускорение свободного падения (приблизительно 9.81 м/с²).

Какие параметры вводит пользователь: Начальная скорость (м/с), угол броска (в градусах)
График: парабола

**Задание 2**
Описание:  Программа для создания графика гармонического колебания
Физические формулы:
x(t) = A \cdot \sin(2 \pi f t + \varphi)

где:
*   \(A\) - амплитуда колебания,
*   \(f\) - частота колебания,
*   \(t\) - время,
*   \(\varphi\) - фаза колебания.
Какие параметры вводит пользователь: Амплитуда (м), частота (Гц), время (с), фаза (градусы)
График: синусоида

**Задание 3**
Описание: Программа для создания графика закона охлаждения Ньютона 
Физические формулы:
T(t) = T_{env} + (T_0 - T_{env}) \cdot e^{-kt}

где:
*   \(T(t)\) - температура тела в момент времени \(t\),
*   \(T_0\) - начальная температура тела,
*   \(T_{env}\) - температура окружающей среды,
*   \(k\) - коэффициент теплообмена,
*   \(t\) - время.
Какие параметры вводит пользователь: начальная температура (градусы Цельсия), температура окружающей среды (градусы Цельсия), коэффициент теплообмена (1/с)
График показывает, как температура тела изменяется со временем в процессе охлаждения.
