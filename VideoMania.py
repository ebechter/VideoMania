# VideoMania exploratory data
import numpy as np
import pandas as pd
import collections
from matplotlib import pyplot as plt
import seaborn as sns



# load the data set
steam = pd.read_csv("steam-200k.csv", header=None, index_col=None,\
names=['ID', 'GameName', 'Action', 'Hours', 'Empty'])
steam.head()

# Remove the purchase flag. That will get rid of expansions and other 'games' in this list 
#that shouldn't be counted

steam = steam.loc[steam['Action'] == 'play']

# Pretty limited data set and appears to be a couple years old. For the full project I intend to update this
# data using steam's API and merging it using subscriber data from twitch.tv. 

# delete final column
del steam['Empty']


# Lets try and define some kind of ranking index that accounts for both hours played and number 
# of copies purchased 

# Normalized total hours played and games purchases using min-max normalization
# This will scale our features to be equally important in the ranking scheme

Tophours = steam.groupby("GameName", as_index=True).Hours.aggregate('sum')
TopUsers = steam.groupby("GameName", as_index=True).ID.aggregate('count')

normhours = (Tophours-Tophours.min())/(Tophours.max()-Tophours.min())
normusers = (TopUsers-TopUsers.min())/(TopUsers.max()-TopUsers.min())

Ranking = normusers+normhours
NormRank=(Ranking-Ranking.min())/(Ranking.max()-Ranking.min())

# ----- Figure 1 ----- # 

# Look at the top 10 games according to this rank
sns.set_style("darkgrid", {"axes.facecolor": ".9", "axes.edgecolor":".9"})
plt.figure(figsize=(10,5))
ax=NormRank.sort_values(ascending=False)[0:10].plot.barh(color='green',alpha=0.5,position=0.5, edgecolor='black')
ax.set_xlabel("Rank")
ax.set_title("Top 10 Games by Rank")
plt.tight_layout(h_pad=5)
# plt.savefig('Figure1.pdf')




# Now lets try to visually classify users into a few categories. Typically there are gamers who play
# lots of games a little, gamers who play a few games a lot, and some inbetween.  

# For each user, sum their total gaming hours and divide by the total number of games they purchased 
# That should give an indicati


# max hours on a game for each user divided by their total hours played. -> loyal gamers closer to 1
# merchant gamers closer to 0, casuals spread in the middle 

sns.set_style("ticks")

UserID = steam.ID.unique()
countGames = np.zeros(steam.ID.nunique())
sumHours = np.zeros(steam.ID.nunique())
OneGameMax = np.zeros(steam.ID.nunique())

for i in range(0,steam.ID.nunique()):
	TempUserList = steam[steam.ID == UserID[i]]
	countGames[i]=TempUserList.shape[0]
	sumHours[i] = TempUserList.Hours.sum()
	OneGameMax[i] = TempUserList.Hours.max()

plt.figure(figsize=(10,5))
ax = plt.gca()
sc=ax.scatter(countGames,sumHours,c=OneGameMax/sumHours,cmap='viridis',s=50,alpha = 0.5)
# ax.set_xscale('log')
# ax.set_yscale('log')
cb=plt.colorbar(sc)
cb.set_label('Game Exclusiveness')
ax.set_xlabel("Total Games Owned ")
ax.set_title("Game Activity per User")
ax.set_ylabel("Total Hours played")
plt.xlim(0, 510)
plt.tight_layout()
plt.savefig('Figure2.pdf')



