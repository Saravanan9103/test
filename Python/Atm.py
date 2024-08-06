class Bank:
	def __init__(self,b):
		self.bal=b
	def avl_bal(self):
		print(self.bal)
	def credit(self,cramt):
		self.bal+=cramt
		print("Amount",cramt,"credited in your account Successfully","Balance is:",self.bal)
	def debit(self,dbamt):
		if self.bal<=500 or self.bal<dbamt:
			print("Insufficent Balance,Transaction Failed")
		else:
            print("suce")	
obj=Bank(500)

msg="""1.Display Balance
2.Deposit
3.Withdrawal
"""

while True:
	print(msg)
	ch=int(input("Enter The Choice : "))
	if ch==1:
		obj.avl_bal()
	elif ch==2:
		amt=int(input("Enter The Amount : "))
		obj.credit(amt)
	elif ch==3:
		amt=int(input("Enter The Amount : "))
		obj.debit(amt)
	else:
		print("Thank you!")
		quit()
