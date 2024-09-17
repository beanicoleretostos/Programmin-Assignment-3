#!/usr/bin/env python
# coding: utf-8

# ##### **Problem 2:** Save your file as Surname_Pandas-P1.py
# ##### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# ##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
# ##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# ##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# ##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[2]:


import pandas as pd

cars = pd.read_csv('cars.csv')


# In[5]:


##### a.) Odd-numbered column

Odd_cars = cars.iloc[[1,3,5,7,9]]

Odd_cars


# In[7]:


#### b.)Display the row that contains the 'Model' of 'Mazda Rx4

cars.loc[[0]] #the row where the model is in index 0. 


# In[9]:


#### c.) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

cars.loc[cars['Model']=='Camaro Z28',['cyl']]


# #### d.) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, 
# #### ‘Ford Pantera L’ and ‘Honda Civic’ have. 
# #### I used tuple so that i can find three models and display the needed info. 

# In[12]:


cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') |
    (cars['Model'] == 'Ford Pantera L') |
    (cars['Model'] == 'Honda Civic'),
    ['gear', 'cyl']
]



# In[ ]:




