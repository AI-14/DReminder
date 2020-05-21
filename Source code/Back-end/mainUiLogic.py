__author__ = 'Amaan Izhar'
"""
    Back-end:
    This script contains all the logical operations needed for the execution of the application. It uses 
    threading to show notification on windows. 
"""

from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QThread
from mainUi import Ui_MainWindow
from win10toast import ToastNotifier
from datetime import date, datetime
from reminders import Reminders
import heapq
from time import sleep
import sys


class MainWindowFunctionality(qtw.QMainWindow):
    def __init__(self):
        """
            Method to initialize all instance variables and connect signals-slots.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show_reminder = ShowReminder()
        self.list_of_reminders = []  #A list to store all components of the reminders in the form of a tuple.
        self.ui.list_widget.addItem('Reminder Titles:')
        self.ui.list_widget.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        self.ui.add_reminder_button.clicked.connect(self.add_reminder)
        self.ui.remind_me_button.clicked.connect(self.remind_me)
        self.ui.clearAll_button.clicked.connect(self.clear_all)
        self.ui.delete_button.clicked.connect(self.delete_reminders)

    def add_reminder(self):
        """
            Method to add the reminder to the list.
        """
        if self.ui.line_edit.text() == '':
            error_msg = qtw.QMessageBox()
            error_msg.setWindowTitle('Error')
            error_msg.setIcon(qtw.QMessageBox.Critical)
            error_msg.setText('Title field is empty!')
            error_msg.setStandardButtons(qtw.QMessageBox.Ok)
            error_msg.exec_()
        elif self.ui.text_edit.toPlainText() == '':
            error_msg = qtw.QMessageBox()
            error_msg.setWindowTitle('Error')
            error_msg.setIcon(qtw.QMessageBox.Critical)
            error_msg.setText('Content field is empty!')
            error_msg.setStandardButtons(qtw.QMessageBox.Ok)
            error_msg.exec_()
        else:
            r_date, r_month, r_year = self.ui.date_edit.date().day(), self.ui.date_edit.date().month(), self.ui.date_edit.date().year()  #Getting the date of reminder.
            date_format = f'{str(r_date)}-{str(r_month)}-{str(r_year)}'

            r_hour, r_minutes = self.ui.time_edit.time().hour(), self.ui.time_edit.time().minute()  #Getting the time of reminder.
            if r_hour in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                r_hour = '0' + str(r_hour)
            time_format = f'{str(r_hour)}:{str(r_minutes)}'

            msg_title = self.ui.line_edit.text()  #Getting the title of the remainder.
            msg_content = self.ui.text_edit.toPlainText()  #Getting the content of the reminder.

            if self.check_duplicate_title(msg_title):
                error_msg_dup = qtw.QMessageBox()
                error_msg_dup.setWindowTitle('Error')
                error_msg_dup.setIcon(qtw.QMessageBox.Critical)
                error_msg_dup.setText('Duplicate title exists. Please try a different one.')
                error_msg_dup.setStandardButtons(qtw.QMessageBox.Ok)
                error_msg_dup.exec_()
            else:
                reminder = Reminders(date_format, time_format, msg_title, msg_content)
                self.list_of_reminders.append(reminder.get_tuple()) #Adding a tuple so that heap sorts the reminders based on date and time.
                heapq.heapify(self.list_of_reminders)  #Using heapq for maintaining the order of the reminders based on date and time.
                self.ui.list_widget.clear()

                #Displaying on the list in sorted order.
                self.ui.list_widget.addItem('Reminder Titles:')
                for item in self.list_of_reminders:
                    self.ui.list_widget.addItem(item[2] + ' on ' + item[0] + ' @' + item[1])

                self.ui.line_edit.clear()
                self.ui.text_edit.clear()
                self.ui.time_edit.setMinimumTime(QtCore.QTime.currentTime())
                self.ui.date_edit.setMinimumDate(QtCore.QDate.currentDate())

    def check_duplicate_title(self, msg_title):
        """
            Method to check if any duplicate reminder title exists.
        """
        for item in self.list_of_reminders:
            if item[2] == msg_title:
                return True
        return False

    def delete_reminders(self):
        """
            Method to delete the reminders from the list.
        """
        sel_row = self.ui.list_widget.selectedIndexes()
        x = self.ui.list_widget.selectedItems()
        sel_item_text = x[0].text()

        for item in self.list_of_reminders:
            if item[2] in sel_item_text:
                self.ui.list_widget.takeItem(sel_row[0].row())
                self.list_of_reminders.remove(item)


    def clear_all(self):
        """
            Method to clear all reminders from the list.
        """
        self.ui.list_widget.clear()
        self.list_of_reminders.clear()
        self.ui.list_widget.addItem('Reminder Titles:')
        self.show_reminder.quit()  #Terminating the thread that notifies the user of the reminder.

    def remind_me(self):
        """
           Method to call the thread responsible for showing the reminder.
        """
        if len(self.list_of_reminders) == 0:
            reminders_completed_msg = qtw.QMessageBox()
            reminders_completed_msg.setWindowTitle('Information')
            reminders_completed_msg.setIcon(qtw.QMessageBox.Information)
            reminders_completed_msg.setText('All reminders are notified.')
            reminders_completed_msg.setStandardButtons(qtw.QMessageBox.Ok)
            reminders_completed_msg.exec_()
        else:
            confirmation_msg = qtw.QMessageBox()
            confirmation_msg.setWindowTitle('Information')
            confirmation_msg.setIcon(qtw.QMessageBox.Information)
            confirmation_msg.setText('All reminders are set and ready to be notified.')
            confirmation_msg.setStandardButtons(qtw.QMessageBox.Ok)
            confirmation_msg.exec_()
            self.show_reminder.content_of_reminder(self.list_of_reminders, self.ui.list_widget)
            self.show_reminder.start()


#This class is responsible for showing the toast notification.
class ShowReminder(QThread):
    def __init__(self):
        """
            Method to initialize all instance variables and connect signals-slots.
        """
        super().__init__()
        self.reminder_list = None
        self.list_widget = None

    def content_of_reminder(self, reminder_list, lw):
        """
            Method for referencing the list and list widget.
        """
        self.reminder_list = reminder_list
        self.list_widget = lw

    def run(self):
        """
            Method that runs the thread.
        """
        sentinel = True
        while sentinel:
            for item in self.reminder_list:
                today = str(date.today()).split('-')
                current_date, current_month, current_year = today[2], today[1], today[0]
                current_hours, current_minutes = str(datetime.now().time())[0:2], str(datetime.now().time())[3:5]
                reminder_date, reminder_month, reminder_year = item[0].split('-')
                time_hours, time_minutes = item[1][0:2], item[1][3:]
                r = datetime(int(reminder_year), int(reminder_month), int(reminder_date), int(time_hours),
                             int(time_minutes))
                c = datetime(int(current_year), int(current_month), int(current_date), int(current_hours),
                             int(current_minutes))
                num_of_secs = (r - c).total_seconds() #Getting the total number of seconds between the current time and reminder's time.
                if num_of_secs < 0:
                    self.list_widget.takeItem(1)
                    heapq.heappop(self.reminder_list)
                    continue
                sleep(num_of_secs)

                # showing the notification
                notifier = ToastNotifier()
                notifier.show_toast(item[2], item[3], duration=30, threaded=False)
                heapq.heappop(self.reminder_list)
                self.list_widget.takeItem(1) #Removing the reminder that was notified from the list widget.
                if len(self.reminder_list) == 0: #Condition to break out of the loop if all reminders are notified.
                    sentinel = False



#STARTING THE APPLICATION
if __name__ == '__main__':
    app = qtw.QApplication([])
    win = MainWindowFunctionality()
    win.show()
    sys.exit(app.exec_())
