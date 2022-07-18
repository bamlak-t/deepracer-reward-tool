from ast import Param
import numpy as np
import reward_functions as rf
import useful_functions as uf
import matplotlib.pyplot as plt
import math
import params

class Checker:
    def __init__(self, track, reward_function):

        data = np.load('./Track_Info/'+ track + '.npy')
        centerCoords = []
        leftCoords = []
        rightCoords = []

        for row in data:
            centerCoords.append( [row[0], row[1]] )
            leftCoords.append( [row[2], row[3]] )
            rightCoords.append( [row[4], row[5]] )

        self.track = track
        self.centerCoords = np.array(centerCoords)
        self.leftCoords = np.array(leftCoords)
        self.rightCoords = np.array(rightCoords)
        self.reward_function = reward_function

    def check(self):

        checkParams = params.Params()

        # distance between left and right side of the track
        checkParams.setTrackWidth(
            uf.getTwoPointDistance(self.leftCoords[0][0], self.rightCoords[0][0], 
            self.leftCoords[0][1], self.rightCoords[0][1]))

        # total distance between each center coordinate and its next coordinate
        trackLength = 0
        for i in range(len(self.centerCoords)-1):
            cur = self.centerCoords[i]
            next = self.centerCoords[i+1]
            trackLength += uf.getTwoPointDistance(cur[0], next[0], cur[1], next[1])
        checkParams.setTrackLength(trackLength)

        checkParams.setWaypoints(self.centerCoords)

        rewardValues = {}

        xRange = int(max(self.rightCoords[:,0]) * 10) + 5
        yRange = int(max(self.rightCoords[:,1]) * 10) + 5

        for x in range(-xRange, xRange):
            for y in range(-xRange, yRange):
                xTest = x/10
                yTest = y/10

                checkParams.setX(xTest)
                checkParams.sety(yTest)

                diff = math.inf
                steps = 0
                for i, coords in enumerate(self.centerCoords):
                    distance = uf.getTwoPointDistance(
                                    x1 = coords[0], 
                                    x2 = xTest, 
                                    y1 = coords[1], 
                                    y2 = yTest)

                    if distance <= diff:
                        diff = distance
                        steps = i+1

                checkParams.setDistanceFromCenter(diff)

                checkParams.setSteps(steps)

                checkParams.setProgress(steps/len(self.centerCoords))

                checkParams.setIsOffTrack( diff > checkParams.getTrackWidth()/2 )

                checkParams.setAllWheelsOnTrack( checkParams.getIsOffTrack() )

                # set if left of center or not
                leftSideDist = uf.getTwoPointDistance(self.leftCoords[steps-1][0], xTest, self.leftCoords[steps-1][1], yTest)
                rightSideDist = uf.getTwoPointDistance(self.rightCoords[steps-1][0], xTest, self.rightCoords[steps-1][1], yTest)
                if  leftSideDist < rightSideDist:
                    checkParams.setIsLeftOfCenter(True)
                else:
                    checkParams.setIsLeftOfCenter(False)

                # closest points on the track
                if steps < len(self.centerCoords)-1:
                    nextCoord = self.centerCoords[steps]
                else:
                    nextCoord = self.centerCoords[0]
                checkParams.setClosestWaypoints( [self.centerCoords[steps-2], nextCoord] )

                rewardValues[(xTest,yTest)] = self.reward_function(checkParams.getAll())

        return rewardValues

    def plotting(self):
        rewardValues = self.check()

        for coords in rewardValues:
            color = "green"
            if rewardValues[coords] == 1:
                color = "red"
            elif rewardValues[coords] == 0.5:
                color = "yellow"
            elif rewardValues[coords] == 0.5:
                color = "blue"

            plt.plot(coords[0], coords[1], marker="o", markersize=1, markeredgecolor=color, markerfacecolor=color)


        plt.plot(self.centerCoords[:,0], self.centerCoords[:,1], alpha=0.5, color="black")
        plt.plot(self.leftCoords[:,0], self.leftCoords[:,1], alpha=0.5, color="black")
        plt.plot(self.rightCoords[:,0], self.rightCoords[:,1], alpha=0.5, color="black")

        plt.show()

c = Checker('dbro_raceway', rf.progressTest)

c.plotting()