import queue as Q

class Cluster:
    # q = Q.PriorityQueue()


    # def __init__(self, id=None, x=None, y=None, next=None):
    #     self.list = []
        # self.id = float(id)
        # self.x = float(x)
        # self.y = float(y)
        # self.next = next

    def __init__(self):
        self.points = []

    def add(self, point):
        self.points.append(point)

    def addAll(self, _points1):
        self.points.extend(_points1)


    def __str__(self):
        s = ""
        for s in self.points:
            s.appent(s + " ")
        return s
        #return "id: " + str(self.id) + ", (" + str(self.x) + " , " + str(self.y) + ")"

        # def __cmp__(self, other):
        #     return cmp(self.dist, other.priority)