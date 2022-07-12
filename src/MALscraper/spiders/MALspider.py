from typing import ClassVar, List

from scrapy.http.response import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import AnimeItem
from ..loaders import AnimeLoader


class MALSpider(CrawlSpider):

    name: ClassVar[str] = "MALspider"
    allowed_domains: ClassVar[List[str]] = ["myanimelist.net"]
    start_urls: ClassVar[List[str]] = ["https://myanimelist.net/topanime.php"]
    rules = (
        # Match animes links and parse them
        Rule(LinkExtractor(allow=r"anime\/\d*"), callback="parse_anime"),
        # Match next pages links
        Rule(
            LinkExtractor(allow=r"\?limit=\d+"),
            callback=None,
            process_value=lambda link: "https://myanimelist.net/topanime.php" + link,
        ),
    )

    def parse_anime(self, response: Response) -> AnimeItem:
        loader = AnimeLoader(item=AnimeItem(), response=response)
        loader.add_xpath("title", '//div[@itemprop="name"]/h1/strong/text()')
        loader.add_xpath("synopsis", '//p[@itemprop="description"]/text()')
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
        loader.add_xpath(
            "broadcast",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Broadcast")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "producers",
            '//span[@class="dark_text"]/text()[contains(.,"Producers")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "licensors",
            '//span[@class="dark_text"]/text()[contains(.,"Licensors")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "studios",
            '//span[@class="dark_text"]/text()[contains(.,"Studios")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "source",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Source")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "genres",
            '//span[@class="dark_text"]/text()[contains(.,"Genres")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "themes",
            '//span[@class="dark_text"]/text()[contains(.,"Themes")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "demographic",
            '//span[@class="dark_text"]/text()[contains(.,"Demographic")]/parent::*/parent::*/a/text()',
        )
        loader.add_xpath(
            "duration",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Duration")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "rating",
            '(string(//span[@class="dark_text"]/text()[contains(.,"Rating")]/parent::*/parent::*))',
        )
        loader.add_xpath(
            "score",
            '//span[@itemprop="ratingValue"]/text()',
        )
        loader.add_xpath(
            "ranked",
            '//div[@data-id="info2"]/text()',
        )
        loader.add_xpath(
            "popularity",
            'string(//span[@class="dark_text"]/text()[contains(.,"Popularity")]/parent::*/parent::*)',
        )
        loader.add_xpath(
            "members",
            'string(//span[@class="dark_text"]/text()[contains(.,"Members")]/parent::*/parent::*)',
        )
        loader.add_xpath(
            "favorites",
            'string(//span[@class="dark_text"]/text()[contains(.,"Favorites")]/parent::*/parent::*)',
        )
        anime_item: AnimeItem = loader.load_item()
        return anime_item
