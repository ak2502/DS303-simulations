import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2/2)/(np.pi*2)**0.5

def g(x):
    return 1/(np.pi*(1+x**2))

x = np.arange(-25, 25)
m = max(f(x)/g(x))

print("Smallest value of M = ",m)
plt.plot(x, f(x),label="target distribution")
plt.plot(x, g(x),label="proposal distribution")
plt.plot(x, m*g(x),label="scale proposal distribution")
plt.legend()
plt.title("Histogram of selected random samples updating with no. of iterations")
samples = []
for i in range(1,10000):
    z = np.random.normal(0, 1)
    u = np.random.uniform(0, m*g(z))

    if u <= f(z):
        samples.append(z)

    if i%500==0:    #plotting only for some values to reduce runtime
        plt.hist(samples,50, density=1)
        plt.pause(0.1)

plt.show()