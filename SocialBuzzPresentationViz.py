import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Load the excel file into a new DataFrame to analyze
df_social_buzz = pd.read_excel('cleanDataFiles/reactionsContentMerged.xlsx', sheet_name='Cleaned Data Set')

#Recal what were found to be the top five categories
df_top_categories = df_social_buzz.groupby('Category', as_index=False).Score.sum().sort_values(by='Score', ascending=False)
df_top_five = df_top_categories[:5]
print(df_top_five['Category'])

#What are all the categories? What are the Reaction Types?
df_all_categories = df_social_buzz.Category.unique()
df_num_categories = df_social_buzz.Category.nunique()
df_all_reaction_types = df_social_buzz['Reaction Type'].unique()
df_num_reaction_types = df_social_buzz['Reaction Type'].nunique()



print(f'There are {df_num_categories} total categories: \n{df_all_categories}\n There are {df_num_reaction_types} total Reaction Types: \n{df_all_reaction_types}')



#print(df_top_categories.head(50))
# sns.set_style('darkgrid')
# plot = sns.displot(data=df_social_buzz, x='Category', hue='Reaction Type')
# plot.set_xticklabels(rotation=90)
# plt.show()