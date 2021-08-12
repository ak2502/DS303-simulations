import numpy as np
import matplotlib.pyplot as plt
   
nTot = 3000  #no, of samples
r = 1           #radius of circle
nIn = 0         #no. of points inside the circle
n = 0           #total no. of points
pi = []         #array to store pi value
n_arr = []      #array to stor no. of points dropped
 
#Generating points in a square of side 2 units
X = np.random.default_rng().uniform(-1, 1, (nTot,))
Y = np.random.default_rng().uniform(-1, 1, (nTot,))

plt.title("Monte Carlo Estimate of π")
# Begin Monte Carlo
for i in range(nTot):
    x = X[i]
    y = Y[i]
    n += 1
    
    if x**2+y**2<=r**2: # Check if the points are inside the circle or not
        nIn += 1
    
    area = 4*nIn/n
    pi.append(area)
    n_arr.append(n)
    # plot only at some values
    
    if i%100==0:          
        # for plotting
        plt.axhline(y=np.pi, c='b')
        plt.plot(n_arr,pi,c='r')
        plt.xlabel("No. of samples")
        plt.ylabel("Estimate of π")
        plt.title('π estimate vs no. of points dropped')
        plt.annotate('π',[0,np.pi],fontsize=20)
        plt.pause(0.1) #for animation
                  
print("Final estimated value of π: ",4*nIn/nTot)
#90% confidence interval
mu = np.mean(pi)
sig = np.std(pi)
print("Confidence Interval : (",mu-1.645*sig/n,",",mu+1.645*sig/n,")" )

plt.show()