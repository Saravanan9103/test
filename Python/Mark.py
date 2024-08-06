class mark:
    def __init__(self,n,m1,m2,m3):
        self.name=n
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def total(self):
        total=self.mark1+self.mark2+self.mark3
        avg=total/3
        print("Student Mark List")
        print("Name: ",self.name)
        print("Mark1: ",self.mark1)
        print("Mark2: ",self.mark2)
        print("Mark3: ",self.mark3)
        print("Total: ",total)
        print("Average: ",avg)
o=mark("Saravanan",80,80,40)
o.total()