class rectangle:

    def __init__(self,l,b):
        self.l = l
        self.b = b
    def perimeter(self):
        return 2*(self.l + self.b)
    
r1 = rectangle(3,4)
r1.perimeter