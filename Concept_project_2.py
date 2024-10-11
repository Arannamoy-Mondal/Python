# make library management system 

class Book:
    def __init__(self,name,id,cat):
        self.name=name
        self.id=id
        self.cat=cat

class User:
    def __init__(self,name,id,password):
        self.name=name
        self.id=id
        self.password=password

class Library:
    def __init__(self,owner,name):
        self.owner=owner
        self.name=name
        self.books=[]
        self.users=[]
