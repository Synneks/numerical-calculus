import math
import numpy as np
from source.calculator import Calculator

Calculator.plot(0, 70, 71, lambda x: np.cos((2*x + 1)*math.pi / 143), 'Tscheb. 1. Art for n = 71')
