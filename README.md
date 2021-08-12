# DS303-simulations

## Q1-Finding value of π using Monte Carlo Method
Using Monte Carlo method, I took a square from x=-1 to x=+1 and y=-1 to y=+1 and inscribed a
circle of radius 1 unit inside the square. Now, I randomly started dropping points inside square. We can
say that the number of points falling inside the circle (nIn) divided by the total no. of points dropped
on the square (n) is given by Area of circle divided by Area of square. So value of πis :
π = 4 ∗ (nIn/n). 
Reference - https://www.bragitoff.com/2021/05/value−of−pi−using−monte−carlo/

## Q2-Monte Carlo estimate of given integral
To estimate the integral, Random draws X_j are made over X_i following a uniform distribution. Then I computed the sum of f(X_i), multiplied it by (b-a) and divided by the number of samples i. This is basically the Monte Carlo Estimate of Integral. Here, I varied i from 1 to n to show convergence as n increases.
Reference - https://towardsdatascience.com/the-basics-of-monte-carlo-integration-5fe16b40482d




  
