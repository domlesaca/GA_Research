
import tweepy
import time
import datetime

def main():
    api = authenticate(
        consumer_key='NpiO9Y5IGB4GnEJHSsIIqB9l2',
        consumer_secret='xQMPyHUy7Wun4VZ72GVhooWkhjdopvg1IUfFDE6hAIM65DyyFZ',
        access_token='923215542957117442-OgEVtGW0tg4OCdJXhLuZ3K6kPMWvsIU',
        access_token_secret='ReaXKCbUEAFuCke2tISyIM9iZpv31I2Tai83gZinW2sBx'
    )

    searchFor(api)

# authenticates tweepy
def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

# get followers of a user
def followers(api, name="domlesaca"):
    sleeptime = 4
    pages = tweepy.Cursor(api.followers, screen_name=name).pages()

    while True:
        try:
            page = next(pages)
            time.sleep(sleeptime)
        except tweepy.TweepError as e: #taking extra care of the "rate limit exceeded"
            print(e)
            print("waiting")
            time.sleep(60*15)
            page = next(pages)
        except StopIteration:
            break
        for user in page:
            print(user.id_str)
            print(user.screen_name)
            print(user.followers_count)

def searchFor(api, query="#green"):
    results = api.search(q=query, count=10)
    for result in results:
        #for r in result
        print(result.text)
        print(results.created_at)

if __name__ == '__main__':
    main()
