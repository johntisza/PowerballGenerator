from PyQt5 import uic

with open('powerball_ui.py', 'w') as py_file:
    uic.compileUi('pyqt_ui\\powerball_generator.ui', py_file)