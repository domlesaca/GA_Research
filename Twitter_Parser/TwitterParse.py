
import tweepy
import time
import codecs
import datetime

#
# Dominic Lesaca
#
# This code is a small example of using the Tweepy Twitter API to search for some terms on twitter.
# Run the program using Python 3 on any IDE which can compile Python code
# You will need to install tweepy to get this code to run properly
# To install Tweepy on pycharm follow these instructions:
#   Go to PyCharm -> Preferences -> Project: your_project -> Project Interpreter,
#   then on the bottom of the window click the "plus" button and type tweepy.
#   Select tweepy on the left side of the window and click the Install Package button.
#   Once you have installed it, then press OK button.
#

def main():
    api = authenticate(
        consumer_key='NpiO9Y5IGB4GnEJHSsIIqB9l2',
        consumer_secret='xQMPyHUy7Wun4VZ72GVhooWkhjdopvg1IUfFDE6hAIM65DyyFZ',
        access_token='923215542957117442-OgEVtGW0tg4OCdJXhLuZ3K6kPMWvsIU',
        access_token_secret='ReaXKCbUEAFuCke2tISyIM9iZpv31I2Tai83gZinW2sBx'
    )

    #  Get the term to search
    q = input("Enter a term to query: ")
    searchFor(api, q)

# authenticates tweepy
def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api



# Function searches for terms on twitter
def searchFor(api, query="#green"):
    # get 10 tweets containing the search term
    results = api.search(q=query, count=200, tweet_mode="extended")

    #open text file to save tweets to
    file = codecs.open(query+'_tweets.txt', 'w', "utf-8")
    # Cycle through each term found
    x= 1
    for result in results:
        if result.lang=='en':
            #N Number them as we print
            print(x, "\n")
            x += 1
            # print text of the tweet
            print(result.full_text)
            # print date and time of the post
            print(result.created_at)
            file.write(result.full_text+"\n")
    file.close()

if __name__ == '__main__':
    main()

# Following code is not necessary to run this test, feel free to play around with it if you want
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
