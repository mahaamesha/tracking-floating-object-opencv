import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os   # to get path
import shutil   # to move file.gif

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 8), ylim=(-5, 5))
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
    r = 1
    circle = plt.Circle(
        (xc, yc), radius=r,
        fc='#ccf',
        lw=2, ls='dashed', color='k'
    )
    plt.gca().add_patch(circle)

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 8, 1000)
	
    # y for wave equation that move to rigth
    y = f(x, i)
    #floating_obj(y_value=0)
		
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#plt.show()


# lines above this line is the original code from Jake Vanderplas
# url https://jakevdp.github.io/downloads/code/basic_animation.py



# modification from Sparisoma Viridi 2022-03-29
option = 1

if option == 0:
    writergif = animation.PillowWriter(fps=60)
    f_name = "anim.gif"
    anim.save(f_name, writer=writergif)
else:
	plt.show()

# move gif file in workspace_folder to this current_folder
src_path = os.path.dirname(__file__)
dst_path = os.path.join(src_path, "../media/anim.gif")
shutil.move(src_path, dst_path)