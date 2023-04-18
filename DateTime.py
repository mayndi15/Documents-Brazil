from datetime import timedelta
from datetime import datetime


# DATE - TIME
class DateTime:
    def __init__(self):
        self.register_date = datetime.today()

    def __str__(self):
        return self.format()

    def register_month(self):
        month_year = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]

        month = self.register_date.month - 1
        return month_year[month]

    def register_week(self):
        day_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        week = self.register_date.weekday()
        return day_week[week]

    def format(self):
        date = "%d/%m/%Y %H:%M"  # brazilian date pattern

        date_format = self.register_date.strftime(date)
        return date_format

    def time_register(self):
        time = (datetime.today() + timedelta(days=30)) - self.register_date
        return time
