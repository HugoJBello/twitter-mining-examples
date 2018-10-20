#pip3 install python-dotenv
#pip3 install tweepy
import tweepy
import os
import time
from dotenv import load_dotenv
load_dotenv()

def main():
    API_KEY = os.getenv("API_KEY")
    API_TOKEN = os.getenv("API_TOKEN")
    ACCESS_KEY = os.getenv("ACCESS_TOKEN")
    ACCESS_SECRET = os.getenv("ACCESS_TOKEN2")

    auth = tweepy.OAuthHandler(API_KEY, API_TOKEN)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    accounts = ["@bello_hugh"]
    for screen_name in accounts:
        followers = get_followers(api,screen_name)
        print(followers);

def get_followers(api,screen_name):

    users = tweepy.Cursor(api.followers, screen_name=screen_name).items()
    followers = []
    while True:
        try:
            user = next(users)
        except tweepy.TweepError:
            time.sleep(60*15)
            user = next(users)
        except StopIteration:
            break
        followers.append(user.__dict__)
    return followers


if __name__ == '__main__':
	main()