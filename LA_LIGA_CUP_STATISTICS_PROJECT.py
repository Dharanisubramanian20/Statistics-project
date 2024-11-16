#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # 1.Read the data set and replace dashes with 0 to make sure you can perform arithmetic operations on the data. (2.5 points)

# In[3]:


data=pd.read_csv("C:\\Users\\dhara\\Documents\\Statistics for Datascience\\download.csv",skiprows=1)
data.head(5)


# In[4]:


data.replace('-',0,inplace=True)


# In[25]:


data.head(5)


# # 2.Print all the teams which have started playing between 1930-1980. (5 points)

# In[16]:


data['Debut']=pd.to_numeric(data['Debut'])
team_1930_1980=data[(data['Debut'] >= 1930) & (data['Debut'] <= 1980)]
print(team_1930_1980['Team'])


# # 3.Print the list of teams which came Top 5 in terms of points (2.5 points)

# In[17]:


data['Points']=pd.to_numeric(data['Points'])
top_5=pd.DataFrame(data.nlargest(5,'Points'))
print(top_5[['Team','Points']])


# # 4.Write a function with name “Goal_diff_count” which should return all the teams with their Goal Differences. Using the same function, find the team which has maximum and minimum goal difference. (5 points)

# # Goal_diff_count = GoalsFor - GoalsAgainst

# In[19]:


def Goal_diff_count(df):
    df['GoalsFor']=pd.to_numeric(df['GoalsFor']).fillna(0)
    df['GoalsAgainst']=pd.to_numeric(df['GoalsAgainst']).fillna(0)
    df['Goal_difference'] = df['GoalsFor'] - df['GoalsAgainst']
    return df[['Team','Goal_difference']]
    
LA_LIGA=Goal_diff_count(data)

max_goal=data.loc[[data['Goal_difference'].idxmax()]]
min_goal=data.loc[[data['Goal_difference'].idxmin()]]
print("Team with maximum goal difference")
print(max_goal)

print("Team with minimum goal difference")
print(min_goal)


# # 5.Create a new column with name “Winning Percent” and append it to the data set (5 points)
# 
# Percentage of Winning = (GamesWon / GamesPlayed)*100
# 
# If there are any numerical error, replace it with 0%
# 
# Print the top 5 teams which has the highest Winning percentage

# In[20]:


data['GamesWon']=pd.to_numeric(data['GamesWon']).fillna(0)
data['GamesPlayed']=pd.to_numeric(data['GamesPlayed']).fillna(0)
data['WinningPercent']=(data['GamesWon']/data['GamesPlayed'])*100
data['WinningPercent'].fillna(0,inplace=True)

top_5_winning_team=data.nlargest(5,'WinningPercent')
print(top_5_winning_team[['Team','WinningPercent']])


# # 6. Group teams based on their “Best position” and print the sum of their points for all positions (10 points)
# 
# Eg: Best Position     Points
# 
#          1                   25000
# 
#          2                    7000

# In[24]:


data['BestPosition']=pd.to_numeric(data['BestPosition']).fillna(0)
Grouped_Points=data.groupby('BestPosition')['Points'].sum().reset_index()
print(Grouped_Points)


# In[ ]:




