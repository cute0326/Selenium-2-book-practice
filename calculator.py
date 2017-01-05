__author__ = 'lenovo'

class Count:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
        self.c = 0

    def add(self):
        return self.a +  self.b

    def sub(self):
        return self.a - self.b

if __name__ == '__main__':
    c = Count(2,3)
    print('the result is',c.add())
