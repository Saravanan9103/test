class library:
    def __init__(self,b):
        self.books=b #["python", "java","c","c++"]
       
    def list_book(self):
        print ("available book")
        for i in self.books:
            print(i)
            
    def bor_book(self,borrow) :#borrow=book
        if borrow in self.books:
            print ("get your book now")
            self.books.remove (borrow)
        else:
            print ("book not available")
                
    def rec_book(self,recive):#recive=book
        print ("you have return book")
        self.books.append(recive)#append add in last place (With Older Records)

x=["python", "java","c","c++"]
o=library(x)

msg="""1.display
2.borrow book
3.Return book"""
while True:
    print (msg)
    ch=int (input ("enter the choice: "))
    if ch == 1:
        o.list_book ()
        #break
    elif ch == 2:
        book=input ("enter the book name: ")
        o.bor_book (book)
    elif ch == 3:
        book=input ("enter the return book name: ")
        o.rec_book (book)
    else:
        print ("Thank you come again ")
        quit ()
        
    
        