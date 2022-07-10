from itemloaders.processors import Identity
from scrapy.loader import ItemLoader


class AnimeLoader(ItemLoader):

    # By default returns the raw data
    default_output_processor = Identity()
