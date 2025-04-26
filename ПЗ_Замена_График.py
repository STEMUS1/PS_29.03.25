import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MathGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Построитель графиков функций")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.function_label = QLabel("Введите функцию (например: x**2, np.sin(x)):")
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("x**2")

        self.range_label = QLabel("Диапазон значений X:")
        self.xmin_input = QLineEdit()
        self.xmin_input.setPlaceholderText("-10")
        self.xmax_input = QLineEdit()
        self.xmax_input.setPlaceholderText("10")

        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_function)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.range_label)
        layout.addWidget(QLabel("X min:"))
        layout.addWidget(self.xmin_input)
        layout.addWidget(QLabel("X max:"))
        layout.addWidget(self.xmax_input)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.canvas)

        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                margin-top: 10px;
            }
            QLineEdit {
                font-size: 14px;
                padding: 5px;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px;
                background-color: #4CAF50;
                color: white;
                border: none;
                margin: 10px 0;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def plot_function(self):
        try:
            func_text = self.function_input.text().strip()
            if not func_text:
                raise ValueError("Введите функцию")

            xmin = float(self.xmin_input.text() or "-10")
            xmax = float(self.xmax_input.text() or "10")

            if xmin >= xmax:
                raise ValueError("Xmin должен быть меньше Xmax")

            x = np.linspace(xmin, xmax, 500)

            y = eval(func_text, {'np': np, 'x': x})

            self.figure.clear()

            ax = self.figure.add_subplot(111)
            ax.plot(x, y, 'b-', linewidth=2)
            ax.grid(True)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title(f'График функции: {func_text}')

            self.canvas.draw()

        except ValueError as ve:
            self.show_error(str(ve))
        except Exception as e:
            self.show_error(f"Ошибка: {str(e)}\nПроверьте правильность ввода функции")

    def show_error(self, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Warning)
        error_dialog.setWindowTitle("Ошибка")
        error_dialog.setText(message)
        error_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MathGraphApp()
    window.show()
    sys.exit(app.exec_())