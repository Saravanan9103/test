print("Stone or Paper or Sisccor")
user1=input("Enter Chioce Stone or Paper or Sisccor :\n")
user2=input("Enter Chioce Stone or Paper or Sisccor :\n")
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
        

	

	
	
