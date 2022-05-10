##class bike:
##    def __init__(self):
##       self.num1=4
##       self.num2=3
##redbike=bike()
##sum=redbike.num1+redbike.num2
##print(sum)




##class bike:
##    def __init__(self,a,b):
##        self.num1=a
##        self.num2=b
##
##    def add(self):
##        sum=self.num1+self.num2
##        print(sum)
##        print(self.num1,self.num2)
##redbike=bike(1,2)
##redbike.add()

##class bankaccount:
##    def __init__(self,n,an,tb):
##        self.name=n
##        self.accountnum=an
##        self.total=tb
##    def bank(self):
##        print(self.name,self.accountnum,self.total)
##    def deposit(self,amount):
##        self.total=amount+self.total
##        print('now your balance is',self.total)
##    def withdraw(self,amount):
##        if amount>self.total:
##            print("you can't do that")
##        else:
##            self.total=self.total-amount
##        print('now your balance is',self.total)          
##account1=bankaccount('a',2389,0)
##account1.bank()
##account2=bankaccount('b',2345,3214323)
##account2.bank()
##class shoppinglist:
##    def __init__(self,shopname):
##        self.shopname=shopname
##        self.shoppingcart={}
##    def additem(self,item,quantity):
##        if item in self.shoppingcart:
##            oldquantity=self.shoppingcart[item]
##            self.shoppingcart[item]=quantity+oldquantity
##            print(self.shoppingcart)
##        else:
##            self.shoppingcart[item]=quantity
##            print(self.shoppingcart)
##    def removeitem(self,item,quantity):
##        if self.shoppingcart[item]==1:
##            del(self.shoppingcart[item])
##            print(self.shoppingcart)
##        else:
##            oldquantity=self.shoppingcart[item]
##            self.shoppingcart[item]=oldquantity-quantity
##            print(self.shoppingcart)
##shoppingcart1=shoppinglist('target')
##shoppingcart1.additem('a',56)
##shoppingcart1.additem('b',55)
##shoppingcart1.additem('c',54)
##shoppingcart1.additem('d',57)
##shoppingcart1.additem('e',59)
##shoppingcart1.additem('f',1)
