class Rectangle:
    def __init__(self,width=1,height=1):
        self.width=width
        self.height=height
    def Area(self):
        return self.width*self.height
    def getRec(self):
        self.width=int(input())
        self.height=int(input())