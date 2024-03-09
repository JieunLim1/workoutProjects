'''
module for figure generator
functions: generate() : generates the figure based on the web API data
'''
import matplotlib.pyplot as plt
import numpy as np

def generate(data, filename):
    '''generate figure'''
    times = []
    temp = []
    for time in data['time']:
        times.append(time)
    for t in data['temperature_2m']:
        temp.append(t)
    xpoints = np.array(times)
    ypoints = np.array(temp)

    plt.plot(xpoints, ypoints)
    plt.title("Hourly Temperature")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    plt.savefig(filename)
    plt.show()
