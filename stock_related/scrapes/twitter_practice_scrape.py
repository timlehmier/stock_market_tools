import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "from:MrZackMorris"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

df_ticker_symbols = (df[df['Tweet'].str.contains('$', regex=False)])

df_ticker_symbols.to_csv('stock_related/data/df_twitter_ticker_symbols.csv',
                         index=False, header=True, sep=',')
