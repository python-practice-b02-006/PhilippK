class Vectors():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return(str(self.x) + " " + str(self.y) + " " + str(self.z))
    
    def __add__(self, inst):
        return Vectors(self.x + inst.x, self.y + inst.y, self.z + inst.z)
    
    def __sub__(self, inst):
        return Vectors(self.x - inst.x, self.y - inst.y, self.z - inst.z)
    
    def __mul__(self, k):
        if type(k) is Vectors:
            return(self.x*k.x + self.y*k.y + self.z*k.z)
        else:
            return Vectors(self.x*k, self.y*k, self.z*k)
    
    def __rmul__(self, k):
        if type(k) is Vectors:
            return(self.x*k.x + self.y*k.y + self.z*k.z)
        else:
            return Vectors(self.x*k, self.y*k, self.z*k)
    
    def __abs__(self):
        return((self.x**2 + self.y**2 + self.z**2)**0.5)
    
    def __pow__(self, inst):
        return Vectors(self.y*inst.z - self.z*inst.y, - self.x*inst.z + self.z*inst.x, self.x*inst.y - self.y*inst.x)
