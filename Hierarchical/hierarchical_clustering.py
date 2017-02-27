import math
import queue as Q
import MinCluster as node
import point as p


#read Files
def Init2DClusters(path):
    cluster_list = []
    with open(path, 'r') as f:
        for line in f:
            l = line.split()
            n = p.point(l[0], l[1], l[2])
            cluster = node.Cluster()
            cluster.add(n)
            cluster_list.append(cluster)
    return cluster_list

clusters = Init2DClusters("/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/Ce.txt")

k = 2
# q = Q.PriorityQueue()

def distance(x1, x2, y1, y2):
    return math.sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)

def findMinDistance(cluster1, cluster2):
    c1Points = cluster1.points
    c2Points = cluster2.points
    m = distance(c1Points[0].x, c2Points[0].x, c1Points[0].y, c2Points[0].y)
    for c1 in c1Points:
        for c2 in c2Points:
            m = distance(c1.x, c2.x, c1.y, c2.y)
    return m

def getDistances():
    q = Q.PriorityQueue()
    for c1 in clusters:
        for c2 in clusters:
            q.put([findMinDistance(c1 , c2), c1, c2])
    return q

def merge(cluster1, cluster2):
    cluster1.addAll(cluster2.points)

q = getDistances()
while len(clusters) > k:
    #Get the smallest distance and merge the clusters
    closest = q.get()
    merge(closest[1], closest[2])
    clusters.remove(closest[2])

print clusters


