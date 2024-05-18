from datetime import date, timedelta

class util:
    def __init__(self):
        self.a=None
    
    def last_day(input1):
        temp=input1.replace(day=1) + timedelta(days=31)
        return temp-timedelta(days=temp.day)