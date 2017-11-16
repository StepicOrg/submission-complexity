import math
from datetime import datetime, timedelta


class BaseVisitor(object):
    def __init__(self, start_time=None, time_limit=None):
        self.a = 0
        self.b = 0
        self.c = 0
        if start_time and time_limit:
            self.max_datetime = start_time + timedelta(seconds=time_limit)
        self.success = True

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    @property
    def abc_vector(self):
        return self.a, self.b, self.c

    def check_time_over(self):
        if self.max_datetime and datetime.now() > self.max_datetime:
            self.success = False
