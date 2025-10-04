# calculator_logic.py
import math

class Calculator:
    def __init__(self):
        self._current = 0
        self._memory = 0
        self._history = []

    def add(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 0
        self._current = x + y
        self._history.append(f"{x} + {y} = {self._current}")
        return self._current

    def subtract(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 0
        self._current = x - y
        self._history.append(f"{x} - {y} = {self._current}")
        return self._current

    def multiply(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 1
        self._current = x * y
        self._history.append(f"{x} * {y} = {self._current}")
        return self._current

    def divide(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 1
        try:
            self._current = x / y
            self._history.append(f"{x} / {y} = {self._current}")
        except ZeroDivisionError:
            self._current = None
        return self._current

    def power(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 2
        self._current = x ** y
        self._history.append(f"{x} ** {y} = {self._current}")
        return self._current

    def sqrt(self, x=None):
        if x is None:
            x = self._current
        self._current = math.sqrt(x)
        self._history.append(f"sqrt({x}) = {self._current}")
        return self._current

    def factorial(self, x=None):
        if x is None:
            x = int(self._current)
        self._current = math.factorial(x)
        self._history.append(f"{x}! = {self._current}")
        return self._current

    def percentage(self, x=None, y=None):
        if x is None:
            x = self._current
        if y is None:
            y = 100
        self._current = (x * y) / 100
        self._history.append(f"{x}% of {y} = {self._current}")
        return self._current

    def store_memory(self):
        self._memory = self._current

    def recall_memory(self):
        return self._memory

    def clear_memory(self):
        self._memory = 0

    def get_current(self):
        return self._current

    def get_history(self):
        return self._history
