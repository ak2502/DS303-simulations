import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

n = 1000 #no. of steps

x = np.zeros(n)
y = np.zeros(n)

for i in range(1, n):
	val = random.randint(1, 4)
	if val == 1:
		x[i] = x[i - 1] + 1
		y[i] = y[i - 1]
	elif val == 2:
		x[i] = x[i - 1] - 1
		y[i] = y[i - 1]
	elif val == 3:
		x[i] = x[i - 1]
		y[i] = y[i - 1] + 1
	else:
		x[i] = x[i - 1]
		y[i] = y[i - 1] - 1

#for animation
fig, ax = plt.subplots()
line, = ax.plot([], [])
xdata, ydata = [], []

def data_extract():
    for i in range(len(x)):
        d = x[i],y[i]
        yield d[0], d[1]

def init():
    ax.set_ylim(-40, 40)	#limits of x and y axis (upper and lower bound)
    ax.set_xlim(-40, 40)
    plt.title('2D Random Walk Animation')
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

def animate(data):
    x, y = data
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata,ydata)
    return line,

anim = animation.FuncAnimation(fig, animate, data_extract, init_func=init, interval=0.5, repeat=False)
plt.show()

plt.plot(x,y)
plt.title("2D Random Walk")
plt.show()