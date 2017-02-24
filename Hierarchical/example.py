import Queue as Q
import heapq

import math

pq = Q.PriorityQueue()



class pnt:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        #self.dist = dist

    def __str__(self):
        return "(" + self.x + "," + self.y + ")"

    # def __cmp__(self, other):
    #     return cmp(self.dist, other.dist)
    # def __str__(self):
    #     return "(" + self.id + ", " + str(self.dist) + ")"

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

#read Files
def Init2DClusters(path):
    cluster_list = []
    with open(path, 'r') as f:
        for line in f:
            l = line.split()
            n = pnt(l[0], l[1], l[2])
            cluster_list.append(n)
    return cluster_list

clusters = Init2DClusters("/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/Ce.txt")

def distance(x1, x2, y1, y2):
    return math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)

distances = {}
def Ds():
    for c1 in clusters:
        print "ID: " + c1.id + "\t"
        clust = cluster(c1.id)
        clust.points.add(c1)
        distances[c1.id] = clust#set()

        for c2 in clusters:
            if c1 == c2:
                print "X\t",
            else:
                dist = distance(c1.x, c2.x, c1.y, c2.y)
                dp = distPoint(dist, c2)
                distances[c1.id].distances[c2.id] = dp
                print str(dist) + "\t",

        print

Ds()


def updateDistances(newClust, distances):

    for dp in distances.values():
        min = distPoint(float("inf"), None)
        for point in newClust.points:
            if point.id in dp.distances:
                d = dp.distances[point.id]
                if min > d:
                    min = dp.distances[point.id]
                dp.distances.pop(point.id)
        dp.distances[newClust.id] = min
        newClust.distances[dp.id] = min



print distances


def findMin(distances):
    min = (float("inf"),float("inf"),distPoint(float("inf"), None))
    for id, innerSet in distances.items():
        for i, dp in innerSet.distances.items():
            if dp < min[2]:
                #min = (id, dp.pnt.id, dp)
                min = (id, i, dp)
    return (min[0], min[1])

smallestDistPoint = findMin(distances)


def merge(point1, point2):
    d1 = distances[point1]
    d2 = distances[point2]
    distances.pop(point1)
    distances.pop(point2)

    newClust = cluster(d1.id + "," + d2.id)
    newClust.points.update(d1.points)
    newClust.points.update(d2.points)
    updateDistances(newClust, distances)
    distances[newClust.id] = newClust
    print d1, d2


merge(smallestDistPoint[0], smallestDistPoint[1])

smallestDistPoint = findMin(distances)

print smallestDistPoint

merge(smallestDistPoint[0], smallestDistPoint[1])

print distances

