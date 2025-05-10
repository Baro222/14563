import snscrape.modules.twitter as sntwitter

class TwitterUserScraper:
    def __init__(self, username):
        self.username = username

    def get_items(self):
        return sntwitter.TwitterUserScraper(self.username).get_items()

