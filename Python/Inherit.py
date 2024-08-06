#Single
class one:#base
    def Func1(self):
        self.a=10
class two(one):
    def Func2(self):
        super().Func1()
        b=20
        c=self.a+b
        print(c)
obj=two()
obj.Func2()



'''
#Multiple
class first:
    def F_one(self):
        self.one=20
        print(self.one)
class second(first):
    def F_two(self):
        super().F_one()
        self.two=30
        print(self.two)
class third(second):
    def F_three(self):
        super().F_two()
        self.three=self.one+self.two
        print(self.three)
o=third()
o.F_three()
'''       
        