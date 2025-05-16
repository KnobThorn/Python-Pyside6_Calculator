import platform
import subprocess

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QGraphicsColorizeEffect
)
from PySide6.QtCore import *
from PySide6.QtGui import *


def is_dark_mode():
    system = platform.system()

    if system == "Windows":
        try:
            import winreg
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0
        except Exception:
            return False

    elif system == "Linux":
        try:
            theme = subprocess.check_output([
                "gsettings", "get", "org.gnome.desktop.interface", "color-scheme"
            ]).decode().strip().lower()
            return "dark" in theme
        except Exception:
            return False

    elif system == "Darwin":  # macOS
        try:
            result = subprocess.check_output(
                ["defaults", "read", "-g", "AppleInterfaceStyle"]
            ).decode().strip()
            return result.lower() == "dark"
        except Exception:
            return False

    return False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 510, 295)
        self.setFixedSize(QSize(510, 295))
        self.setWindowTitle("CALCULATOR")

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(5, 5, 500, 100)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.returnPressed.connect(self.equals_pressed)

        font = self.line_edit.font()
        font.setPointSize(30)
        self.line_edit.setFont(font)

        # Apply dark or light theme
        if is_dark_mode():
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2e2e2e;
                }
                QLineEdit {
                    background-color: #444;
                    color: white;
                    border: 0.25px solid white;
                    border-radius: 8px;
                }
                QPushButton {
                    background-color: #555;
                    color: white;
                    font-size: 18px;
                    font-family: Arial;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
        else:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #ffffff;
                }
                QLineEdit {
                    background-color: #f9f9f9;
                    color: black;
                    border: 0.25px solid black;
                    border-radius: 8px;
                }
                QPushButton {
                    background-color: #e0e0e0;
                    color: black;
                    font-size: 18px;
                    font-family: Arial;
                }
                QPushButton:hover {
                    background-color: #d0d0d0;
                }
            """)

        self.buttons()

    def buttons(self):
        button_1 = QPushButton("1", self)
        button_1.setGeometry(5, 110, 100, 45)
        button_1.clicked.connect(self.one_pressed)

        button_2 = QPushButton("2", self)
        button_2.setGeometry(105, 110, 100, 45)
        button_2.clicked.connect(self.two_pressed)

        button_3 = QPushButton("3", self)
        button_3.setGeometry(205, 110, 100, 45)
        button_3.clicked.connect(self.three_pressed)

        button_4 = QPushButton("4", self)
        button_4.setGeometry(5, 155, 100, 45)
        button_4.clicked.connect(self.four_pressed)

        button_5 = QPushButton("5", self)
        button_5.setGeometry(105, 155, 100, 45)
        button_5.clicked.connect(self.five_pressed)

        button_6 = QPushButton("6", self)
        button_6.setGeometry(205, 155, 100, 45)
        button_6.clicked.connect(self.six_pressed)

        button_7 = QPushButton("7", self)
        button_7.setGeometry(5, 200, 100, 45)
        button_7.clicked.connect(self.seven_pressed)

        button_8 = QPushButton("8", self)
        button_8.setGeometry(105, 200, 100, 45)
        button_8.clicked.connect(self.eight_pressed)

        button_9 = QPushButton("9", self)
        button_9.setGeometry(205, 200, 100, 45)
        button_9.clicked.connect(self.nine_pressed)

        button_decimal = QPushButton(".", self)
        button_decimal.setGeometry(205, 245, 100, 45)
        button_decimal.clicked.connect(self.decimal_pressed)

        button_0 = QPushButton("0", self)
        button_0.setGeometry(105, 245, 100, 45)
        button_0.clicked.connect(self.zero_pressed)

        button_modulus = QPushButton("%", self)
        button_modulus.setGeometry(5, 245, 100, 45)
        button_modulus.clicked.connect(self.modulus_pressed)

        button_clear = QPushButton("CLEAR", self)
        button_clear.setGeometry(305, 110, 100, 45)
        button_clear.clicked.connect(self.clear_pressed)

        button_delete = QPushButton("DELETE", self)
        button_delete.setGeometry(405, 110, 100, 45)
        button_delete.clicked.connect(self.delete_pressed)

        button_plus = QPushButton("+", self)
        button_plus.setGeometry(305, 155, 100, 45)
        button_plus.clicked.connect(self.plus_pressed)

        button_subtract = QPushButton("-", self)
        button_subtract.setGeometry(405, 155, 100, 45)
        button_subtract.clicked.connect(self.subtract_pressed)

        button_multiply = QPushButton("*", self)
        button_multiply.setGeometry(305, 200, 100, 45)
        button_multiply.clicked.connect(self.multipy_pressed)

        button_divide = QPushButton("/", self)
        button_divide.setGeometry(405, 200, 100, 45)
        button_divide.clicked.connect(self.divide_pressed)

        button_equals = QPushButton("=", self)
        button_equals.setGeometry(305, 245, 200, 45)
        button_equals.clicked.connect(self.equals_pressed)

        button_effect = QGraphicsColorizeEffect(self)
        button_effect.setColor(Qt.red)
        button_equals.setGraphicsEffect(button_effect)

    # Input functions...
    def one_pressed(self): self.line_edit.setText(self.line_edit.text() + "1")
    def two_pressed(self): self.line_edit.setText(self.line_edit.text() + "2")
    def three_pressed(self): self.line_edit.setText(self.line_edit.text() + "3")
    def four_pressed(self): self.line_edit.setText(self.line_edit.text() + "4")
    def five_pressed(self): self.line_edit.setText(self.line_edit.text() + "5")
    def six_pressed(self): self.line_edit.setText(self.line_edit.text() + "6")
    def seven_pressed(self): self.line_edit.setText(self.line_edit.text() + "7")
    def eight_pressed(self): self.line_edit.setText(self.line_edit.text() + "8")
    def nine_pressed(self): self.line_edit.setText(self.line_edit.text() + "9")
    def zero_pressed(self): self.line_edit.setText(self.line_edit.text() + "0")
    def plus_pressed(self): self.line_edit.setText(self.line_edit.text() + "+")
    def subtract_pressed(self): self.line_edit.setText(self.line_edit.text() + "-")
    def multipy_pressed(self): self.line_edit.setText(self.line_edit.text() + "*")
    def divide_pressed(self): self.line_edit.setText(self.line_edit.text() + "/")
    def modulus_pressed(self): self.line_edit.setText(self.line_edit.text() + "%")
    def decimal_pressed(self): self.line_edit.setText(self.line_edit.text() + ".")
    def clear_pressed(self): self.line_edit.setText("")
    def delete_pressed(self): self.line_edit.setText(self.line_edit.text()[:-1])
    def equals_pressed(self):
        try:
            answer = str(eval(self.line_edit.text()))
        except ZeroDivisionError:
            answer = "CANNOT DIVIDE BY ZERO"
        except SyntaxError:
            answer = "INVALID INPUT"
        self.line_edit.setText(answer)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
