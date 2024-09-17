#!/usr/bin/env python
# coding: utf-8

# ## **Bea Nicole L. Retostos**
# ### **2ECE-C**
# #### **Programming Assignment #3** 

# #### I. **Intended Learning Outcomes:** 
# 1. To identify the codes and functions incorporated in the Pandas library
#   2.  To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

# #### **II. Instructions:**
# 
# Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.
# For this programming assignment, download the following file and save to your default user folder:
# http://bit.ly/Cars_file

# Problem 1: Save your file as Surname_Pandas-P1.py
# Using knowledge obtained from the experiment and demonstrations:
# a. Load the corresponding .csv file into a data frame named cars using pandas
# b. Display the first five and last five rows of the resulting cars.
# 

# In[5]:


#### Step 1: Import Pandas Libary

import pandas as pd

#### Step 2: Load the file (make sure that it is in the same path with your code.)
cars = pd.read_csv('cars.csv')

#### Step 3: To get the first five cars, use .head syntax. 
First_five = cars.head()


#### Step 4: Print First five
First_five 


# In[7]:


#### Step 5: To get the last five cars, use .tail syntax.
Last_five = cars.tail()

#### Step 6: Print Last five
Last_five 


# In[ ]:




