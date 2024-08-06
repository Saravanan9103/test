print("Electricity Bill Calculator")
unit=int(input("\nEnter No Of Units : "))
if(unit>0 and unit<100):
	Charge=0
	print("Electricity Charge =",Charge)
elif(unit>=100 and unit<500):
	Charge=unit*0.50
	print("Electricity Charge =",Charge)
elif(unit>=500 and unit<1000):
	Charge=unit*1.50
	print("Electricity Charge =",Charge)
elif(unit>=1000 and unit<2000):
	Charge=unit*2.00
	print("Electricity Charge =",Charge)
    