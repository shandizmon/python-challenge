
# coding: utf-8

# In[48]:


# Import Dependencies
import pandas as pd
import os


# In[49]:


# Store the file path associated with the file
#budget_data = os.path.join("Resources", "budget_data_1.csv")
budget_data = os.path.join("Resources", "budget_data_2.csv")


# In[43]:


df_budget_data = pd.read_csv(budget_data)
df_budget_data.head()


# In[44]:


num_months = df_budget_data['Date'].count()
sum_revenue = df_budget_data['Revenue'].sum()
print('Total months:',num_months)
print('Total Revenue: $',sum_revenue)


# In[45]:


df_budget_data['Change'] = df_budget_data['Revenue'].diff()
#print(df_budget_data)
averageRevenueChange = df_budget_data['Change'].sum() / num_months
print('Average Revenue Change:',averageRevenueChange)


# In[46]:


maxChange = df_budget_data.loc[df_budget_data['Change'].idxmax()]
print('Greatest Increase in Revenue: ',maxChange['Date'],'($',maxChange['Revenue'],')')


# In[47]:


minChange = df_budget_data.loc[df_budget_data['Change'].idxmin()]
print('Greatest Decrease in Revenue:', minChange['Date'],'($',minChange['Revenue'],')')

