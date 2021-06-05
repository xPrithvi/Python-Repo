from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.gcf().suptitle("The Ideal Pendulum", fontsize = 16)

X_VALUES = []
Y_VALUES = []

INITIAL_THETA = 0.5
INITIAL_TIME = 0
GRAVITY = 9.81
TIME_STEP = 1/60
LENGTH = 1
INDEX = 0

def function_iteration(i):
    global INITIAL_THETA, INITIAL_TIME, TIME_STEP, LENGTH, GRAVITY, INDEX
    X_VALUE = LENGTH*np.sin(INITIAL_THETA * np.cos(INITIAL_TIME + (INDEX * TIME_STEP)))
    Y_VALUE = LENGTH - (LENGTH*np.cos(INITIAL_THETA * np.cos(INITIAL_TIME + (INDEX * TIME_STEP))))
    INDEX += 1

    plt.cla()
    plt.xlim([-LENGTH, LENGTH])
    plt.ylim([-LENGTH, LENGTH])
    plt.plot([0, X_VALUE], [LENGTH, Y_VALUE], color = "white")
    plt.plot(0, LENGTH, "o", X_VALUE, Y_VALUE, "o", color = "white")
    plt.xlabel("$\Theta_{i} = " + str(INITIAL_THETA) + ",L = " + str(LENGTH) +
                ",t = " + str(INITIAL_TIME + (INDEX * TIME_STEP))[0:3] + "$")

ANIMATION = FuncAnimation(plt.gcf(), function_iteration, frames = 180,  interval = 0)
#ANIMATION.save("PendulumGraphAnimation.mp4", dpi = 300, fps = 60, writer = "ffmpeg")
plt.show()
