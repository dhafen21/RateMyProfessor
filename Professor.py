from scrape import *


class Professor:

    def __init__(self):
        self.name = None
        self.url = None
        self.data = Responses.Responses()

    def get_data(self, url, wd):
        self.data.class_name, self.data.quality, self.data.difficulty, self.data.comments, self.name, self.date = scrape(self.url, wd)

    def set_url(self, url):
        self.url = url
