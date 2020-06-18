#!/usr/bin/env python
# coding: utf-8

# <b> Weather Dataset

# In[43]:


import pandas as pd


# In[44]:


weather=pd.read_csv(r"C:\Users\chest\OneDrive\Desktop\Weather\WeatherData.csv")


# In[45]:


weather


# <b> Analyze DataFrames and Data Explorations

# In[46]:


weather.head()


# In[47]:


weather.shape


# There are 8784 rows and 8 columns in our dataset

# <b>.Index

# In[48]:


weather.index


# <b>columns

# In[49]:


weather.columns


# These are all the names of the columns on our dataset

# <b>dtypes

# In[50]:


weather.dtypes


# columns and their datatypes

# <b>unique()

# In[51]:


weather['Weather'].unique()


# All the unique values present in Weather column

# <b>nunique()

# In[52]:


weather.nunique()


# The total numberof unique values present in each column of our dataset

# <b>count()

# In[53]:


weather.count()


# Our dataset doesnt have null values

# In[ ]:





# In[ ]:


weather['Weather'].value_counts()


# Shows unique values in our dataset weather column with their total count

# <b>info()

# In[ ]:


weather.info()


# our dataset columns and their infomations

# <b> Q1 Find the total number of unique 'Wind Speed' values in the dataset

# In[15]:


weather.nunique()


# In[16]:


weather['Wind Speed_km/h'].nunique()


# There are 34 unique values in total for Wind Speed

# In[17]:


weather['Wind Speed_km/h'].unique()


# these are all the unique values present and in total they are 34

# <b> Q2 Find the number of times when the 'Weather is exactly clear'

# In[18]:


weather.Weather.value_counts()


# it is exactly clear for 1326 times

# In[19]:


#using filter
weather[weather.Weather=='Clear']


# In[20]:


#using groupby
weather.groupby('Weather').get_group('Clear')


# <b> Q3 Find the number of times when the Wind Speed was exactly 4km/h

# In[21]:


weather.groupby('Wind Speed_km/h').get_group(4)


# In[22]:


weather[weather['Wind Speed_km/h']==4]


# The windspeed was exactly 4km/h for 474 times

# <b> Q4 Find all the null values in the dataset

# In[23]:


weather.isnull().sum()


# We have no null values in our dataset

# In[24]:


weather.notnull().sum()


# <b> Q5 Rename the column name 'Weather' of the dataframe to 'Weather Condition'

# In[25]:


weather.rename(columns={'Weather':'Weather Condition'},inplace=True)


# In[26]:


weather.head(2)


# <b> Q6 Find the mean for Visibility

# In[27]:


weather['Visibility_km'].mean()


# In[28]:


weather.Visibility_km.mean()


# <B>Q7 What is the standard deviation of Pressure

# In[29]:


weather.Press_kPa.std()


# In[30]:


weather['Press_kPa'].std()


# <B> Q8 What is the Variance of 'Relative Humidity'?

# In[31]:


weather['Rel Hum_%'].var()


# <b> Q9 Find all instance where Snow was recorded in this data

# In[32]:


weather['Weather Condition'].value_counts()


# In[33]:


weather.groupby('Weather Condition').get_group('Snow')


# In[34]:


weather[weather['Weather Condition']=='Snow']


# In[35]:


#str.contains()
#if snow is present
weather[weather['Weather Condition'].str.contains("Snow")]


# <B> Q10 Find all instances when 'Wind Speed is above 24' and  'Visibility is 25'

# In[36]:


cond1=weather['Wind Speed_km/h']>24
cond2=weather['Visibility_km']==25


# In[37]:


ans=weather[cond1 & cond2]
ans


# In[38]:


weather[(weather['Wind Speed_km/h']>24) & (weather['Visibility_km']==25)]


# <b> Q11 Find the max and min value of each column against Weather Condition

# In[39]:


weather.groupby('Weather Condition').max()


# In[40]:


weather.groupby('Weather Condition').min()


# In[ ]:





# In[ ]:





# In[ ]:




