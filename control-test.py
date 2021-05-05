import numpy as np 
import matplotlib as plt
import control as co

# %conifg InlineBackend.figure_format = 'svg' # plots will be in svg format
plt.rcParams['figure.figsize'] = [23,10] # you don't need this
plt.rcParams['font.size'] = 24

G1 = co.tf([2,5], [1,2,3])
G1

t = np.linspace(0, 10, 100)
t1, y1 = co.impulse_response(G1,t)

plt.pyplot.plot(t1, y1)
plt.pyplot.xlabel('time(s)')
plt.pyplot.ylabel('amplitude')
plt.pyplot.grid()