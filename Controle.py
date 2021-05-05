# a biblioteca de controle tem dois tipos de sintaxe, nesse script utilizaremos a que se
from control.matlab import *
import matplotlib.pyplot as plt  # parece com a do matlab.
import numpy as np


sys = tf([1, 1], [1, 1])
print(sys)

plt.figure(1)

bode(sys)


plt.figure(2)
sysmf = feedback(sys, 1)
print(sysmf)
bode(sysmf)
