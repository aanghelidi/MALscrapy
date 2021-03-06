# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


class AnimeItem(Item):

    # Meta section
    url = Field()

    # Information section
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
    themes = Field()
    demographic = Field()
    duration = Field()
    rating = Field()

    # Statistics section
    score = Field()
    ranked = Field()
    popularity = Field()
    members = Field()
    favorites = Field()
