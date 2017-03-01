import Queue as Q
from matplotlib import pyplot

import math

pq = Q.PriorityQueue()



class pnt:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + self.x + "," + self.y + ")"

class distPoint:
    def __init__(self, dist, pnt):
        self.dist = dist
        self.pnt = pnt
    def __cmp__(self, other):
        return cmp(self.dist, other.dist)
    def __hash__(self):
        return hash(self.dist) ^ hash(self.pnt)


class cluster:
    def __init__(self, id):
        self.id = id
        self.distances = {}
        self.points = set()

x = []
y = []
z = []

#read Files
def Init2DClusters(path):
    cluster_list = []
    with open(path, 'r') as f:
        for line in f:
            l = line.split()
            n = pnt(l[0], l[1], l[2])
            x.append(round(float(l[1]), 3))
            y.append(round(float(l[2]), 3))
            z.append(int(l[0]))
            cluster_list.append(n)
    return cluster_list

clusters = Init2DClusters("/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/C1.txt")

def distance(x1, x2, y1, y2):
    return math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)

distances = {}
def Ds():
    for c1 in clusters:
        #print "ID: " + c1.id + "\t"
        clust = cluster(c1.id)
        clust.points.add(c1)
        distances[c1.id] = clust#set()

        for c2 in clusters:
            if c1 == c2:
                pass
                #print "X\t",
            else:
                dist = distance(c1.x, c2.x, c1.y, c2.y)
                dp = dist#distPoint(dist, c2)
                distances[c1.id].distances[c2.id] = dp
                #print str(dist) + "\t",

        print

# First compute the distances
Ds()

# def updateDistance(id1, id2):
#     for d in distances.values():
#         if id1 in d.distances:
#             d.distances.pop(id1)
#         if id2 in d.distances:
#             d.distances.pop(id2)

def updateDistances(point1, point2, newClust, distances):
    for dp in distances.values():
        min = float('inf')#distPoint(float("inf"), None)
        if point1 in dp.distances:
            dp.distances.pop(point1)
        if point2 in dp.distances:
            dp.distances.pop(point2)
        dp.distances[newClust.id] = newClust.distances[dp.id]


def findMin(distances):
    #min = (float("inf"),float("inf"),distPoint(float("inf"), None))
    min = (float("inf"),float("inf"),float("inf"))
    for id, innerSet in distances.items():
        for i, dp in innerSet.distances.items():
            if dp < min[2]: # Min
                min = (id, i, dp)
    return (min[0], min[1])

def findMax(distances):
    max = (-float("inf"),-float("inf"),distPoint(-float("inf"), None))
    for id, innerSet in distances.items():
        for i, dp in innerSet.distances.items():
            if dp > max[2]: # Max
                max = (id, i, dp)
    return (max[0], max[1])

def findMean(distances):
    min = (-float("inf"),float("inf"),distPoint(-float("inf"), None))
    sum = 0
    for id, innerSet in distances.items():
        for i, dp in innerSet.distances.items():
            if dp > min[2]: # Max
                min = (id, i, dp)
    return (min[0], min[1])


def getMin(dist1, dist2):
    return 0.5*(dist1 + dist2 - abs(dist1 - dist2))

def getMax(dist1, dist2):
    return 0.5*(dist1 + dist2 + abs(dist1 - dist2))



# def getMedian(n1, n2, d1, d2):
#     ai = n1 / (n1 + n2)
#     aj = n2 / (n1 + n2)
#     return (ai*d1) + (aj*d2)

def getMedian(dist1, dist2):

    sum = 0
    for id1, d1 in dist1.items():
        sum += d1
    for id2, d2 in dist2.items():
        sum += d2
    tot = len(dist1) + len(dist2)
    return sum/tot

def merge(point1, point2):
    d1 = distances[point1]
    d2 = distances[point2]
    distances.pop(point1)
    distances.pop(point2)

    newClust = cluster(d1.id + "," + d2.id)

    #Remove the distances from eachother
    d1.distances.pop(point2)
    d2.distances.pop(point1)

    for d, dist1 in d1.distances.items():
        min = getMedian(d1.distances, d2.distances)#getMin(dist1, d2.distances[d])
        newClust.distances[d] = min

    updateDistances(point1, point2, newClust, distances) # Update the distances to every other cluster.
    distances[newClust.id] = newClust

def printDistances():
    for d in distances.keys():
        print d + " ",

def singleLink():
    k = 4
    while len(distances) > k:
        #smallestDistPoint = findMin(distances)
        smallestDistPoint = findMin(distances)
        merge(smallestDistPoint[0], smallestDistPoint[1])
        print smallestDistPoint

def completeLink():
    k = 4
    while len(distances) > k:
        maxDistPoint = findMin(distances)
        merge(maxDistPoint[0], maxDistPoint[1])
        print maxDistPoint

def meanLink():
    k = 4
    while len(distances) > k:
        maxDistPoint = findMean(distances)
        merge(maxDistPoint[0], maxDistPoint[1])
        print maxDistPoint

# Compute complete link clustering
completeLink()

printDistances()



pyplot.scatter(x, y)

fig = pyplot.figure()
ax = fig.add_subplot(111)

A = x
B = y
C = z

pyplot.scatter(A,B)
for xyz in zip(A, B, C):
    ax.annotate('(%s)' % xyz[2], xy=(xyz[0], xyz[1]), textcoords='data')

pyplot.grid()
pyplot.show()