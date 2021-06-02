from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.tight_layout()

X_VALUES = []
Y_VALUES = []

INITIAL_THETA = 0
STEP_SIZE = (np.pi)/60
RADIUS = 3
INDEX = 0

def function_iteration(i):
    global INITIAL_X, STEP_SIZE, RADIUS, INDEX
    X_VALUES.append(RADIUS*np.sin(INITIAL_THETA + (INDEX * STEP_SIZE)))
    Y_VALUES.append(RADIUS*np.cos(INITIAL_THETA + (INDEX * STEP_SIZE)))
    INDEX += 1

    plt.cla()
    plt.xlim([-RADIUS, RADIUS])
    plt.ylim([-RADIUS, RADIUS])
    plt.plot(X_VALUES, Y_VALUES, "w")
    plt.style.use('dark_background')
    plt.xlabel("$x^2 + y^2 = " + str(RADIUS) + "^2 $")

ANIMATION = FuncAnimation(plt.gcf(), function_iteration, frames = 120,  interval = 0)
ANIMATION.save("DrawingCircleGraphAnimation.mp4", dpi = 300, fps = 60, writer = "ffmpeg")
 #plt.show()
