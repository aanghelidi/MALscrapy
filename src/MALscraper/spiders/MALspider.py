from typing import ClassVar, List

from scrapy.http.response import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AnimeItem
from ..loaders import AnimeLoader


class MALSpider(CrawlSpider):

    name: ClassVar[str] = "MALspider"
    allowed_domains: ClassVar[List[str]] = ["myanimelist.net"]
    start_urls: ClassVar[List[str]] = ["https://myanimelist.net/anime.php?letter=A"]
    rules = (Rule(LinkExtractor(allow=r"anime\/\d*"), callback="parse_anime"),)

    def parse_anime(self, response: Response) -> AnimeItem:
        loader = AnimeLoader(item=AnimeItem(), response=response)
        loader.add_xpath("title", '//div[@itemprop="name"]/h1/strong/text()')
        loader.add_xpath(
            "jtitle",
            'string(//span[@class="dark_text"]/text()[contains(.,"Japanese")]/parent::*/parent::*)',
        )
        loader.add_xpath(
            "anime_type",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Type")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "n_episodes",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Episodes")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "status",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Status")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "aired",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Aired")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "premiered",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Premiered")]/parent::*/parent::*))',
        )
        anime_item: AnimeItem = loader.load_item()
        return anime_item
