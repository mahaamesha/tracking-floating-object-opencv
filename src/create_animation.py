import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os
import sys

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 8), ylim=(-4, 4))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

def f(x, i):
    y = np.sin(0.2*np.pi*x - 0.01*np.pi*i)
    return y

# make floating object
def floating_obj(y_value):
    # draw circle
    xc = 4
    yc = y_value
    r = 1/2
    circle = plt.Circle(
        (xc, yc), radius=r,
        fc='gray',
        lw=2
    )
    plt.gca().add_patch(circle)

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 8, 50)
	
    # y for wave equation that move to rigth
    y = f(x, i)
    floating_obj(y_value=y[i])
		
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=True)


isSave = 0
if isSave:
    writergif = animation.PillowWriter(fps=30)
    fpath = "./media/anim.gif"
    try: os.remove(fpath)
    except: pass
    anim.save(fpath, writer=writergif)

plt.show()
sys.exit("Done")