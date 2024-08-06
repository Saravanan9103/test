try:
	list=[4]
	print(type(list))
	i=0
	while i<4:
		list[i]=int(input("Enter The Value"))
		i+=1
	print(list)
except Exception as ex:
	print(ex)
finally:
	print("Passed Err With msg")