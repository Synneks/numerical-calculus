import math
from source.calculator import Calculator

Calculator.plot(-1, 1, 10, lambda x: math.e**x, 'e^x for n = 10')
