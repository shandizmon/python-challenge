
# coding: utf-8

# In[2]:


# Import Dependencies
import pandas as pd
import os


# In[30]:


# Store the file path associated with the file
election_data = os.path.join("Resources", "election_data_1.csv")
#election_data = os.path.join("Resources", "election_data_2.csv")


# In[31]:


df_election_data = pd.read_csv(election_data)
df_election_data.head()


# In[32]:


vote_count = df_election_data['Voter ID'].count()
print(vote_count)


# In[33]:


print(df_election_data.Candidate.unique())


# In[34]:


candidate_votes = df_election_data['Candidate'].value_counts()
print(candidate_votes)


# In[35]:


print(candidate_votes / vote_count * 100)


# In[37]:


import operator
print('Winner:',max(candidate_votes.items(), key=operator.itemgetter(1))[0])

