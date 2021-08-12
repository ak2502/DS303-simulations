from scipy import random
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 1
n =2000
A=[] #array to store ans

def f(x):
    return (-65536*x**8 + 262144*x**7 - 409600*x**6 + 311296*x**5 - 114688*x**4 + 16384*x**3)/27

#Plot for showing that f(x) is fully contained in a unit square
for i in range(1000):
    plt.scatter(i/1000,f(i/1000),c='yellow')

plt.axhline(y=0, c='r')
plt.axhline(y=1, c='r')
plt.axvline(x=0, c='r')
plt.axvline(x=1, c='r')
plt.xlabel("X")
plt.ylabel("Y = f(X)")
plt.title("Plot showing that f(x) is fully contained in a unit square")
plt.show()

plt.title("Monte Carlo Estimate of Integral")
for i in range(1,n+1):
    arr = np.zeros(i)

    for j in range(len(arr)):
        arr[j] = random.uniform(a, b)

    integral = 0.0

    for j in arr:
        integral += f(j)
    
    ans = (b-a)/float(i)*integral
    A.append(ans)

    if i%10==0:          
        # for plotting
        plt.scatter(i,ans,c='r')
        plt.xlabel("No. of samples")
        plt.ylabel("Estimate of integral")
        plt.pause(0.1) #for animation

print("The estimate of integration is ",ans)
mu = np.mean(A)
sig = np.std(A)
print("Confidence Interval : (",mu-1.645*sig/n,",",mu+1.645*sig/n,")" )
plt.show()