class Tweet:
    def __init__(self, id, content, media=None):
        self.id = id
        self.content = content
        self.media = media or []

class TwitterUserScraper:
    def __init__(self, username):
        self.username = username

    def get_items(self):
        return [Tweet("demo123", f"Mock tweet from @{self.username}")]
