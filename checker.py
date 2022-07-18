import numpy as np
import reward_functions as rf

class Checker:
    def __init__(self, track, reward_function):

        data = np.load('./'+ track + '.npy')
        centerCoords = []
        leftCoords = []
        rightCoords = []

        for row in data:
            centerCoords.append( [row[0], row[1]] )
            leftCoords.append( [row[2], row[3]] )
            rightCoords.append( [row[4], row[5]] )

        self.track = track
        self.centerCoords = centerCoords
        self.leftCoords = leftCoords
        self.rightCoords = rightCoords
        self.reward_function = reward_function

    def check(self, params):
        reward = self.reward_function(params)
        return reward

c = Checker('dbro_raceway', rf.default)