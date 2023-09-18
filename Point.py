class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def translateX(self,dx):
        return Point(self.x + dx, self.y)

    def translateY(self,dy):
        return Point(self.x, self.y + dy)

    def addPoint(self,pt):
        return Point(self.x + pt.getX(), self.y + pt.getY())