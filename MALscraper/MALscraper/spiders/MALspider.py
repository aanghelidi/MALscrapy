from typing import ClassVar

from scrapy.http.response import Response
from scrapy.item import Item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MALSpider(CrawlSpider):
    name: ClassVar[str] = "MALspider"
    allowed_domains: ClassVar[list[str]] = ["myanimelist.net"]
    start_urls: ClassVar[list[str]] = ["https://myanimelist.net/anime.php?letter=A"]

    rules = (Rule(LinkExtractor(allow=r"anime\/\d*"), callback="parse_anime"),)

    def parse_anime(self, response: Response) -> Item:
        anime: dict[str, int | str] = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return anime
