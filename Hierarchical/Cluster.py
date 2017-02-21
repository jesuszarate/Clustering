
class Cluster:
    def __init__(self, id=None, x=None, y=None, next=None):
        self.id = float(id)
        self.x = float(x)
        self.y = float(y)
        #self.dist = math.sqrt(x**2 + y**2)
        self.next  = next

    def __str__(self):
        return "id: " + str(self.id) + ", (" + str(self.x) + " , " + str(self.y) + ")"

    # def __cmp__(self, other):
    #     return cmp(self.dist, other.priority)