'''try:
    a=10/0
    print(a)
except Exception as e:
    print(e)'''
    
try:
    f=open("Arr.py")
except FileNotFoundError:
    print("File not Found")
else:
    print(f.read())
