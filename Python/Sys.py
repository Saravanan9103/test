import random
lst=["Stone","Paper","Sisccor"]
user1=random.choice(lst)

print("\t\t\t\t\tStone Paper Sisccor")
'''user1=input("Enter Chioce Stone or Paper or Sisccor :")'''
user2=input("Enter Chioce Stone or Paper or Sisccor :")
print(user1,"vs",user2)

if (user1==user2):
	print("Match Draw")
else:
    if(user1=="Stone" and user2=="Paper"):
        print("user2 Is Win",user2)
        
    elif(user1=="Paper" and user2=="Stone"):
        print("user1 Is Win",user1)
        
    elif(user1=="Stone" and user2=="Sisccor"):
        print("user2 Is Win",user2)
        
    elif(user1=="Sisccor" and user2=="Stone"):
        print("user1 Is Win",user1)
        
    elif(user1=="Paper" and user2=="Sisccor"):
        print("user2 Is Win",user2)
        
    elif((user1=="Sisccor" and user2=="Stone")):
        print("user1 Is Win",user1)
        

	
