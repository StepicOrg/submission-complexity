import math
from datetime import datetime


class BaseVisitor(object):
    def __init__(self, start_time=None, time_limit=None):
        self.a = 0
        self.b = 0
        self.c = 0
        self.start_time = start_time or datetime.now()
        self.time_limit = time_limit
        self.success = True

    @property
    def abc_score(self):
        return round(math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2), 2)

    @property
    def abc_vector(self):
        return self.a, self.b, self.c
