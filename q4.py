import numpy as np
import scipy.stats as st
from scipy.integrate import quad

def integrand(x,p):
    return 1/2*np.exp(-abs(x))*(x**p)

def integral(p):    #actual value for E[X],E[X^2],E[X^5]
    return quad(integrand,-np.inf,np.inf,args=(p))[0]

def ImportSamp(p):
    for n in [100,500,1000]:
        z = np.random.normal(0, 2, n)   #based on g(x)
        mu=[]
        for i in range(n):
            weight=(np.exp(-abs(z[i]))/2)/(np.exp(-(z[i]**2)/8)/(np.pi*8)**0.5)     #p(x)/g(x)
            mu.append(weight*(z[i]**p))

        e=sum(mu)/n
        err=abs(e-integral(p))
        print("->Estimate of E[X^{}] for N = {} is {}".format(p,n,e))
        print("Error in Estimate of E[X^{}] for N = {} is {}".format(p,n,err))
    print()

ImportSamp(1)   #for E[X]
ImportSamp(2)   #for E[X^2]
ImportSamp(5)   #for E[X^5]
