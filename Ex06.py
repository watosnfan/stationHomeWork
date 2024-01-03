# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:19:48 2023

@author: USER
"""

class Father:
    def display(self,name):
        self.name = name
        print('Father name is ',self.name)
        
        
class Mother:
    def display(self,name):
        self.name = name
        print('Mother name is ',self.name)     
        
        
class Child(Father,Mother):
    pass

class Son(Father):
    pass

print(Child.__name__,'類別有二個父類')

for item in Child.__bases__:
    print(item)
    
print(Son.__name__,'類別，只有一個父類')    
print(Son.__bases__)

bill = Son()
bill.display('John')

Son.__bases__ = (Mother,)
bill.display('Mary')
print(Son.__bases__)





        