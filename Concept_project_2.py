from random import *
class Book:
    def __init__(self,name,id,category,quantity):
        self.name=name
        self.id=id
        self.category=category
        self.quantity=quantity

class User:
    def __init__(self,name,id,password):
        self.name=name
        self.id=id
        self.__password=password
        self.borrowedBooks=[]
        self.returnBooks=[]
    def changePassword(self,newPassWord):
        self.__password=newPassWord
        # print(f'{self.__password}')
    def checkCriteria(self,name1,id1,password1):
        # print(f'{self.name},{self.id},{self.__password},\n,{name1},{id1},{password1}')
        if self.name!=name1:
            print('problem in name')
            return False
        elif self.id!=id1:
            print('problem in id')
            return False
        elif self.__password!=password1:
            print('Problem in password')
            return False
        else:
            return True
    # def userAddBook(self,name):
    #     self.borrowedBooks.append(name)
    # def isBookAvailable(self):
    #     for it in self.borrowedBooks:
    #         print(it)            

class Library:
    def __init__(self,name):
        self.name=name
        self.userList=[]
        self.bookList=[]
    def addUser(self,name,id,password):
        user=User(name,id,password)
        self.userList.append(user)
        return user
    def addBooks(self,name,id,category,quantity):
        book=Book(name,id,category,quantity)
        self.bookList.append(book)
        return book
    def showBookList(self):
        for book in self.bookList:
            print(f'Book name: {book.name}, Book category: {book.category}, Book quantity: {book.quantity}')
    def showUserList(self):
        for user in self.userList:
            print(f'User name: {user.name}, User id: {user.id}')
    """
def borrowBook(self,name,id,password,bookName):
        user=User(name,id,password)
        ok=False
        for it in self.userList:
            if(it.checkCriteria(name,id,password)):
                print('Congratulations ! You are logged in.')
                ok=True
                break
        if ok==True:
            for it in user.borrowedBooks:
                print('GO')
            for it in self.bookList:
                if it.name==bookName and it.quantity>0:
                    it.quantity-=1
                    user.borrowedBooks.append(f'{bookName}')
                    print(f'You have successfully borrowed this book. Please collect from shelf no: {randrange(100,999)}') 
                    break
        else:
           print('No user found')   """ 
lib1=Library('Hello')
book1=lib1.addBooks('CP Book',231,'CP',10)
book2=lib1.addBooks('CP Book 2',234,'CP',1)
user1=lib1.addUser('Aranna','231','123')
user2=lib1.addUser('Aranna2','232','123')
user1.borrowedBooks.append('CP')
lib1.showBookList()
lib1.showUserList()
# borrowBook(lib1,'Aranna','231','123','CP Book')
# borrowBook(lib1,'Aranna','231','123','CP Book 2')
# borrowBook(lib1,'Aranna2','232','123','CP Book 2')
print(user2.borrowedBooks)


user=None

while(True):
    op=input('\tRegistration/Log In/Exit(R/L/E)\n\tEnter option:')
    if op=='R' or op=='r':
        name=input('\n\tEnter name:')
        id=input('\n\tEnter id:')
        password=(input('\n\tEnter password:'))
        user=User(name,id,password)
        lib1.addUser(user,id,password)
        print('\tRegistration successful.\n\tNow log in')
    elif op=='L' or op=='l':
        name=input('\n\tEnter name:')
        id=input('\n\tEnter id:')
        password=(input('\n\tEnter password:'))
        user=User(name,id,password)
        ok=False
        for it in lib1.userList:
            if(it.checkCriteria(name,id,password)==True):
                print('\tLog in successful')
                ok=True
                break
        if ok==True:
            while True:
                choice=int(input('\tEnter 1 for borrow book, 2 for return book, 3 for book list, 0 for exit:'))
                if choice==1:
                     name=input('\tEnter book name:')
                     found=False
                     if name in user.borrowedBooks:
                        print('\tYou have already borrowed this book')
                        continue
                     for it in lib1.bookList:
                        if it.name==name and it.quantity>1:
                          found=True
                          it.quantity-=1
                          break
                     if found==True:
                        print('\tBook borrowed successfully')
                        user.borrowedBooks.append(name)
                     else:
                         print('\tBook not found')
                elif choice==2:
                    choice2=input('\tAre you want to return your book? (Y/N):')
                    if choice2=='Y' or choice2=='y':
                        name=input('\tEnter book name:')
                        if name in user.borrowedBooks:
                            user.borrowedBooks.remove(name)
                            for it in lib1.bookList:
                                if it.name==name:
                                    it.quantity+=1
                                    break
                            print('\tYou have successfully return this book.')
                        else:
                            print('\tYou return this book or you have enter incorrect name.')
                elif choice==3:
                    print(f'\tYour borrowed books are: {user.borrowedBooks}')
                elif choice==0:
                    break
    elif op=='E' or op=='e':
        print('\tThanks for visiting')
        break