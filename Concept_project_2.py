# make a library management system 
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
        print(f'\t{self.name},{self.id},{self.__password},\n\t,{name1},{id1},{password1}')
        if self.name!=name1:
            print('\tproblem in name')
            return False
        elif self.id!=id1:
            print('\tproblem in id')
            return False
        elif self.__password!=password1:
            print('\tProblem in password')
            return False
        else:
            return True



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
        book=Book(name,id,category,int(quantity))
        self.bookList.append(book)
        return book
    

    def showBookList(self):
        for book in self.bookList:
            print(f'\tBook name: {book.name}, Book category: {book.category}, Book quantity: {book.quantity}')


    def showUserList(self):
        for user in self.userList:
            print(f'\tUser name: {user.name}, User id: {user.id}')





lib1=Library('Library 1')
user=None
while(True):
    op=input('\n\tRegistration/Log In/Administration/Exit(R/L/A/E)\n\tEnter option:')
    if op=='R' or op=='r':
        name=input('\n\tEnter name:')
        if(len(name)<4):
            name=input('\n\tEnter name (Minimum 4 character):')
        id=input('\n\tEnter id:')
        password=(input('\n\tEnter password:'))
        user=User(name,id,password)
        lib1.addUser(name,id,password)
        print('\n\tRegistration successful.\n\tNow log in')
    elif op=='L' or op=='l':
        name=input('\n\tEnter name:')
        id=input('\n\tEnter id:')
        password=(input('\n\tEnter password:'))
        user=User(name,id,password)
        ok=False
        for it in lib1.userList:
            if(it.checkCriteria(name,id,password)==True):
                print('\n\tLog in successful')
                ok=True
                break
        if ok==False:
            print('\n\tYou have enter incorrect credential.')
        elif ok==True:
            while True:
                choice=int(input('\n\tEnter 1 for borrow book, 2 for return book, 3 for book list, 0 for exit:'))
                if choice==1:
                     name=input('\n\tEnter book name:')
                     found=False
                     if name in user.borrowedBooks:
                        print('\n\tYou have already borrowed this book')
                        continue
                     for it in lib1.bookList:
                        if it.name==name and it.quantity>1:
                          found=True
                          it.quantity-=1
                          break
                     if found==True:
                        print('\n\tBook borrowed successfully')
                        user.borrowedBooks.append(name)
                     else:
                         print('\n\tBook not found')
                elif choice==2:
                    choice2=input('\n\tAre you want to return your book? (Y/N):')
                    if choice2=='Y' or choice2=='y':
                        name=input('\n\tEnter book name:')
                        if name in user.borrowedBooks:
                            user.borrowedBooks.remove(name)
                            for it in lib1.bookList:
                                if it.name==name:
                                    it.quantity+=1
                                    break
                            print('\n\tYou have successfully return this book.')
                        else:
                            print('\n\tYou return this book or you have enter incorrect name.')
                elif choice==3:
                    print(f'\n\tYour borrowed books are: {user.borrowedBooks}')
                elif choice==0:
                    break
    elif op=='E' or op=='e':
        print('\n\tThanks for visiting')
        break
    elif op=='A' or op=='a':
        userid=input('\n\tEnter userid:')
        password=input('\n\tEnter password:')
        if userid=='admin' and password=='admin':
            print('\n\tAdmin log in successful.')
            while True:
                choice=int(input('\n\t1 for Add book in booklist, 2 for user list, 3 for book list, 0 for exit:'))
                if choice==1:
                    name=input('\n\tEnter book name:')
                    id=input('\n\tEnter book id:')
                    category=input('\n\tEnter book category:')
                    quantity=input('\n\tEnter book quantity:')
                    lib1.addBooks(name,id,category,quantity)
                    print('\n\tAdd book successfully')
                elif choice==2:
                    lib1.showUserList()
                elif choice==3:
                    lib1.showBookList()
                elif choice==0:
                    break


