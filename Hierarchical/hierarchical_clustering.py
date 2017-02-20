import queue as Q
import Cluster as node

q = Q.PriorityQueue()
q.put(node.Cluster(2,1,None))
q.put(node.Cluster(1,1,None))
#q.put(1)
#q.put(5)
while not q.empty():
    print q.get(),

