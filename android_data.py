#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


gp = pd.read_csv('googleplaystore.csv')
gp


# In[4]:


gp_1 = gp.drop_duplicates()
print('Total number of apps in dataset = ', gp_1)


# In[5]:


print(gp_1.info)


# In[6]:


n = 5
gp_1.sample(n)


# In[66]:


gp_1.dtypes


# In[125]:


gp_1['Size'] = gp_1['Size'].str.strip('M')
gp_1['Category'] = gp_1['Category'].astype('str')
gp_1['Installs'] = gp_1['Installs'].astype('str')
gp_1['Price'] = gp_1['Price'].astype('str')



# In[108]:


gp_1


# In[109]:


conda install plotly


# In[110]:


import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go


# In[111]:


num_categories = len(gp_1['Category'].unique())
print('Number of categories = ', num_categories)

num_apps_in_category = gp_1['Category'].value_counts().sort_values(ascending = False)


# In[112]:



data = [go.Bar(
        x = num_apps_in_category.index, 
        y = num_apps_in_category.values, 
)]

plotly.offline.iplot(data)


# In[113]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[114]:


avg_app_rating = gp_1['Rating'].mean()
print('Average app rating = ', avg_app_rating)
avg_app_rating


# In[115]:


data = [go.Histogram(
        x = gp_1['Rating']
)]


layout = {'shapes': [{
              'type' :'line',
              'x0': avg_app_rating,
              'y0': 0,
              'x1': avg_app_rating,
              'y1': 1000,
              'line': { 'dash': 'dashdot'}
          }]
          }

plotly.offline.iplot({'data': data, 'layout': layout})


# In[116]:


large_categories


# In[126]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set_style("darkgrid")
import warnings
warnings.filterwarnings("ignore")

apps_with_size_and_rating_present = gp_1[(~gp_1['Rating'].isnull()) & (~gp_1['Size'].isnull())]

large_categories = apps_with_size_and_rating_present.groupby(['Category']).filter(lambda x: len(x) >= 250).reset_index()

plt1 = sns.jointplot(x = large_categories['Size'], y = large_categories['Rating'], kind = 'hex')

paid_apps = apps_with_size_and_rating_present[apps_with_size_and_rating_present['Type'] == 'Paid']

plt2 = sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])
get_ipython().run_line_magic('debug', '')


# In[128]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(20,8)
popular_apps_cats = gp_1[gp_1.Category.isin(['GAME', 'PHOTOGRAPHY', 'MEDICAL', 'BUSINESS'])]
ax = sns.stripplot(x = popular_apps_cats['Price'], y = popular_apps_cats['Category'], color = 'blue', jitter = True, linewidth = 1)
ax.set_title('App pricing trends across categories')
apps_above_200 = popular_apps_cats[['Category', 'App','Price']][popular_apps_cats['Price'] > 200]
apps_above_200


# In[130]:


apps_under_100 = popular_apps_cats[['Category','App', 'Price']][popular_apps_cats['Price'] < 100]
fig, ax = plt.subplots()
fig.set_size_inches(15,8)
ax = sns.stripplot(x='Price', y='Category', data=apps_under_100,
                   jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories after filtering for junk apps')


# In[131]:


trace0 = go.Box(
  
    y=gp_1[gp_1['Type'] == 'Paid']['Installs'],
    name = 'Paid'
)

trace1 = go.Box(
   
    y=gp_1[gp_1['Type'] == 'Free']['Installs'],
    name = 'Free'
)

layout = go.Layout(
    title = "Number of downloads of paid apps vs. free apps",
    yaxis = dict(
        type = 'log',
        autorange = True
    )
)

# Add trace0 and trace1 to a list for plotting
data = [trace0, trace1]
plotly.offline.iplot({'data': data, 'layout': layout})


# In[134]:


reviews_df = pd.read_csv('googleplaystore_user_reviews.csv')


merged_df = pd.merge(gp_1, reviews_df, on = 'App', how = "inner")

# Drop NA values from Sentiment and Translated_Review columns
merged_df = merged_df.dropna(subset=['Sentiment', 'Translated_Review'])

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)

# User review sentiment polarity for paid vs. free apps
ax = sns.boxplot(x = 'Type', y = 'Sentiment_Polarity', data = merged_df)
ax.set_title('Sentiment Polarity Distribution')


# In[ ]:




