# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from dataclasses import dataclass, field


@dataclass
class AnimeItem:
    title: str | None = field(default=None)
    jtitle: str | None = field(default=None)
