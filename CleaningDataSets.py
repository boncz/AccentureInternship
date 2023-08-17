import pandas as pd
import numpy as np

#Read the csv files to pandas DataFrames
df_reaction_types = pd.read_csv('originalData/ReactionTypes.csv', index_col=[0])
df_reactions = pd.read_csv('originalData/Reactions.csv', index_col=[0])
df_content = pd.read_csv('originalData/Content.csv', index_col=[0])

#Save the DataFrames to a list for easier inspection and cleaning
SocialBuzz_dfs = [df_reaction_types, df_reactions, df_content]

#Investigate general state of the data, as well as datatypes
for df in SocialBuzz_dfs:
    print(df.head())
    print(df.info())



#Remove all rows that are missing data
for df in SocialBuzz_dfs:
    df.dropna(axis = 0, how = 'any', inplace=True)

#Change datatypes to reflect the data, as well as dropping columns that are unncessary for this project
df_reaction_types = df_reaction_types.astype({'Type': 'category', 'Sentiment': 'category'} )
df_reactions = df_reactions.astype({'Type': 'category', 'Datetime':'datetime64[ns]'}).drop('User ID', axis = 1)
df_content = df_content.astype({'Type': 'category', 'Category': 'category'}).drop(['User ID', 'URL'], axis = 1)

#Rename columns if necessary for clarity
df_reaction_types.rename(columns={'Type': 'Reaction Type'}, inplace= True)
df_reactions.rename(columns={'Type': 'Reaction Type'}, inplace= True)
df_content.rename(columns= {'Type': 'Content Type'}, inplace= True)

#Checking categorical columns to make sure there are no spelling errors or punctuation differences 
df_unique_reaction_types = np.unique(df_reaction_types[['Reaction Type', 'Sentiment']].values)
print(df_unique_reaction_types)
df_unique_reactions = np.unique(df_reactions['Reaction Type'].values)
print(df_unique_reactions)
df_unique_content = np.unique(df_content[['Content Type', 'Category']].values)
print(df_unique_content)

#Data appears to look good!

#Save the newly cleaned DataFrames to csv files
df_reaction_types.to_csv('cleanDataFiles/ReactionTypesCleaned.csv')
df_reactions.to_csv('cleanDataFiles/ReactionsCleaned.csv')
df_content.to_csv('cleanDataFiles/ContentCleaned.csv')