#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd# data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np#linear algebra 
import seaborn as sns
import matplotlib.pyplot as plt #r data visualizing processes
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[30]:


data = pd.read_csv("F:\\abalone\HR.csv")


# In[31]:


data.head(5)


# In[32]:


data.tail(5)


# In[33]:


data.sample(5)


# In[34]:


print("original data in index base  " + str(len(data.index)))


# In[35]:


data.shape


# In[36]:


data.info()


# In[37]:


data.describe()


# In[38]:


def count_unique(data):
    for i in data.columns:
        count = data[i].nunique()
        print(i , " : " , count)
count_unique(data)        


# In[39]:


sns.countplot(x='left', data=data)


# In[40]:


sns.countplot(x='left', hue="department", data=data)


# In[41]:


sns.countplot(x="left", hue="salary", data=data)


# In[42]:


data['promotion_last_5years'].plot.hist()


# In[43]:


data.isnull().any()


# In[44]:


data.isnull().sum()


# In[45]:


pd.get_dummies(data["salary"]).head(10)


# In[46]:


pd.get_dummies(data["salary"], drop_first=True).head(10)


# In[47]:


department=pd.get_dummies(data['department'],drop_first=True)
department.head(5)


# In[48]:


data_1=pd.concat([data,salary],axis=1)#combining the dummy variables into dataset & naming the new datset as data_1.showing the first 5 observations 
data_1.head(5)


# In[ ]:





# In[ ]:




