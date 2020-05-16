__author__ = 'Amaan Izhar'

# This is the model class we are going to use for reminders.
class Reminders:
    def __init__(self, date_of_reminder='No date', time_of_reminder='No time', title='No title', content='No content'):
        """
            Method to initialize all instance variables and connect signals-slots.
        """
        self.__date_of_reminder = date_of_reminder
        self.__time_of_reminder = time_of_reminder
        self.__title = title
        self.__content = content

    def get_title(self):
        return self.__title

    def get_content(self):
        return self.__content

    def get_date_of_reminder(self):
        return self.__date_of_reminder

    def get_time_of_reminder(self):
        return self.__time_of_reminder

    def set_title(self, title):
        self.__title = title

    def set_content(self, content):
        self.__content = content

    def set_date_of_reminder(self, date_of_reminder):
        self.__date_of_reminder = date_of_reminder

    def set_time_of_reminder(self, time_of_reminder):
        self.__time_of_reminder = time_of_reminder

    def get_tuple(self):
        return ((self.get_date_of_reminder(), self.get_time_of_reminder(), self.get_title(), self.get_content()))

    def __str__(self):
        return f'Title: {self.get_title()}\nContent: {self.get_content()}\nDate of reminder: {self.get_date_of_reminder()}\nTime of reminder: {self.get_time_of_reminder()}\n'

    def __eq__(self, other):
        return self.get_title() == other.get_title() and self.get_content() == other.get_content() and self.get_date_of_reminder() == other.get_date_of_reminder() and self.get_time_of_reminder() == other.get_time_of_reminder()
