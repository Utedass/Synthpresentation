import matplotlib.pyplot as plt
import numpy as np

def sine(x, frec, phase = 0, amplitude = 2, offset = 0):
    rad = x * (2*np.pi*frec)
    y = amplitude/2 * np.sin(rad + phase/360*2*np.pi) + offset
    return y

def saw(x, frec, amplitude = 2, offset = 0):
    period = 1/frec
    y = amplitude * (x / period - np.floor(x/period + 1/2)) + offset 
    return y

def triangle(x, frec, amplitude = 2, offset = 0):
    period = 1/frec
    y = amplitude * (2 * np.abs(x / period - np.floor(x/period + 1/2))) - amplitude/2 + offset
    return y

def pwm(x, frec, pwm = 0.5, amplitude = 2, offset = 0):
    period = 1/frec
    y = amplitude * (np.floor(x / period) - np.floor(x/period - pwm)) - amplitude/2 + offset
    return y

def vca(i, cv, depth):
    y = i * (1-depth + depth*cv)
    return y

x = np.linspace(0, 3, 2000)

freq = 2

mod = x / 5 + 0.25

a = sine(x, freq, amplitude=0.9, offset = 3)
b = triangle(x,freq, amplitude=0.9, offset = 2)
c = saw(x, freq, amplitude=0.9, offset = 1)
d = pwm(x, freq, amplitude=0.9, offset = 0, pwm = mod)

plt.plot(x, a)
plt.plot(x, b)
plt.plot(x, c)
plt.plot(x, d)

ax = plt.gca()
ax.set_facecolor('#fff8e2')

plt.show()
