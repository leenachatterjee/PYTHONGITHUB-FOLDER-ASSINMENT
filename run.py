class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop

    def __iter__(self): 
        return self

    def __next__(self): # next in Python 2
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current


iterator = Squares(7, 8)
