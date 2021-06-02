from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.tight_layout()

X_VALUES = []
Y_VALUES = []

INITIAL_X = 0
STEP_SIZE = (np.pi)/45
INDEX = 0

def function_iteration(i):
    global INITIAL_X, STEP_SIZE, INDEX
    X_VALUES.append(INITIAL_X + (INDEX * STEP_SIZE))
    Y_VALUES.append(np.exp(-0.25 * X_VALUES[INDEX] ) * np.sin(X_VALUES[INDEX]))
    INDEX += 1

    plt.cla()
    plt.xlim([0, 4*np.pi])
    plt.ylim([-1.01, 1.01])
    plt.plot(X_VALUES, Y_VALUES, "w")
    plt.style.use('dark_background')
    plt.xlabel('$x$')
    plt.ylabel('$y = e^{-0.25x}sin(x)$')

ANIMATION = FuncAnimation(plt.gcf(), function_iteration, frames = 180,  interval = 0)
ANIMATION.save("BasicGraphAnimation.mp4", dpi = 300, fps = 60, writer = "ffmpeg")
