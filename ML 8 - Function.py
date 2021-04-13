#!/usr/bin/env python
# coding: utf-8

# In[2]:


# simple function
def function1 ():
    print("Hello, knowledge Shelf")
# calling function
function1()
    


# In[5]:


# no argument no return type function
def add():
    num1 = int(input("Enter the value of num1 :"))
    num2 = int(input("Enter the value of num2 :"))
    num3 = num1 + num2
    print("Sum is ", num3)

add()


# In[1]:


# with argument and no return type
def sub(var1, var2):
    sub = var1 - var2
    print("Subtraction is", sub)
    
# calling function
sub (12, 6)


# In[2]:


# with no argument and with return type
def multiply():
    var1 = int(input("Enter the value of variable 1"))
    var2 = int(input("Enter the value of variable 2"))
    var3 = var1*var2
    return(var3)
# calling function in another variable
var4 = multiply()
print("Multiplication is", var4)


# In[4]:


# with argument and return type
def div(var1, var2):
    var3 = var1/var2
    return var3

# calling the function
var4 = div(49, 9)
print("Division is", var4)

