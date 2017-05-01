import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd


# generate 4 random variables from the random, gamma, exponential, and uniform distributions
b = 20
n = 1000
x1 = np.random.normal(0, 1, n)
x2 = np.random.gamma(2, 1.5, n)
x3 = np.random.exponential(2, n)
x4 = np.random.uniform(0,10, n)


# plot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(9,9))


# create the function that will do the plotting, where curr is the current frame
def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr*10 == n: 
        a.event_source.stop()

    plt.subplot(2, 2, 1)
    plt.cla()
    plt.hist(x1[100:curr*10], bins=b, color="blue", alpha=0.5)
    plt.axis([-4,4,0,300])
    plt.gca().set_title('Sampling the Normal Distribution', fontsize=10)
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr*10), [2,250])
    
    plt.subplot(2, 2, 2) 
    plt.cla()
    plt.hist(x2[100:curr*10], bins=b, color="orange", alpha=0.5)
    plt.axis([0,15,0,300])
    plt.gca().set_title('Sampling the Gamma Distribution', fontsize=10)
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr*10), [10,250])
    
    plt.subplot(2, 2, 3) 
    plt.cla()
    plt.hist(x3[100:curr*10], bins=b, color="green", alpha=0.5)
    plt.axis([0,15,0,300])
    plt.gca().set_title('Sampling the Exponential Distribution', fontsize=10)
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr*10), [10,250])
    
    plt.subplot(2, 2, 4) 
    plt.cla()
    plt.hist(x4[100:curr*10], bins=b, color="red", alpha=0.5)
    plt.axis([0,15,0,300])
    plt.gca().set_title('Sampling the Uniform Distribution', fontsize=10)
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n = {}'.format(curr*10), [10,250])

    
a = animation.FuncAnimation(fig, update, interval=10)




