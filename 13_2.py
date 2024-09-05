class Counter:

   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       if self.min_value <= start <= self.max_value:
           self.current = start
       else:
           raise ValueError("Initial value must be between minimum and maximum values.")

   def set_max(self, max_max):
       if max_max < self.min_value:
           raise ValueError("Maximum value cannot be less than minimum value.")
       self.max_value = max_max
       if self.current > self.max_value:
           self.current = self.max_value

   def set_min(self, min_min):
       if min_min > self.max_value:
           raise ValueError("Minimum value cannot be greater than maximum value.")
       self.min_value = min_min
       if self.current < self.min_value:
           self.current = self.min_value

   def step_up(self):
       if self.current < self.max_value:
           self.current += 1
       else:
           raise ValueError("Досягнуто максимум")

   def step_down(self):
       if self.current > self.min_value:
           self.current -= 1
       else:
           raise ValueError("Досягнуто мінімум")

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())

try:
    counter.step_up()
except ValueError as e:
    print(e)
print(counter.get_current())

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())

try:
    counter.step_down()
except ValueError as e:
    print(e)
print(counter.get_current())