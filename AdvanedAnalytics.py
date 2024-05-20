from datetime import date, timedelta

class AdvanedAnalytics:
    # WoE encoding
    # Target encoding
    # IV
    # Correlation
    # VIF
    # Adversarial Validation
    # RFECV
    # Optuna
    # FLAML



    def __init__(self):
        self._a=None
    
    def last_day(input1):
        # Utility to return the last day of the month
        temp=input1.replace(day=1) + timedelta(days=31)
        return temp-timedelta(days=temp.day)
    
    def first_day(input1):
        # Utility to return the first day of the month
        temp=input1.replace(day=1)
        return temp