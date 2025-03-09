import matplotlib.pyplot as plt
import numpy as np

def sine(x, frec, phase = 0):
    rad = x * (2*np.pi*frec)
    y = np.sin(rad + phase/360*2*np.pi)
    return y

def saw(x, frec, min = -1, max = 1):
    period = 1/frec
    y = (max-min) * (x / period - np.floor(x/period + 1/2)) + max - (max-min)/2
    return y

def triangle(x, frec):
    period = 1/frec
    y = 2 * (2 * np.abs(x / period - np.floor(x/period + 1/2))) - 1
    return y

def vca(i, cv, depth):
    y = i * (1-depth + depth*cv)
    return y

x = np.linspace(0, 1, 2000)

a = saw(x, 2, max=1, min=-1)
b = 0*x
c = sine(x, 50, 180)
d = triangle(x,5)

y1 = c
m = a
y2 = vca(y1,m,0.2)

#plt.subplot(1, 3, 1)
plt.plot(x, y1, label="input")
#plt.subplot(1, 3, 2)
plt.plot(x, y2, label="output")
#plt.subplot(1, 3, 3)
plt.plot(x, m, label="cv")
plt.legend(loc="upper left")
plt.show()
