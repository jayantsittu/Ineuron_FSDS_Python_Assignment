#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print &quot;Hello Python&quot;?
# 

# In[ ]:

print("Hello Python")


# # 2. Write a Python program to do arithmetical operations addition and division.?
# 

# In[6]:


nums=[int(i) for i in input('Enter space separated numbers - ').split()]
def arithmetic_operation(operation_type,numbers):
    if operation_type.lower() in ('addition','add','sum','+'):
        return sum(numbers)
    elif operation_type.lower() in ('division','/'):
        if len(numbers)>=2:
                
            div=numbers[0]
            for number in numbers[1:]:
                if number !=0 and number >0:
                    div=div/number
        else:
            print('There should be atleast two numbers for division')
        return div

sum_=arithmetic_operation('addition',nums)
div=arithmetic_operation('/',nums)
print(f"sum = {sum_} and div={div}")


# # 3. Write a Python program to find the area of a triangle?
# 

# In[19]:


base,height,unit=input('Enter space separated base height and unit of triange respectively').split()[:3]
area_of_triangle=0.5*int(base)*int(height)
unit=unit+'^2'
print(f"Area of the triange is {area_of_triangle} {unit}.")


# # 4. Write a Python program to swap two variables?
# 

# In[21]:


x,y=input('Enter two values').split()
print('Values before swap')
print(f'value 1 is {x} and value 2 is {y}')
y,x=x,y
print('Values after swap')
print(f'value 1 is {x} and value 2 is {y}')


# # 5. Write a Python program to generate a random number?

# In[25]:


import random
num = random.random()
print(num)


# In[ ]:





# In[ ]:




