'''#Syntax For Function
    def Func_Name():
        Attributes #variables
        Return Statement or print statement
        
        
#Syntax For Calling Function
    Func_Name() => Without Return
    print(Func_Name) => With Return

#Syntax For No Argument Without Return
    def Func_Name():
        v.name=values
        print(v.name)
 
#Syntax For Argument Without Return
    def Func_Name(argument1,argument2,...):
        print(argument_name)

#Syntax For No Argument With Return
    def Func_Name():
        v.name=values
        return v.name
 
#Syntax For Argument With Return
    def Func_Name(argument1,argument2,...):
        return argument1,argument2
'''
#Examples
def Func1():
	a=10
	b=20
	print("Total=",a+b)
	#print("Func1","No Argument without Return")
	
	
def Func2():
	a=10
	b=20
	return ("a-b Is :",a-b ,"Func2 No Argument with Return")

	
	
def Func3(a):
	b=20
	print("Total=",a*b)
	#print("Func3","Argument without Return")
	
def Func4(a):
	b=20
	return "a/b Is :",a/b,"Func4","Argument with Return"
    
Func1() #Calling Function 1
print(Func2()) #Calling Function 2
Func3(10) #Calling Function 3
print(Func4(10)) #Calling Function 4