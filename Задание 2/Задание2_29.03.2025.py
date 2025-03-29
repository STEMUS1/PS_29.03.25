import sys
import math
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class HarmonicOscillationPlotter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("График гармонического колебания")

        # Создаем элементы интерфейса
        self.amplitude_label = QLabel("Амплитуда (м):")
        self.amplitude_input = QLineEdit()
        self.frequency_label = QLabel("Частота (Гц):")
        self.frequency_input = QLineEdit()
        self.phase_label = QLabel("Фаза (градусы):")
        self.phase_input = QLineEdit()
        self.plot_button = QPushButton("Построить")

        # Подключаем кнопку к функции построения графика
        self.plot_button.clicked.connect(self.plot_oscillation)

        # Создаем виджет для отображения графика
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        # Создаем макеты для размещения элементов
        amplitude_layout = QHBoxLayout()
        amplitude_layout.addWidget(self.amplitude_label)
        amplitude_layout.addWidget(self.amplitude_input)

        frequency_layout = QHBoxLayout()
        frequency_layout.addWidget(self.frequency_label)
        frequency_layout.addWidget(self.frequency_input)

        phase_layout = QHBoxLayout()
        phase_layout.addWidget(self.phase_label)
        phase_layout.addWidget(self.phase_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(amplitude_layout)
        main_layout.addLayout(frequency_layout)
        main_layout.addLayout(phase_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        # Устанавливаем макет для окна
        self.setLayout(main_layout)

    def plot_oscillation(self):

        'Функция для построения графика гармонического колебания.'

        try:
            amplitude_str = self.amplitude_input.text()
            frequency_str = self.frequency_input.text()
            phase_str = self.phase_input.text()

            if not all([amplitude_str, frequency_str, phase_str]):
                raise ValueError("Пожалуйста, заполните все поля ввода.")
            amplitude = float(amplitude_str)
            frequency = float(frequency_str)
            phase_degrees = float(phase_str)

            if amplitude <= 0:
                raise ValueError("Амплитуда должна быть положительной.")
            if frequency <= 0:
                raise ValueError("Частота должна быть положительной.")

            phase_radians = math.radians(phase_degrees)

            time = np.linspace(0, 2 / frequency, 200)  # Отображаем 2 периода

            # Вычисляем смещение
            displacement = amplitude * np.sin(2 * math.pi * frequency * time + phase_radians)

            # Очищаем предыдущий график
            self.figure.clear()
            ax = self.figure.add_subplot(111)

            # Строим график
            ax.plot(time, displacement)
            ax.set_xlabel("Время (с)")
            ax.set_ylabel("Смещение (м)")
            ax.set_title("График гармонического колебания")
            ax.grid(True)
            self.figure.tight_layout()
            self.canvas.draw()

        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла непредвиденная ошибка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HarmonicOscillationPlotter()
    window.show()
    sys.exit(app.exec_())