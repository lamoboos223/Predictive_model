import tweepy
from textblob import TextBlob


consumer_key= "xNBKv9tSNTfYJEl1Vn8wTKPTj"
consumer_secret = "pl68vDTIKJowvmsFkZ7LHlhobHDtrfh2V1nL8WUBVpaKYTaLNK"

access_token = "871902424310665217-s2LbBl1NH1M2TdXd7N83lI2xjL4UwjG"
access_token_secret = "Lv3mrcPD8HV17zJHOF0GZefOGy3kdlptTZdp3xjH2rcJn"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search("lamaoslamaoslamaos")
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print (analysis.sentiment)