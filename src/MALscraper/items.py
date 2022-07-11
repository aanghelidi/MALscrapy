# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


class AnimeItem(Item):
    synopsis = Field()
    title = Field()
    jtitle = Field()
    anime_type = Field()
    n_episodes = Field()
    status = Field()
    aired = Field()
    premiered = Field()
    broadcast = Field()
    producers = Field()
    licensors = Field()
    studios = Field()
    source = Field()
    genres = Field()
    duration = Field()
    rating = Field()
    score = Field()
