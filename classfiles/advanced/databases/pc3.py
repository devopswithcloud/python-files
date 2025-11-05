class MyRange:
    def __init__(self,start,end):
         self.current=start
         self.end =end

    def __iter__(self):
         return self # iterator returns itself
    
    def __next__(self):
         if self.current >=self.end:
          raise StopIteration
         else:
             self.current+=1
             return self.current-1
         
    
for num in MyRange(1,5):
    print(num)
