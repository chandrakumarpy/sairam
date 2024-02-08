ram = 'ayodya'

class chandu:
    
    happy = 'this is happy mood' #class or static variable
    
    def __init__(self,sal1,sal2) -> None:
        self.sal1 = sal1 #instance variable
        self.sal2 = sal2
        
    def job1(self): #instant method
        print("this is my sal of first job",self.sal1)
        
    @classmethod
    def job2(cls): #class method
        print("getting the salary ",cls.happy)
        
    @staticmethod
    def job3(): #static method
        print('am contributing somthing',ram)
        
class gomathi(chandu):
    
    def __init__(self, sal1, sal2, sal3, sal4) -> None:
        super().__init__(sal1, sal2)
        self.sal3 = sal3 
        self.sal4 = sal4
        
    def fjob1(self):
        super().job2()
        print("my salary and my chandu salary\n", self.sal1+self.sal2, self.sal3+self.sal4)
        
a = chandu(20000,400000)
b=gomathi(20000,40000,80000,90000)
b.fjob1()
        
        
        