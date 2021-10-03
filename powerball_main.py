from powerball_ui import Ui_MainWindow
import random

from PySide2 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class PowerballGenerator(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)

        self.powerball_generator.clicked.connect(self.display_nums)
        self.powerball_copy.clicked.connect(self.copy_nums)
        self.powerball_web_button.clicked.connect(self.open_pb_website)
        self.actionQuit.triggered.connect(self.quit_app)

    def generate_lotto_nums(self):
        lotto_nums = []
        powerball_num = ""

        while len(lotto_nums) < 5:
            lotto_num = str(random.randint(1, 69))
            lotto_num = lotto_num.zfill(2)
            if lotto_num not in lotto_nums:
                lotto_nums.append(lotto_num)

        lotto_nums = sorted(lotto_nums)
        lotto_nums = " - ".join(lotto_nums)

        powerball_num = str(random.randint(1, 26))
        powerball_num = powerball_num.zfill(2)

        return lotto_nums, powerball_num

    def display_nums(self):
        lotto_nums, powerball_num = self.generate_lotto_nums()
        self.lotto_num_field.setText(lotto_nums)
        self.lotto_num_field.setAlignment(Qt.AlignCenter)
        self.powerball_num_field.setText(powerball_num)
        self.powerball_num_field.setAlignment(Qt.AlignCenter)

    def copy_nums(self):

        all_nums = f"Your lottery ticket:\t{self.lotto_num_field.toPlainText()}\t PB {self.powerball_num_field.toPlainText()} PB"

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.clear()
        clipboard.setText(all_nums)

    def open_pb_website(self):
        QtGui.QDesktopServices.openUrl("https://www.powerball.com/games/home")
        
    def quit_app(self):
        self.close()


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PowerballGenerator()
    ui.show()
    sys.exit(app.exec_())
