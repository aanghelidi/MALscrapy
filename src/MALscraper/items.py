# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


class AnimeItem(Item):
    title = Field()
    jtitle = Field()
    anime_type = Field()
    n_episodes = Field()
