class size:
    def ds():
        height=20
        width=10
        padding=5
        print("Size Is",height," ",width," ",padding)
        
size.ds() # 20 10 5

obj1=size()
obj1.height=40
obj1.width=10
obj1.padding=5 
print(obj1.ds())