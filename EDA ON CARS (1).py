#!/usr/bin/env python
# coding: utf-8

# ##EDA ON CARS DATA SET
# Exploratory data analysis was promoted by John Tukey to encourage statisticians to explorethe data, and possibly formulate hypotheses that could lead to new data collection and
# experiments.
# 
# EDA:EDA means EXPLORATORY DATA ANALYSIS. In statistics, exploratory data analysis (EDA) is an approach to analyzing data sets to
# summarize their main characteristics, often with visual methods. 
# 

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Numpy:It is a package used for importing Numerical data type
# Pandas:It is a package used for Data Analytics 
# Matplotlib.pyplot:It is a package used for Visulaization purpose 
# Seaborn:It is a advance package built based on Matplotlib

# In[4]:


car=pd.read_csv("E:/ppts/machine learning/1-eda/CARS.csv")
car


# In[ ]:


IN THESE WE ARE LOADING THE CARS DATA SET
AS WE CAN SEE THE MAKE,MODEL,TYPE ...etc


# In[5]:


car.isnull().sum()


# In[ ]:


dataframename.isnull().sum()display which column has how many missing values (or null values)
As we can see In Cylinders Columns there are two missing values


# In[6]:


# show how many rows and cols in the dataset
car.shape


# In[7]:


# dataset information
car.info()


# In[8]:


car = car.drop_duplicates(keep='first')
car


# In[9]:


car.dropna(inplace=True)


# In[10]:


car.isnull().sum()


# In[11]:


car.describe()


# In[12]:


car.columns = car.columns.str.replace(' ', '')
car.columns 


# In[13]:


car_sort = car.sort_values(by='MPG_City', ascending=False)

car_sort.head()


# In[14]:


plt.hist(car["MPG_City"],bins=10,color='green',edgecolor='black')


# In[15]:


sns.distplot(car[('MPG_City')], bins=10, color='green')


# To select only numeric type of columns, we can give their names or datatypes as:

# In[16]:


car[['EngineSize','Cylinders','Horsepower','MPG_City','MPG_Highway','Weight','Wheelbase'
,'Length']]


# In[17]:


car.select_dtypes(include=['float64', 'int64'])


# In[23]:


car_num = car.select_dtypes(include=['float64', 'int64'])
car_num
# display histograms for all numeric columns
car_num.hist(bins=20)


# In[24]:


car_num.corr(method ='pearson')['MPG_City']


# In[25]:


#draw pair plots to show correlations
sns.pairplot(car_num, vars = ["EngineSize", "Cylinders", "Horsepower", "MPG_City",
"MPG_Highway"], hue='MPG_City')


# In[26]:


box1 = sns.boxplot(x='Type', y='MPG_City', data=car)


# In[27]:


# SUV gives less mileage and Hybrid gives more mileage
# sedan and wagon show more variation


# In[28]:


box2 = sns.boxplot(x='Origin', y='MPG_City', data=car)
# The origin of car is Asia gives slightly more mileage


# In[29]:


box3 = sns.boxplot(x='DriveTrain', y='MPG_City', data=car)
# Front drive train is giving more mileage


# In[30]:


sns.regplot(car['Length'], car['MPG_City'])


# In[ ]:




