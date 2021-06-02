from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

X_VALUES = []
Y_VALUES = []

INITIAL_THETA = 0.5
INITIAL_TIME = 0
TIME_STEP = 0.1
LENGTH = 1
INDEX = 0

def function_iteration(i):
    global INITIAL_THETA, INITIAL_TIME, TIME_STEP, LENGTH, INDEX
    X_VALUE = LENGTH*np.sin(INITIAL_THETA * np.cos(INITIAL_TIME + (INDEX * TIME_STEP)))
    Y_VALUE = LENGTH - (LENGTH*np.cos(INITIAL_THETA * np.cos(INITIAL_TIME + (INDEX * TIME_STEP))))
    INDEX += 1

    plt.cla()
    plt.xlim([-LENGTH, LENGTH])
    plt.ylim([-LENGTH, LENGTH])
    plt.plot([0, X_VALUE], [LENGTH, Y_VALUE], color = "white")
    plt.plot(0, LENGTH, "o", X_VALUE, Y_VALUE, "o", color = "white")
    plt.xlabel("Ideal Pendulum")

ANIMATION = FuncAnimation(plt.gcf(), function_iteration, frames = 720,  interval = 0)
ANIMATION.save("PendulumGraphAnimation.mp4", dpi = 300, fps = 60, writer = "ffmpeg")
plt.show()
