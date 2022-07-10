from typing import ClassVar, List

from scrapy.http.response import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AnimeItem


class MALSpider(CrawlSpider):
    name: ClassVar[str] = "MALspider"
    allowed_domains: ClassVar[List[str]] = ["myanimelist.net"]
    start_urls: ClassVar[List[str]] = ["https://myanimelist.net/anime.php?letter=A"]

    rules = (Rule(LinkExtractor(allow=r"anime\/\d*"), callback="parse_anime"),)

    def parse_anime(self, response: Response) -> AnimeItem:
        anime: AnimeItem = AnimeItem()
        anime.title = response.xpath('//div[@itemprop="name"]/h1/strong/text()').get()
        anime.jtitle = (
            response.xpath(
                'normalize-space(string(//span[@class="dark_text"]/text()[contains(.,"Japanese")]/parent::*/parent::*))',
            )
            .get()
            .split(":")[-1]
            .strip()
        )
        return anime
