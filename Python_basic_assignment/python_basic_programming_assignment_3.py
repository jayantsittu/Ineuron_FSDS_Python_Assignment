#!/usr/bin/env python
# coding: utf-8

# # 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

# In[2]:


num=int(input("Enter a number"))
if num==0:
    print(f"Number {num} is zero. ")
elif num>0:
    print(f"Number {num} is a postive number")
else:
    print(f"Number {num} is a negative number")
    


# # 2.	Write a Python Program to Check if a Number is Odd or Even?

# In[3]:


num=int(input("Enter a number "))
if num%2==0:
    print(f"Number {num} is an even number.")
else:
    print(f"Number {num} is an odd number. ")


# # 3.	Write a Python Program to Check Leap Year?

# In[5]:


year=int(input("Enter year value "))
if year%4==0 and year%400==0:
    print(f"Year '{year}' is a leap year.")
else:
    print(f"Year '{year}' is not a leapyear.")


# # 4.	Write a Python Program to Check Prime Number?

# In[13]:


num=int(input('Enter a number '))
cnt=0
for values in range(2,(num//2)+1):
    if num%values==0:
        cnt+=1
    if cnt>0:
        print(f"Number {num} is not a prime number.")
        break
else:
    print(f"Number {num} is a prime number.")
    


# # 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

# In[12]:


num=10000

for values in range(2,10001):
    cnt=0
    for i in range(2,(values//2)+1):
        if values%i==0:
            cnt+=1
        if cnt>0:
            
            break
    if cnt==0:
        print(values)
    


# In[ ]:




