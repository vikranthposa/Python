class PowTwo:
    def __init__(self,maxV):
        self.max = maxV
    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        if(self.x <= self.max):
            temp = 2**self.x
            self.x += 1
            return temp
        else:
            raise StopIteration

a = PowTwo(3)
pob = iter(a)
print(next(pob))
print(next(pob))
print(next(pob))
print(next(pob))
print(next(pob))
print(next(pob))
