class Cluster:
    def __init__(self, x=None, y=None, next=None):
        self.x = x
        self.y = y
        self.next  = next

    def __str__(self):
        return str(self.x) + " , " + str(self.y);