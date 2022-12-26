#!/usr/bin/env python
# coding: utf-8

# # 1.	Write a Python program to convert kilometers to miles?

# In[5]:


input_km=float(input('Enter Kilometers'))
def km_to_miles (km):
    return float(round(km*0.621371, 2))
km_to_miles(input_km)


# # 2.	Write a Python program to convert Celsius to Fahrenheit?

# In[7]:


cel=float(input('Enter celsius'))
def celsius_to_Fahrenheit(cel):
    return float(round(cel*(1.8)+32,2))
celsius_to_Fahrenheit(cel)


# # 3.	Write a Python program to display calendar?

# In[12]:


import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year, month))


# # 4.	Write a Python program to solve quadratic equation?

# In[15]:


import cmath

a =float(input('Enter value of a for the quadretic equation ax^2 +bx+c'))
b =float(input('Enter value of b for the quadretic equation ax^2 +bx+c'))
c =float(input('Enter value of c for the quadretic equation ax^2 +bx+c'))

# calculate the discriminant
d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(f'The solution are {sol1} and {sol2}'.format(sol1,sol2))


# # 5.	Write a Python program to swap two variables without temp variable?

# In[16]:


var1=input('Enter 1st variable')
var2=input('Enter 1st variable')
print(f"Before swap var1 & var2 are - {var1} and {var2}")
var2,var1=var1,var2
print(f"After swap var1 & var2 are - {var1} and {var2}")


# In[ ]:




