#!/usr/bin/env python
# coding: utf-8

# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# A class is considered as a blueprint of objects. We can think of the class as a sketch (prototype) of a house. It contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House is the object.
# 
# Since many houses can be made from the same description, we can create many objects from a class.
# 
# An object is called an instance of a class.
# 
# 
# 

# In[3]:


class Home:
    def __init__(self, door, window):
        self.door = door
        self.window = window
        
    def Door(self):
        return self.door
    def Window(self):
        return self.window
Obj = Home('open','close')


# In[7]:


Obj


# In[8]:


Obj.Door()


# In[9]:


Obj.Window()


# Q2. Name the four pillars of OOPs.

# The Four pillars of OOPs, abstraction, encapsulation, inheritance, and polymorphism, are integral to understanding and using OOP.

# In[23]:


#encapsulation

class Bank:
    def __init__(self, balance):
        self.__balance = balance  #private balance we have created
        
    def check_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
        return self.__balance
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
pin = Bank(5000)
    

    


# In[24]:


pin


# In[25]:


pin.check_balance()


# In[26]:


pin.withdraw(500)


# In[27]:


pin.deposit(500)


# In[32]:


#inheritance
class A:
    def a(self):
        print("This is class A")
        
class B(A):
    def b(self):
        print("This is class B")
        
class C(B):
    def c(self):
        pass
    
inh = C()


# In[34]:


inh.a()


# In[35]:


inh.b()


# In[44]:


class a:
    def A(self):
        print("This is class A")
class b:
    def B(self):
        print("This is class B")
class c(a,b):
    pass

m = c()


# In[48]:


m.A()


# In[49]:


m.B()


# Q3. Explain why the __init__() function is used. Give a suitable example.

# __init__ is a special python method that runs whenever a new object is created. These types of functions are used to initialize the attributes of that class

# In[53]:


class car:
    def __init__(self,car):
        self.car = car
    
    def giv(self):
        return self.car
    
obj = car('Black')
        


# In[54]:


obj.giv()


# Q4. Why self is used in OOPs?

# The use of self makes it easier to distinguish between instance attributes (and methods) from local variables.

# Q5. What is inheritance? Give an example for each type of inheritance.

# In[ ]:




