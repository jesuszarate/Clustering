import math
import queue as Q
import Cluster as node

# q = Q.PriorityQueue()
# q.put(node.Cluster(2,1,None))
# q.put(node.Cluster(1,1,None))
# #q.put(1)
# #q.put(5)
# while not q.empty():
#     print q.get(),

#read Files
def Init2DClusters(path):
    cluster_list = []
    with open(path, 'r') as f:
        for line in f:
            l = line.split()
            n = node.Cluster(l[0], l[1], l[2], None)
            cluster_list.append(n)

    return cluster_list

clusters = Init2DClusters("/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/C1.txt")

k = 7
q = Q.PriorityQueue()

def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def getDistances(queue, clusters):
    for i in range(len(clusters)):
        curClust = clusters[i]
        for j in range(i, len(clusters)):
            clust = clusters[j]
            dist = distance(curClust.x, clust.x, curClust.y, clust.y)
            queue.put([dist, curClust, clust])
    return queue

# while len(clusters) > k:
#     getDistances(q, clusters)

#getDistances(q, clusters)
c1 = clusters[0]
c2 = clusters[2]

dist = distance(c1.x, c2.x, c1.y, c2.y)
q.put([dist, c1, c2])

c1 = clusters[0]
c2 = clusters[1]
dist = distance(c1.x, c2.x, c1.y, c2.y)
q.put([dist, c1, c2])

while not q.empty():
    print q.get(),

#Initialize the clusters

