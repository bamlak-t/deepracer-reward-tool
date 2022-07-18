from ast import Param
import numpy as np
import reward_functions as rf
import useful_functions as uf
import math
import params

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

        checkParams = params.Params()

        xRange, yRange = checkParams.getMaxXYRange()

        rewardValues = {}

        for x in range(-xRange, xRange):
            for y in range(-xRange, yRange):
                xTest = x/10
                yTest = y/10

                checkParams.setx(xTest)
                checkParams.sety(yTest)

                diff = math.inf
                for coords in self.centerCoords:
                    distance = uf.getTwoPointDistance(coords[0], xTest, coords[1], yTest)
                    if distance < diff:
                        diff = distance

                checkParams.setDistanceFromCenter(diff)

                rewardValues[(x,y)] = self.reward_function(checkParams)


        reward = self.reward_function(params)
        return reward

c = Checker('dbro_raceway', rf.default)