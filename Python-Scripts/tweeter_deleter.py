import tweepy

consumer_key = 'xxxx'
consumer_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

deleted_count = 0  # Counter for deleted tweets

while True:
    tweets = api.user_timeline(count=200)  # Retrieve up to 200 of your most recent tweets

    if not tweets:  # No more tweets to delete
        break

    for tweet in tweets:

        # Optionally, you can also print other information such as the tweet ID, creation time, etc.
        # Example:
        # print(f"ID: {tweet.id}")
        # print(f"Created at: {tweet.created_at}")

        # Uncomment the above lines if you want to print additional information

        api.destroy_status(tweet.id)  # Delete the tweet
        deleted_count += 1

print(f"Deleted {deleted_count} tweets.")