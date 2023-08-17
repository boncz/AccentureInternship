import pandas as pd
from openpyxl import load_workbook

#First read in the cleaned csv data files
df_reaction_types = pd.read_csv('cleanDataFiles/ReactionTypesCleaned.csv', index_col=[0])
df_reactions = pd.read_csv('cleanDataFiles/ReactionsCleaned.csv', index_col=[0])
df_content = pd.read_csv('cleanDatafiles/ContentCleaned.csv', index_col=[0])

#merge the files into one usable DataFrame
df_reactions_content = pd.merge(df_reactions, df_content, on='Content ID')
df_merged = pd.merge(df_reactions_content, df_reaction_types, on='Reaction Type')

#Determine the top 5 categories, based on the sum of all points per category
df_top_categories = df_merged.groupby('Category').Score.sum().sort_values(ascending=False)
df_top_five = df_top_categories[:5]

#save the merged/clean DataFrame to a new excel file
df_merged.to_excel('cleanDataFiles/reactionsContentMerged.xlsx', sheet_name= 'Cleaned Data Set')

with pd.ExcelWriter('cleanDataFiles/reactionsContentMerged.xlsx', mode='a', engine='openpyxl') as writer:
    df_top_five.to_excel(writer, sheet_name='Top Five Categories')