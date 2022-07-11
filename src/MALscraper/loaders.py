from itemloaders.processors import Identity, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from .utils.loaders import get_last_split_value


class AnimeLoader(ItemLoader):

    # By default returns the raw data
    default_output_processor = Identity()

    # How to preprocess title field
    title_in = MapCompose(str.strip, str.title)
    title_out = TakeFirst()

    # How to preprocess jtitle field
    jtitle_in = MapCompose(str.strip, get_last_split_value, str.strip)
    jtitle_out = TakeFirst()
