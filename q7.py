import numpy as np
import matplotlib.pyplot as plt

def bivarNorm(cov):
	#taking mean as [0,0] and cov according to question
	x,y = np.random.multivariate_normal([0,0], cov, size=100000).T
	return x,y

plt.title("Scatter Plot for part(a)")
x,y=bivarNorm([[10,0],[0,10]]) #cov = c*I
plt.scatter(x,y,c='c')
plt.axis("equal")
plt.show()
print("a) When covariance matrix is of the form c*I, the scatter plot is uniformly and evenly distributed around the origin and it almost forms a circle with radius c. This is because the diagonal elements are equal")

plt.title("Scatter Plot for part(b)")
x,y=bivarNorm([[1,0],[0,2]]) #cov = diag(a1,a2)
plt.scatter(x,y,c='c')
plt.axis("equal")
plt.show()
print("b) When covariance matrix is of the form diag(a1,a2), the scatter plot is also uniformly distributed along both axis but here it forms an ellipse with its axes parallel to x and y axis. This is because the diagonal elements are different.")

#cov = A (symmetric) 
figure, axis = plt.subplots(3, 2)
figure.suptitle("Scatter Plot for part(c)")

x,y=bivarNorm([[1,0.5],[0.5,1]]) #off diagonal entries 0.5
axis[0, 0].scatter(x, y,c='r')
axis[0, 0].set_title("off diagonal entries 0.5")

x,y=bivarNorm([[1,-0.5],[-0.5,1]]) #off diagonal entries -0.5 
axis[0, 1].scatter(x, y,c='r')
axis[0, 1].set_title("off diagonal entries -0.5")

x,y=bivarNorm([[1,2],[2,1]]) #off diagonal entries 2
axis[1, 0].scatter(x, y,c='b')
axis[1, 0].set_title("off diagonal entries 2")

x,y=bivarNorm([[1,-2],[-2,1]]) #off diagonal entries -2
axis[1, 1].scatter(x, y,c='b')
axis[1, 1].set_title("off diagonal entries -2")

x,y=bivarNorm([[1,10],[10,1]]) #off diagonal entries 10
axis[2, 0].scatter(x, y,c='g')
axis[2, 0].set_title("off diagonal entries 10")

x,y=bivarNorm([[1,-10],[-10,1]]) #off diagonal entries -10
axis[2, 1].scatter(x, y,c='g')
axis[2, 1].set_title("off diagonal entries -10")

print("c) When the off diagonal elements are not zero, we can see that the plots with diagonal entries as +0.5,+2 and +10 fall along a line with positive slope and the ones having off diagonal elements as -0.5,-2,-10 fall along a line with negative slope. The range of values in plot increases with increase in magnitude of off-diagonal elements. ")
plt.axis("equal")
plt.show()

print("\n From the above 3 plots, we can conclude that when the off diagonal elements of covariance matrix are 0, then we generate uncorrelated data and when they are non-zero, then the data is positively or negatively correlated depending on the off diagonal elements")
print("These insights are also applicable to other distributions as covariance matrix helps to determine correlation between data.")


