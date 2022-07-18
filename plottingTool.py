import matplotlib.pyplot as plt
import numpy as np

while True:
    centerCoords = np.genfromtxt('coords.csv', delimiter=',')
    racing = np.genfromtxt('racingLineCoords.csv', delimiter=',')

    total = racing + centerCoords

    plt.plot(centerCoords[:,0], centerCoords[:,1], 'o')
    plt.plot(total[:,0], total[:,1], 'o')

    plt.show()