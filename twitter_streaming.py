import tweepy
 
# API keyws that yous saved earlier
api_key = "77UdiVpfBQpFZDvxuPlgvMFHs"
api_secrets = "AvycXqpzW6eMv0sjZA6nkLGwqOh4Gh0WRCId0JAKVnABgxP3gb"
access_token = "1531544153275785216-ei4xlrXO8sKVb3QXbkE3Mm12o6W6Jx"
access_secret = "qpA5x82cFKlTnOCqSwwgdQQtzjpRECwkYYV4Ki4NHxAOv"
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)

# tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
 
for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')



# for item in items:
#    print(item.text)
