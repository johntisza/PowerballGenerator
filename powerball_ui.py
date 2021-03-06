# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui\powerball_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 253)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerball_generator = QtWidgets.QPushButton(self.centralwidget)
        self.powerball_generator.setGeometry(QtCore.QRect(60, 90, 351, 31))
        self.powerball_generator.setAutoDefault(False)
        self.powerball_generator.setDefault(True)
        self.powerball_generator.setFlat(False)
        self.powerball_generator.setObjectName("powerball_generator")
        self.lotto_num_field = QtWidgets.QTextEdit(self.centralwidget)
        self.lotto_num_field.setGeometry(QtCore.QRect(60, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lotto_num_field.setFont(font)
        self.lotto_num_field.setFrameShape(QtWidgets.QFrame.Panel)
        self.lotto_num_field.setObjectName("lotto_num_field")
        self.powerball_copy = QtWidgets.QPushButton(self.centralwidget)
        self.powerball_copy.setGeometry(QtCore.QRect(60, 130, 351, 31))
        self.powerball_copy.setObjectName("powerball_copy")
        self.powerball_num_field = QtWidgets.QTextEdit(self.centralwidget)
        self.powerball_num_field.setGeometry(QtCore.QRect(370, 20, 41, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 107, 107))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.powerball_num_field.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.powerball_num_field.setFont(font)
        self.powerball_num_field.setFrameShape(QtWidgets.QFrame.Panel)
        self.powerball_num_field.setObjectName("powerball_num_field")
        self.numbers_label = QtWidgets.QLabel(self.centralwidget)
        self.numbers_label.setGeometry(QtCore.QRect(60, 60, 301, 16))
        self.numbers_label.setAlignment(QtCore.Qt.AlignCenter)
        self.numbers_label.setObjectName("numbers_label")
        self.PB_label = QtWidgets.QLabel(self.centralwidget)
        self.PB_label.setGeometry(QtCore.QRect(370, 60, 41, 16))
        self.PB_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PB_label.setObjectName("PB_label")
        self.powerball_web_button = QtWidgets.QPushButton(self.centralwidget)
        self.powerball_web_button.setGeometry(QtCore.QRect(60, 170, 351, 31))
        self.powerball_web_button.setAutoDefault(False)
        self.powerball_web_button.setDefault(False)
        self.powerball_web_button.setFlat(False)
        self.powerball_web_button.setObjectName("powerball_web_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lotto_num_field, self.powerball_num_field)
        MainWindow.setTabOrder(self.powerball_num_field, self.powerball_generator)
        MainWindow.setTabOrder(self.powerball_generator, self.powerball_copy)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Powerball Ticket Generator"))
        self.powerball_generator.setText(_translate("MainWindow", "Create Powerball Numbers"))
        self.lotto_num_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-weight:400;\"><br /></p></body></html>"))
        self.powerball_copy.setText(_translate("MainWindow", "Copy Powerball Numbers"))
        self.powerball_num_field.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400;\"><br /></p></body></html>"))
        self.numbers_label.setText(_translate("MainWindow", "Lotto Numbers"))
        self.PB_label.setText(_translate("MainWindow", "PB"))
        self.powerball_web_button.setText(_translate("MainWindow", "Check Winning Numbers"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Quit Program"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
