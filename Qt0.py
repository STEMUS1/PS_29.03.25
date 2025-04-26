import sys
import math
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QDoubleValidator

class BallCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ball_calculator.ui', self)

        self.height_input.setValidator(QDoubleValidator(0.00, 10000.00, 2, self))
        self.time_input.setValidator(QDoubleValidator(0.00, 10000.00, 2, self))

        self.calculate_button.clicked.connect(self.calculate)
        self.clear_button.clicked.connect(self.clear_fields)

        self.height_input.setToolTip("Введите начальную высоту в метрах (м)")
        self.time_input.setToolTip("Введите время в секундах (с)")

        self.calculate_button.setEnabled(False)
        self.height_input.textChanged.connect(self.check_input)
        self.time_input.textChanged.connect(self.check_input)


    def check_input(self):
        try:
            height = float(self.height_input.text())
            time = float(self.time_input.text())

            if height <= 0:
                self.display_error("Высота должна быть больше нуля", "height")
                self.calculate_button.setEnabled(False)
                return

            if time < 0:
                self.display_error("Время не может быть отрицательным", "time")
                self.calculate_button.setEnabled(False)
                return

            self.display_error("", "all") # Clear all errors
            self.calculate_button.setEnabled(True)
        except ValueError:
            self.display_error("Некорректный формат числа", "all")
            self.calculate_button.setEnabled(False)


    def calculate(self):
        try:
            height = float(self.height_input.text())
            time = float(self.time_input.text())
            g = 9.81
            two_g = 2 * g

            time_of_impact = math.sqrt(2 * height / g)
            velocity_at_impact = math.sqrt(two_g * height)

            if time <= time_of_impact:
                y_coordinate = height - 0.5 * g * time**2
                velocity_at_time = g * time
            else:
                y_coordinate = 0
                velocity_at_time = velocity_at_impact

            self.time_of_impact_label.setText(f"{time_of_impact:.2f} с")
            self.velocity_at_impact_label.setText(f"{velocity_at_impact:.2f} м/с")
            self.y_coordinate_label.setText(f"{y_coordinate:.2f} м")
            self.velocity_at_time_label.setText(f"{velocity_at_time:.2f} м/с")

        except ValueError as e:
            self.display_error(str(e), "all")


    def clear_fields(self):
        self.height_input.clear()
        self.time_input.clear()
        self.time_of_impact_label.setText("")
        self.velocity_at_impact_label.setText("")
        self.y_coordinate_label.setText("")
        self.velocity_at_time_label.setText("")
        self.display_error("", "all")
        self.calculate_button.setEnabled(False)

    def display_error(self, message, field="all"):
        if field == "all":
            self.time_of_impact_label.setText(message)
            self.velocity_at_impact_label.setText("")
            self.y_coordinate_label.setText("")
            self.velocity_at_time_label.setText("")
        elif field == "height":
            self.time_of_impact_label.setText(message)  # Show height errors in same place for simplicity
        elif field == "time":
            self.velocity_at_impact_label.setText(message) # Show time errors in a different place


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BallCalculator()
    window.show()
    sys.exit(app.exec_())