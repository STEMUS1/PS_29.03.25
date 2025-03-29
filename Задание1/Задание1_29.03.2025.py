import sys
import math
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class TrajectoryPlotter(QWidget):
    def __init__(self):
        super().__init__()

        # Задаем заголовок окна
        self.setWindowTitle("Траектория брошенного тела")

        # Создаем элементы интерфейса
        self.velocity_label = QLabel("Начальная скорость (м/с):")
        self.velocity_input = QLineEdit()
        self.angle_label = QLabel("Угол броска (градусы):")
        self.angle_input = QLineEdit()
        self.plot_button = QPushButton("Построить траекторию")

        # Подключаем кнопку к функции построения графика
        self.plot_button.clicked.connect(self.plot_trajectory)

        # Создаем виджет для отображения графика
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        # Создаем макет для размещения элементов
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.velocity_label)
        input_layout.addWidget(self.velocity_input)
        input_layout.addWidget(self.angle_label)
        input_layout.addWidget(self.angle_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)  # Добавляем виджет графика

        # Устанавливаем макет для окна
        self.setLayout(main_layout)

    def plot_trajectory(self):

        'Функция для построения траектории полета тела, брошенного под углом к горизонту.'

        try:
            # Получаем значения из полей ввода и преобразуем их в числа
            initial_velocity = float(self.velocity_input.text())
            launch_angle = float(self.angle_input.text())

            # Проверяем входные значения
            if initial_velocity < 0:
                raise ValueError("Начальная скорость не может быть отрицательной.")
            if not 0 <= launch_angle <= 90:  # Угол от 0 до 90
                raise ValueError("Угол броска должен быть от 0 до 90 градусов.")

            # Переводим угол из градусов в радианы
            angle_radians = math.radians(launch_angle)

            # Определяем параметры полета
            g = 9.81  # Ускорение свободного падения
            total_time = (2 * initial_velocity * math.sin(angle_radians)) / g # общее время полета
            time_points = np.linspace(0, total_time, 100) # 100 точек для графика

            # Вычисляем координаты x и y для каждой точки времени
            x_coordinates = initial_velocity * time_points * math.cos(angle_radians)
            y_coordinates = (initial_velocity * time_points * math.sin(angle_radians) -
                             0.5 * g * time_points**2)

            # Очищаем предыдущий график, если он был
            self.figure.clear()
            ax = self.figure.add_subplot(111) # Создаем область рисования

            # Строим график траектории
            ax.plot(x_coordinates, y_coordinates)
            ax.set_xlabel("Расстояние (м)")
            ax.set_ylabel("Высота (м)")
            ax.set_title("Траектория полета тела, брошенного под углом к горизонту")
            ax.grid(True)  # Добавляем сетку для наглядности

            #Пересчитываем размеры, чтобы все влезло и обновляем график.
            self.figure.tight_layout()
            self.canvas.draw()

        except ValueError as e:
            # Обрабатываем ошибки ввода и выводим сообщение пользователю
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:  # Ловим вообще все ошибки, на всякий случай
            QMessageBox.critical(self, "Ошибка", f"Произошла непредвиденная ошибка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаем и показываем главное окно
    window = TrajectoryPlotter()
    window.show()

    sys.exit(app.exec_())