import pytest
from Point import Point

class TestPointT:
    @classmethod
    def setup_class(self):
        self.pointA = Point(2,3)
        self.pointB = Point(-4,6)

    def testGetX(self):
        assert self.pointA.getX() == 2
        assert self.pointB.getX() == -4

    def testGetY(self):
        assert self.pointA.getY() == 3
        assert self.pointB.getY() == 6

    def testTranslateX1(self):
        pointAnew = self.pointA.translateX(-2)
        assert pointAnew.getX() == 0

    def testTranslateX2(self):
        pointAnew = self.pointB.translateX(5)
        assert pointAnew.getX() == 1

    def testTranslateY1(self):
        pointAnew = self.pointA.translateY(-2)
        assert pointAnew.getY() == 1

    def testTranslateY2(self):
        pointAnew = self.pointB.translateY(5)
        assert pointAnew.getY() == 11

    def testAddPoint(self):
        pointNew = self.pointA.addPoint(self.pointB)
        assert pointNew.getX() == -2
        assert pointNew.getY() == 9

    