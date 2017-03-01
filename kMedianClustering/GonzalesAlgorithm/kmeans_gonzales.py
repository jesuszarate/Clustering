import math

from matplotlib import pyplot


class pnt:
    def __init__(self, id, x, y, centerInd):
        self.id = id
        self.x = x
        self.y = y
        self.centerInd = centerInd

    def __str__(self):
        return "(" + self.x + "," + self.y + ")"


points = []
centers = []
distances = []

def distance(pnt1, pnt2):
    x1 = pnt1.x
    x2 = pnt2.x
    y1 = pnt1.y
    y2 = pnt2.y
    return math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)

def Init2DClusters(path):
    cluster_list = []
    center = None
    gotCenter = False
    with open(path, 'r') as f:
        for line in f:
            l = line.split()
            if not gotCenter:
                center = pnt(l[0], l[1], l[2], l[0])
                gotCenter = True

            point = pnt(l[0], l[1], l[2], 1)
            points.append(point)
            centers.append(center)
            dist = distance(center, point)
            distances.append(dist)

    return cluster_list

clusters = Init2DClusters("/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/C2.txt")

'''
Choose c1 in X arbitrarily, and set phe[j] = 1 for all j in [n]
for i = 2 to k:
    M = 0
    ci = x1
    for j = 1 to n:
        if d(xj , Cphe[j]) > M:
            M = d(xj , Cphe[j])
            ci = xj
    for j = 1 to n:
        if d(xj , Cphe[j]) > d(xj , ci):
            phe[j] = i
'''


k = 3
n = len(points)
C = set()
C.add(points[0].id)

# Represents the centers
for i in range(1, k):
    M = 0
    ci = points[0]

    for j in range(0, n):
        if distance(points[j], centers[j]) > M:
            M = distance(points[j], centers[j])
            ci = points[j]

    for j in range(0, n):
        if distance(points[j], centers[j]) > distance(points[j], ci):
            centers[j] = ci
            C.add(ci.id)


def showClusterPlot():
    clusterX1 = []
    clusterY1 = []
    clusterX2 = []
    clusterY2 = []
    clusterX3 = []
    clusterY3 = []
    for i in range(0, n):
        if centers[i].id == '1':
            clusterX1.append(points[i].x)
            clusterY1.append(points[i].y)
        elif centers[i].id == '534':
            clusterX2.append(points[i].x)
            clusterY2.append(points[i].y)
        elif centers[i].id == '1004':
            clusterX3.append(points[i].x)
            clusterY3.append(points[i].y)

    pyplot.scatter(clusterX1, clusterY1, c='red')
    pyplot.scatter(clusterX2, clusterY2, c='blue')
    pyplot.scatter(clusterX3, clusterY3, c='green')
    pyplot.show()


def get3MeanCost():
    dict = {}
    counts = {}
    for c in C:
        dict[c] = 0
        counts[c] = 0
    for i in range(0, n):
        #print distance(centers[j], points[j])
        #print str(centers[j]) + " " + str(points[j])
        dict[centers[i].id] += distance(centers[i], points[i])
        counts[centers[i].id] += 1

    for id, val in dict.items():
        print id + " : " + str(math.sqrt((val**2)/(counts[id])))
    print dict

get3MeanCost()