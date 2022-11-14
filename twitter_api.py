import tweepy as tw
import pandas as pd
import json

# Keys and Access Tokens
consumer_key = '77UdiVpfBQpFZDvxuPlgvMFHs'
consumer_secret = 'AvycXqpzW6eMv0sjZA6nkLGwqOh4Gh0WRCId0JAKVnABgxP3gb'
access_token = '1531544153275785216-ei4xlrXO8sKVb3QXbkE3Mm12o6W6Jx'
access_token_secret = 'qpA5x82cFKlTnOCqSwwgdQQtzjpRECwkYYV4Ki4NHxAOv'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def search_tweets(language, hashtag, date, number):

    # Define the search term and the date_since date as variables
    search_words = hashtag
    date_since = date
    new_search = search_words + " -filter:retweets"  # Do not get retweet of tweets

    # Collect tweets
    tweets = tw.Cursor(api.search, q=new_search,
                       lang=language, since=date_since).items(number)

    users_locs = [[tweet.created_at, tweet.text, tweet.user.followers_count,
                   tweet.retweet_count, tweet.favorite_count] for tweet in tweets]

    data = users_locs

    # with open('testData.json', 'w') as fh:
    #     json.dump(users_locs, fh)

    with open('testData.json', 'w') as f:
        f.write(data.to_json())

    # !cat df.json

    # # To Dataframe
    # tweet_df = pd.DataFrame(data=users_locs, columns=[ 'time_stamp', 'text', 'followers_count',
    #                                                   'retweet_count', 'favorite_count'])

    # return Dataframe
    # return tweet_df

    # df = search_tweets('th', '#GDAinBKK', '2022-11-14', 1000)

    # df.sample(10)

    # with open('test.json', 'w') as f:
    # f.write(df.to_json(orient='records', lines=True))
