import sys
import math
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class NewtonCooling(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Моделирование охлаждения по закону Ньютона")

        # Создаем элементы интерфейса
        self.initial_temp_label = QLabel("Начальная температура (°C):")
        self.initial_temp_input = QLineEdit()
        self.env_temp_label = QLabel("Температура среды (°C):")
        self.env_temp_input = QLineEdit()
        self.heat_transfer_label = QLabel("Коэффициент теплообмена (1/с):")
        self.heat_transfer_input = QLineEdit()
        self.plot_button = QPushButton("Построить")

        # Подключаем кнопку к функции построения графика
        self.plot_button.clicked.connect(self.plot_cooling)

        # Создаем виджет для отображения графика
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        # Создаем макеты для размещения элементов
        initial_temp_layout = QHBoxLayout()
        initial_temp_layout.addWidget(self.initial_temp_label)
        initial_temp_layout.addWidget(self.initial_temp_input)

        env_temp_layout = QHBoxLayout()
        env_temp_layout.addWidget(self.env_temp_label)
        env_temp_layout.addWidget(self.env_temp_input)

        heat_transfer_layout = QHBoxLayout()
        heat_transfer_layout.addWidget(self.heat_transfer_label)
        heat_transfer_layout.addWidget(self.heat_transfer_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(initial_temp_layout)
        main_layout.addLayout(env_temp_layout)
        main_layout.addLayout(heat_transfer_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        # Устанавливаем макет для окна
        self.setLayout(main_layout)

    def plot_cooling(self):
        "Отображает график охлаждения объекта по закону Ньютона."
        try:
            # Получите входные значения
            T0_str = self.initial_temp_input.text()
            Tenv_str = self.env_temp_input.text()
            k_str = self.heat_transfer_input.text()

            if not all([T0_str, Tenv_str, k_str]):
                raise ValueError("Пожалуйста, заполните все поля.")

            T0 = float(T0_str)
            Tenv = float(Tenv_str)
            k = float(k_str)

            # Проверка входных значений (k не может быть отрицательным)
            if k < 0:
                raise ValueError("Коэффициент теплообмена не может быть отрицательным.")

            # Моделирование охлаждения
            time = np.linspace(0, 60, 200)  # Время от 0 до 60 секунд
            T = Tenv + (T0 - Tenv) * np.exp(-k * time)  # Закон охлаждения

            # Очистите график
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            # Постройте график
            ax.plot(time, T)
            ax.set_xlabel("Время (с)")
            ax.set_ylabel("Температура (°C)")
            ax.set_title("Закон охлаждения Ньютона")
            ax.grid(True)
            self.figure.tight_layout()
            self.canvas.draw()

        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Непредвиденная ошибка: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NewtonCooling()
    window.show()
    sys.exit(app.exec_())