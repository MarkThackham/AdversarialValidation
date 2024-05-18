from datetime import date, timedelta

class AdvanedAnalytics:
    def __init__(self, input1):
        self.startDate = input1

    def last_day(self):
        temp=self.startDate.replace(day=1) + timedelta(days=31)
        return temp-timedelta(days=temp.day)