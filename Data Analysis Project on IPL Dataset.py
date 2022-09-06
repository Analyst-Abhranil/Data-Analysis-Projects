#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data=pd.read_csv('matches - matches.csv')
data


# In[ ]:


#Getting a preview of the data


# In[4]:


data.info()


# In[5]:


data.describe()


# In[13]:


# How many matches have been played in Hyderabad,Bangalore and Mumbai


# In[8]:


mask=data['city']=='Hyderabad'
x=data[mask]
x.shape[0]


# In[9]:


def city_match_count(place):
    mask=data['city']==place
    return data[mask].shape[0]
    


# In[10]:


city_match_count('Bangalore')


# In[16]:


city_match_count('Mumbai')


# In[12]:


#Finding out the number matches have been played in Kolkata after 2010


# In[14]:


mask1=data['city']=='Kolkata'
mask2=data['season']>2010
data[mask1 & mask2].shape[0]


# In[35]:


#Finding out the playing teams and winners from each matchday


# In[40]:


data.iloc[:,[4,5,10]]


# In[17]:


# Finding Out the Top 5 teams in terms of most wins

#Showing the result in a diagram



# In[19]:


data['winner'].value_counts()


# In[22]:


x=data['winner'].value_counts().sort_values(ascending=False).head()
x


# In[21]:


import matplotlib.pyplot as plt


# In[25]:


x.plot(kind='barh')


# In[26]:


# Finding out the ratio between batting first and bowling first after winning the toss


# In[28]:


data['toss_decision'].value_counts()


# In[29]:


data['toss_decision'].value_counts().plot(kind='pie')


# In[30]:


#Finding Out the total number of matches played by all the teams


# In[34]:


x=(data['team1'].value_counts()+data['team2'].value_counts())
x.sort_values(ascending=False)


# In[41]:


# Finding out the winner of every IPL Season



# In[45]:


data.drop_duplicates(subset=['season'],keep='last')


# In[46]:


data.drop_duplicates(subset=['season'],keep='last')[['season','winner']]


# In[49]:


data.drop_duplicates(subset=['season'],keep='last')[['season','winner']].sort_values('season').set_index('season')


# In[4]:


data2=pd.read_csv('deliveries.csv')
data2.head()


# In[5]:


# Finding out Top 5 Batsman with most runs in IPL



# In[10]:


data2.groupby('batsman')['batsman_runs'].sum()


# In[11]:


data2.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head()


# In[12]:


# Find out Top 5 Six hitters in IPL


# In[14]:


mask=data2['batsman_runs']==6
x=data2[mask]
x


# In[15]:


x.groupby('batsman')['batsman_runs'].count()


# In[16]:


x.groupby('batsman')['batsman_runs'].count().sort_values(ascending=False).head()


# In[17]:


# Find Out Strike rate any batsman


# In[19]:


balls=data2.groupby('batsman')['batsman_runs'].count()
balls


# In[21]:


runs=data2.groupby('batsman')['batsman_runs'].sum()
runs


# In[22]:


strike_rate=(runs/balls)*100
strike_rate


# In[23]:


def get_sr(batter):
    mask=data2['batsman']==batter
    x=data2[mask]
    return (x['batsman_runs'].sum()/x['batsman_runs'].count())*100
    
    


# In[25]:


get_sr('Yuvraj Singh')


# In[26]:


# Find Out The Top 3 teams against which Virat Kohli scored most runs


# In[27]:


data2[data2['batsman']=='V Kohli'].groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending=False).head(3)


# In[28]:


#Finding Out the top 5 batsmen with highest strike rate in the deathovers(16-20)
#batsman should play atleast 200 balls in the deathovers


# In[29]:


mask=data2['over']>15
death_over=data2[mask]
death_over


# In[32]:


x=death_over.groupby('batsman')['batsman_runs'].count()
eligible_batters=x[x>200]
eligible_batters



# In[33]:


eligible_batters.index


# In[34]:


batter_list=eligible_batters.index.to_list()
batter_list


# In[37]:


death_over['batsman'].isin(batter_list)
y=death_over[death_over['batsman'].isin(batter_list)]
y


# In[38]:


balls=y.groupby('batsman')['batsman_runs'].count()


# In[39]:


runs=y.groupby('batsman')['batsman_runs'].sum()


# In[41]:


S_rate=(runs/balls)*100
S_rate.sort_values(ascending=False).head()


# In[42]:


# Find Out The Orange Cap Holder of each season


# In[43]:


new_data=data2.merge(data,left_on='match_id',right_on='id')
new_data.shape


# In[45]:


new_data.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False)


# In[50]:


new_data.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False).reset_index()


# In[51]:


new_data.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False).reset_index().drop_duplicates(subset=['season'])


# In[58]:


z=new_data.groupby(['season','batsman'])['batsman_runs'].sum().sort_values(ascending=False).reset_index().drop_duplicates(subset=['season'])
z[['season','batsman']].sort_values('season')


# In[65]:


## Finding Out How many Sixes every team has hit in each over
# Showing the result by using a heatmap


# In[60]:


s=new_data[new_data['batsman_runs']==6]
s


# In[62]:


pt=s.pivot_table(index='batting_team',columns='over',values='batsman_runs',aggfunc='count')
pt


# In[63]:


import seaborn as sns


# In[64]:


sns.heatmap(pt)


# In[ ]:




