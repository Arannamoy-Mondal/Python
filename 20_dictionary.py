dictionary={'Word1':'Hello','Word2':'Hi','Word3':'Bye'}
for key,value in dictionary.items():
    print(key,value)
print(dictionary['Word1'])
del dictionary['Word1']
print(dictionary)
dictionary['Word1']='Good Bye'
print(dictionary)