import pandas as pd

#Read the csv files to pandas DataFrames
df_reaction_types = pd.read_csv('ReactionTypes.csv', index_col=[0])
df_reactions = pd.read_csv('Reactions.csv', index_col=[0])
df_content = pd.read_csv('Content.csv', index_col=[0])

#Save the DataFrames to a list for easier inspection and cleaning
SocialBuzz_dfs = [df_reaction_types, df_reactions, df_content]

#Investigate general state of the data, as well as datatypes
for df in SocialBuzz_dfs:
    print(df.head(20))
    print(df.info())

#Remove all rows that are missing data
for df in SocialBuzz_dfs:
    df.dropna(axis = 0, how = 'any', inplace=True)

#Change datatypes to reflect the data, as well as dropping columns that are unncessary for this project
df_reaction_types = df_reaction_types.astype({'Type': 'category', 'Sentiment': 'category'} )
df_reactions = df_reactions.astype({'Type': 'category', 'Datetime':'datetime64[ns]'}).drop('User ID', axis = 1)
df_content = df_content.astype({'Type': 'category', 'Category': 'category'}).drop(['User ID', 'URL'], axis = 1)

#Save the newly cleaned DataFrames to csv files
df_reaction_types.to_csv('ReactionTypesCleaned.csv')
df_reactions.to_csv('ReactionsCleaned.csv')
df_content.to_csv('ContentCleaned.csv')