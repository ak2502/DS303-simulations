import numpy as np
from matplotlib import pyplot as plt

U = np.random.uniform(0, 1, 1000)
X = (-3 + (9 + 160*U)**0.5)/2  #inverse of F(x) (i.e. inverse of cumulative of f(x))
plt.hist(X,bins=50,color="c",label="Drawn samples")

x=np.linspace(0,5,1000)
plt.plot(x,(2*x+3)/40,c='b',label='Given density function')
plt.legend()
plt.xlabel("Value of generated R.V.")
plt.ylabel("Frequency")
plt.title("Histogram of the drawn samples")
plt.show()
