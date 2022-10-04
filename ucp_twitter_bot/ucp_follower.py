import tweepy

from ucp_twitter_bot import twitter_authentication


def following_follower_from_follower_list() -> None:
    api = twitter_authentication.set_authetication()

    for follower in tweepy.Cursor(api.get_followers).items():
        print(f"Check Follower: {follower.name}")
        if not follower.following:
            print(f"Following {follower.name}")
            try:
                follower.follow()
            except tweepy.errors.Forbidden as err:
                print("Failed Following")
                print(err)
            except Exception as err:
                raise err
