class teacher: # class no 1
    def __init__(self,name,id,subject) -> None:
        self.name=name
        self.id=id
        self.subject=subject
    def __repr__(self) -> str:
        return f'Name: {self.name}, Id: {self.id}, Subject: {self.subject}'

class student: # class no 2
    def __init__(self,name,ClaSs,id) -> None:
        self.name=name
        self.ClaSs=ClaSs
        self.id=id
    def __repr__(self) -> str:
        return f'Student name: {self.name}, Class: {self.ClaSs}, Id: {self.id}'

class school: # combine class
    def __init__(self,name) -> None:
           self.name=name
           self.std=[]
           self.teach=[]
           self.problem=''
    def add_teacher(self,name,id,subject):
        tmp=teacher(name,id,subject)
        self.teach.append(tmp)
    def enroll(self,name,ClaSs,id,amount):
        if(amount<6500):
            self.problem+=(name+' '+id+' has not enough balance\n')
        else:
            tmp=student(name,ClaSs,id)
            self.std.append(tmp)
    def __repr__(self):
        for i in self.std:
            print(i)
        for i in self.teach:
            print(i)
        return self.problem
school1=school('AITM')
school1.add_teacher('A','01','Algorithm; Autonomous Nagigation;')
school1.add_teacher('B','02','Introduction to C, C++, Python, JS, Solidity, Anaconda, Ruby;System Design; Introduction to Cryptography ;')
school1.add_teacher('C','03','Advanced Data Structure and Algorithm; Solidity Framework; Web 3 tokens; Layer 2 blockchain;')
school1.add_teacher('D','10','Introduction to blockchain; Advanced Cryptography; Ether;')
school1.add_teacher('E','25','Introduction to FPGA, ASIC and Microcontroller; FPGA Capstone;')
school1.add_teacher('F','35','Introduction to PoS,PoW, PoS; Blockchain Implementation;')
school1.add_teacher('K','99','Penetration; Database; DevOps;')
school1.enroll('Std1','Quarter-6','B-6',6500)
school1.enroll('Std36','Quarter-12','B-2',5500)
school1.enroll('Std5','Quarter-4','B-3',6400)
school1.enroll('Std7','Quarter-8','B-4',9500)
school1.enroll('Std35','Quarter-8','B-5',6500)
print(school1)
"""
teacher1=teacher('A','01','Algorithm; Autonomous Nagigation;')
teacher2=teacher('B','02','Introduction to C, C++, Python, JS, Solidity, Anaconda, Ruby;System Design; Introduction to Cryptography ;')
teacher3=teacher('C','03','Advanced Data Structure and Algorithm; Solidity Framework; Web 3 tokens; Layer 2 blockchain;')
teacher4=teacher('D','10','Introduction to blockchain; Advanced Cryptography; Ether;')
teacher5=teacher('E','25','Introduction to FPGA, ASIC and Microcontroller; FPGA Capstone;')
teacher6=teacher('F','35','Introduction to PoS,PoW, PoS; Blockchain Implementation;')
teacher7=teacher('K','99','Penetration; Database; DevOps;')
std1=student('Std1','Quarter-6','B-6')
std2=student('Std36','Quarter-12','B-2')
std3=student('Std5','Quarter-4','B-3')
std4=student('Std7','Quarter-8','B-4')
std5=student('Std35','Quarter-8','B-5')
print(teacher1)
print(teacher2)
print(teacher3)
print(teacher4)
print(teacher5)
print(teacher6)
print(teacher7)
print(std1)
print(std2)
print(std3)
print(std4)
print(std5)"""