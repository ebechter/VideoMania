# VideoMania

# Exploring the data

import numpy as np
import pandas as pd
import collections
from matplotlib import pyplot as plt
import seaborn as sns


df = pd.read_csv("steam-200k.csv", header=None, index_col=None,\
names=['UserID', 'Game', 'Action', 'Hours', 'Other'])
df = df[df['Action'] == 'play']
# del df['Other']pl
# del df['Action']
# df.head()

# Top20_hours = df.groupby("Game", as_index=False).Hours.aggregate('sum').sort_values('Hours', ascending=False)[:20]
# Top20_Users = df.groupby("Game", as_index=False).UserID.aggregate('count').sort_values('UserID', ascending=False)[:20].rename_axis({"UserID": "Users"}, axis="columns")

# Top20_hours.set_index(pd.Index(list(range(20))), inplace=True)
# Top20_Users.set_index(pd.Index(list(range(20))), inplace=True)

# Lets try and define some kind of ranking index that accounts for both hours played and number 
# of copies purchased 

Tophours = df.groupby("Game", as_index=True).Hours.aggregate('sum')
TopUsers = df.groupby("Game", as_index=True).UserID.aggregate('count')
normhours = (Tophours-Tophours.min())/(Tophours.max()-Tophours.min())
normusers = (TopUsers-TopUsers.min())/(TopUsers.max()-TopUsers.min())
Ranking = normusers+normhours
NormRank=(Ranking-Ranking.min())/(Ranking.max()-Ranking.min())

sns.set_style("darkgrid", {"axes.facecolor": ".9", "axes.edgecolor":".9"})

plt.figure(figsize=(10,5))
ax=NormRank.sort_values(ascending=False)[0:10].plot.barh(color='green',alpha=0.5,position=0.5, edgecolor='black')
ax.set_xlabel("Rank")
ax.set_title("Top 10 Games by Rank")
plt.tight_layout(h_pad=5)
plt.savefig('Figure1.pdf')




# fig1, ax1 = plt.subplots(figsize=(10, 10), sharex=True)  # Set up the matplotlib figure
# x1 = np.array(list(Top20_hours['Game']))
# y1 = np.array(list(Top20_hours['Hours']))
# sns.barplot(x1, y1, palette="BuGn_d", ax=ax1)
# ax1.set_ylabel("Top20 Based on Hours")
# plt.xticks(rotation=90)
# sns.despine(bottom=True)
# plt.tight_layout(h_pad=5)


