def getTwoPointDistance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def getAllDistance(data):
    total = 0
    for i in range(len(data)-1):
        x1 = data[i][2]
        y1 = data[i][3]

        x2 = data[i+1][2]
        y2 = data[i+1][3]

        total += getTwoPointDistance(x1,x2,y1,y2)
    return total

# TODO get max x and y range from data
def getMaxXYRange():
    return 65, 45
