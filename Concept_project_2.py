# make library management system 

class Book:
    def __init__(self,name,id,cat,quantity):
        self.name=name
        self.id=id
        self.cat=cat # category 
        self.quantity=quantity

class User:
    def __init__(self,name,id,password):
        self.name=name
        self.id=id
        self.password=password
        self.borrowBooks=[]

class Library:
    def __init__(self,owner,name):
        self.owner=owner
        self.name=name
        self.books=[]
        self.users=[]
    def addBook(self,name,id,cat,quan):
        book=Book(name,id,cat,quan)
        self.books.append(book)
        return book
    def addUser(self,name,id,password):
        user=User(name,id,password)
        self.users.append(user)
        return user
    def borrowBook(self,user,id):
        for book in self.books:
            if book.id==id:
                if book in user.borrowBooks:
                    print(f'Already borrow this book')
                    return
                elif book.quan<1:
                    print(f'No available copies !')
                    return
                else:
                    print(f'You have successfully borrowed {book.name} book')
                    user.borrowBooks.append(book)
                    book.quan-=1
                    return
        print(f'Book not found !')


library1=Library('Everyone','None')
admin1=library1.addUser('Admin1','1','admin')
user1=library1.addUser('User01','2','user')
pybook=library1.addBook('Sci-Fi','15','Dune',100)

currentUser=admin1
while True:
    if currentUser==None:
        print(f'\n\tNo user logged in !')

        option=input('Registration / Log in (R/L):')
        if option=='R':
            id=int(input(f'\t Enter id: '))
            name=input(f'\tEnter name: ')
            password=input(f'Enter password: ')
            user=library1.addUser(id,name,password)
        elif option=='L':
            id=int(input(f'\t Enter id: '))
            # name=input(f'\tEnter name: ')
            password=input(f'Enter password: ')
            match=False
            for user in library1.users:
                if id==user.id and password==user.password:
                    currentUser=user
                    match=True
                    break
            if match==False:
                print('\n\tUser not found !')
    else:

        if currentUser==admin1:
            print('\tOptions:\n')
            print('1: Add Book')
            print('2: Add User')
            print('3: Show Books')
            print('5: LogOut')
            choice=int(input('Enter option no:'))
            if choice==1:
                name=input('Enter name: ')
                id=input('Enter id: ')
                cat=input('Enter category: ')
                quantity=int(input('Enter quantity:'))
                book=Book(name,id,cat,quantity)
                library1.addBook(name,id,cat,quantity)
            elif choice==5:
                currentUser=None
        else:
            print('\tOptions:\n')
            print('1: Add Book')
            print('2: Add User')
            print('3: Show Books')
            print('5: LogOut')