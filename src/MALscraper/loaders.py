from itemloaders.processors import Identity, MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class AnimeLoader(ItemLoader):

    # By default returns the raw data
    default_output_processor = Identity()

    # How to preprocess title field
    title_in = MapCompose(str.strip, str.capitalize)
    title_out = TakeFirst()
