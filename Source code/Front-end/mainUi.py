__author__ = 'Amaan Izhar'
"""
    Front-end:
    This is the GUI of the application.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 571)
        MainWindow.setMaximumSize(QtCore.QSize(966, 571))
        font = QtGui.QFont()
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #0f2027, stop:1 #203a43, stop:1 #2c5364);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 200, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-width: 3px;\n"
            "border-color: #161517;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit.setGeometry(QtCore.QRect(120, 200, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("background-color: #f7f8f8;\n"
                                     "border-radius: 7px;\n"
                                     "border-style: outset;\n"
                                     "border-width: 2px;\n"
                                     "border-color: #3c9fe6;\n"
                                     "color: #1c7987")
        self.line_edit.setObjectName("line_edit")
        self.content_label = QtWidgets.QLabel(self.centralwidget)
        self.content_label.setGeometry(QtCore.QRect(10, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.content_label.setFont(font)
        self.content_label.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-width: 3px;\n"
            "border-color: #161517;")
        self.content_label.setAlignment(QtCore.Qt.AlignCenter)
        self.content_label.setObjectName("content_label")
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(120, 260, 311, 131))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.text_edit.setFont(font)
        self.text_edit.setStyleSheet("background-color: #f7f8f8;\n"
                                     "border-radius: 7px;\n"
                                     "border-style: outset;\n"
                                     "border-width: 2px;\n"
                                     "border-color: #3c9fe6;\n"
                                     "color: #1c7987\n"
                                     "")
        self.text_edit.setObjectName("text_edit")
        self.date_edit = QtWidgets.QDateEdit(self.centralwidget)
        self.date_edit.setGeometry(QtCore.QRect(120, 20, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.date_edit.setFont(font)
        self.date_edit.setStyleSheet("background-color: #f7f8f8;\n"
                                     "border-radius: 7px;\n"
                                     "border-style: outset;\n"
                                     "border-width: 2px;\n"
                                     "border-color: #3c9fe6;\n"
                                     "color: #3543e6")
        self.date_edit.setObjectName("date_edit")
        self.date_edit.setMinimumDate(QtCore.QDate.currentDate())
        self.time_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.time_edit.setGeometry(QtCore.QRect(120, 80, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.time_edit.setFont(font)
        self.time_edit.setStyleSheet("background-color: #f7f8f8;\n"
                                     "border-radius: 7px;\n"
                                     "border-style: outset;\n"
                                     "border-width: 2px;\n"
                                     "border-color: #3c9fe6;\n"
                                     "color: #3543e6")
        self.time_edit.setObjectName("time_edit")
        self.time_edit.setMinimumTime(QtCore.QTime.currentTime())
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(10, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-width: 3px;\n"
            "border-color: #161517;")
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(10, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet(
            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
            "border-radius: 5px;\n"
            "border-style: solid;\n"
            "border-width: 3px;\n"
            "border-color: #161517;")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(550, 20, 391, 421))
        self.list_widget.setStyleSheet("background-color: #e6e9f0;\n"
                                       "border-radius: 7px;\n"
                                       "border-style: outset;\n"
                                       "border-width: 2px;\n"
                                       "border-color: #00000;")
        self.list_widget.setObjectName("list_widget")
        self.add_reminder_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_reminder_button.setGeometry(QtCore.QRect(190, 400, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_reminder_button.setFont(font)
        self.add_reminder_button.setStyleSheet("#add_reminder_button {\n"
                                               "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
                                               "border-radius: 5px;\n"
                                               "border-style: outset;\n"
                                               "border-width: 2px;\n"
                                               "border-color: #161517;\n"
                                               "}\n"
                                               "\n"
                                               "#add_reminder_button:pressed {\n"
                                               "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #c6ffdd, stop:1 #fbd786);\n"
                                               "}")
        self.add_reminder_button.setObjectName("add_reminder_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(550, 450, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("#delete_button {\n"
                                         "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
                                         "border-radius: 5px;\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-color: #161517;\n"
                                         "}\n"
                                         "#delete_button:pressed {\n"
                                         "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #c6ffdd, stop:1 #fbd786);\n"
                                         "}")
        self.delete_button.setObjectName("delete_button")
        self.clearAll_button = QtWidgets.QPushButton(self.centralwidget)
        self.clearAll_button.setGeometry(QtCore.QRect(850, 450, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.clearAll_button.setFont(font)
        self.clearAll_button.setStyleSheet("#clearAll_button {\n"
                                           "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
                                           "border-radius: 5px;\n"
                                           "border-style: outset;\n"
                                           "border-width: 2px;\n"
                                           "border-color: #161517;\n"
                                           "}\n"
                                           "#clearAll_button:pressed {\n"
                                           "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #c6ffdd, stop:1 #fbd786);\n"
                                           "}")
        self.clearAll_button.setObjectName("clearAll_button")
        self.remind_me_button = QtWidgets.QPushButton(self.centralwidget)
        self.remind_me_button.setGeometry(QtCore.QRect(190, 450, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.remind_me_button.setFont(font)
        self.remind_me_button.setStyleSheet("#remind_me_button {\n"
                                            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #1fa2ff, stop:1 #12d8fa);\n"
                                            "border-radius: 5px;\n"
                                            "border-style: outset;\n"
                                            "border-width: 2px;\n"
                                            "border-color: #161517;\n"
                                            "}\n"
                                            "#remind_me_button:pressed {\n"
                                            "background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #c6ffdd, stop:1 #fbd786);\n"
                                            "}")
        self.remind_me_button.setObjectName("remind_me_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 966, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DReminder"))
        self.title_label.setText(_translate("MainWindow", "Title:"))
        self.line_edit.setPlaceholderText(_translate("MainWindow", "Type here..."))
        self.content_label.setText(_translate("MainWindow", "Content: "))
        self.text_edit.setPlaceholderText(_translate("MainWindow", "Type here..."))
        self.date_label.setText(_translate("MainWindow", "Date: "))
        self.time_label.setText(_translate("MainWindow", "Time: "))
        self.add_reminder_button.setText(_translate("MainWindow", "Add to the list"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.clearAll_button.setText(_translate("MainWindow", "Clear All"))
        self.remind_me_button.setText(_translate("MainWindow", "REMIND ME"))
