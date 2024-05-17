#!/usr/bin/env python
# coding: utf-8

# # Calculator Project

# In[20]:


# Building the Calculations for Addition, Multiplication, Subtraction, Divison

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y


# In[9]:


#Creating our user inputs, having the user specify add , sub multiply or divide

choice = input('Enter Choice(A, S,M, D) : ')

num1 = float(input('Enter first number'))

num2 = float(input('Enter second number'))


# In[27]:


# Creating an if statement to check if the user input the correct choice

print("Enter A for Addition")
print("Enter S for Subtraction")
print("Enter M for Multiplication")
print("Enter D for Divison")

choice = input('Enter Choice (A,S,M,D) : ')

if choice.upper() in ('A','ADD','ADDITION','S','SUBTRACT','SUBTRACTION','M','MULTIPLE','MULTIPLICATION','D','DIVIDE','DIVISON'):
    num1 = float(input('Enter first number'))
    num2 = float(input('Enter second number'))
    
    if  choice.upper() in ('A','ADD','ADDITION'):
        print('Result:', num1,'+', num2, '=', add(num1, num2))

    elif  choice.upper() in ('S','SUBTRACT','SUBTRACTION'):
        print('Result:',num1,'-', num2, '=', subtract(num1, num2))

    elif  choice.upper() in ('M','MULTIPLY','MULTIPLICATION'):
        print('Result:',num1,'*', num2, '=', multiply(num1, num2))

    elif  choice.upper() in ('D','DIVIDE','DIVISON'):
        print('Result:',num1,'/', num2, '=', divide(num1, num2))

else:
    print("Please Input a correct choice")











# In[37]:


# Creating an if statement to check if the user input the correct choice, and putting into a while loop so users can continue to keep using the calculator

print("Enter A for Addition")
print("Enter S for Subtraction")
print("Enter M for Multiplication")
print("Enter D for Divison")

while True: 
    choice = input('Enter Choice (A,S,M,D) : ')
    if choice.upper() in ('A','ADD','ADDITION','S','SUBTRACT','SUBTRACTION','M','MULTIPLE','MULTIPLICATION','D','DIVIDE','DIVISON'):
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter second number'))
        
        if  choice.upper() in ('A','ADD','ADDITION'):
            print('Result:', num1,'+', num2, '=', add(num1, num2))
    
        elif  choice.upper() in ('S','SUBTRACT','SUBTRACTION'):
            print('Result:',num1,'-', num2, '=', subtract(num1, num2))
    
        elif  choice.upper() in ('M','MULTIPLY','MULTIPLICATION'):
            print('Result:',num1,'*', num2, '=', multiply(num1, num2))
    
        elif  choice.upper() in ('D','DIVIDE','DIVISON'):
            print('Result:',num1,'/', num2, '=', divide(num1, num2))
    
    else:
        print("Please Input a correct choice")

    next_calculation = input("want to do another calucation? (Yes/No?): ")
    if next_calculation.lower() in ('no','n','nope','nah'):
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




