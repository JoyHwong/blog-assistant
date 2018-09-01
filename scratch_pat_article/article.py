class Article:
    def __init__(self, url, title, id):
        self.url = url
        self.title = title
        self.id = id

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id
