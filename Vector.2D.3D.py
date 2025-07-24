a1 = int(input("enter the number for 2d vector for i: "))
a2 = int(input("enter the number for 2d vector for j: "))
a3 = int(input("enter the number for 3d vector for i: "))
a4 = int(input("enter the number for 3d vector for j: "))
a5 = int(input("enter the number for 3d vector for k: "))


class twovector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"the vector sum is {self.i}i + {self.j}j")

class threevector(twovector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):    
        print(f"the vector sum is {self.i}i + {self.j}j + {self.k}k")

a = twovector(a1, a2)
a.show()
b = threevector(a3, a4, a5)
b.show()
#code by salman
#github  = numaan28
        
