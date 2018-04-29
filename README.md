
# Video-Mania Project Description
I plan on looking into non-obvious trends in data sets concerning the videogame industry. Currently, there is data as to the purchasers and users of video games as well as the consumers of video game streams. This data can yield interesting insights into which games particular users would enjoy, or which streams they should consider watching. This has the potential to create more diversity in the purchasing and viewership of lesser known games. In addition to this, it’s possible to create a recommender system based off of a users previous interests to find games that would likely be enjoyable to him or her. Furthermore these results are applicable to groups of friends with diverse tastes or even a couple who can never decide on a game.

## What video game should I play?

If you Google the question, “which video game should I play next?” you will yield about 1.45 million results, and Google’s search results exist the form of quizzes (simple decision trees); clickbait articles (click through slides); and online forums (communal decision making). However, there is no tool present that will accurately choose which video games an individual, couple, or group of individuals would enjoy. In order to begin researching this question, I first looked into which video games, according to the data set I accessed, were most popular. I characterized most popular as being a hybrid between most purchased and games with the most hours played. This yielded these shown in my first figure. The second graphic I produced was intended to visually explore how often people play one game in their library far more than the others. The results are shown in the second figure. 

## What is the market significance of these questions?
PwC projects that the videogame industry will surpass 90 billion dollars by 2020. The video game market is saturated by few top, high performing games, and this creates, in the end users, an effective silo where the games they are recommended across platforms tend to be other high selling games. If a tool could identify games that are enjoyed by a smaller number of users but exhibit a high level of loyalty, we could identify “cult favorites” or “indie games.” Doing this can allow for a possible recommender system to not just contribute to the sales of already top selling games, but allow for a bit of diversity in the picking process.

In addition to being able to identify games that a user might never have heard of, or played otherwise, a recommender tool could be able to match not just a single user to a list of games they would likely enjoy, but match multiple individuals. This is, of course, helpful for couples who enjoy different game genres, and groups of friends with diverse tastes. This type of matching can be accomplished by the user-user collaborative filtering, as we mainly have user information detailing which game titles are in their library, or singular value decomposition (SVD).

## How do we retrieve this data?
So far, the data I’ve worked with is publically available on Kaggle. The dataset I used to create these graphs utilized 20,000 video game titles with such characteristics as amount of purchasers of a game, hours played in certain games, user IDs, and other games owned by those users. This data set is fairly limited in scope and slightly outdated. However, by connecting with Twitch and Steam, through their APIs if I continue on with this project, I will be able to collect more updated and more precise data. For example, since this data set was released, two more popular games of the year - PUBG and Fortnite have been searched for on Google between two and twenty times more that DOTA 2 (the most popular game listed on the Kaggle data set) has. You can see here (https://twitchtracker.com/games) that, even on Twitch, streams of Fortnite, League of Legends, and PubG are exceeding in popularity above Dota 2.

Working with this data set has led me to want to utilize Steam and Twitch’s APIs to collect a similar data set that is perhaps larger and more updated. On Steam, seen here (http://steamcharts.com/) as of April 29th, 2018, Dota 2 is still popular but other newer games are eclipsing the Kaggle’s top ten most popular games due to the data set being outdated.

## What are some questions that may be answered with data gathered from Steam or Twitch?

1. What games are more likely to be “cult favorites,” with a high number of hours played by a relatively low number of users?

2. What games are going to be more appealing to different groups of gamers: the merchant gamer, the casual gamer, and the loyal gamer (respectively, individuals who buy many games but play little, individuals who play and purchase an average amount, and individuals who purchase few games that they play a lot)?

3. What games are the highest performing, with a high number of users purchasing them and playing them for a relatively high number of hours?

4. What games should I play in the future, given my past favorite games and other user’s experiences?

5. What games should my partner and I play together, given that we have divergent tastes?

6. What games should my group of friends and I play, given that we each have preferences to genre but need to identify non-obvious shared characteristics between those preferences?

## Conclusion

There’s much to be done with data retrieved from Steam and/or Twitch. It would be incredibly interesting to explore all or some of the questions I have posed above, and it would be helpful to learn more tools as I pursue this capstone project.




