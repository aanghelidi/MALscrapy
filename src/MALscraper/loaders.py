from functools import partial

from itemloaders.processors import Identity, Join, MapCompose, TakeFirst
from scrapy.loader import ItemLoader

from .utils.loaders import get_last_split_value

# Custom functions
get_field = partial(get_last_split_value, sep=":")


class AnimeLoader(ItemLoader):

    # By default returns the raw data
    default_output_processor = Identity()

    # How to preprocess synopsis field
    synopsis_in = MapCompose(
        str.strip,
        lambda v: v if v else None,
        lambda v: v if "Written" not in v else None,
        lambda v: v if "Source" not in v else None,
    )
    synopsis_out = Join()

    # How to preprocess title field
    title_in = MapCompose(str.strip, str.title)
    title_out = TakeFirst()

    # How to preprocess jtitle field
    jtitle_in = MapCompose(str.strip, get_field, str.strip)
    jtitle_out = TakeFirst()

    # How to preprocess anime_type field
    anime_type_in = MapCompose(str.strip, get_field, str.strip)
    anime_type_out = TakeFirst()

    # How to preprocess n_episodes field
    n_episodes_in = MapCompose(str.strip, get_field, str.strip)
    n_episodes_out = TakeFirst()

    # How to preprocess status field
    status_in = MapCompose(str.strip, get_field, str.strip)
    status_out = TakeFirst()

    # How to preprocess aired field
    aired_in = MapCompose(str.strip, get_field, str.strip)
    aired_out = TakeFirst()

    # How to preprocess premiered field
    premiered_in = MapCompose(str.strip, get_field, str.strip)
    premiered_out = TakeFirst()

    # How to preprocess broadcast field
    broadcast_in = MapCompose(
        str.strip,
        str.split,
        lambda v: v if "Broadcast" not in v else None,
    )
    broadcast_out = Join()

    # How to preprocess producers field
    producers_in = MapCompose(str.strip, str.title)
    producers_out = Identity()

    # How to preprocess licensors field
    licensors_in = MapCompose(str.strip, str.title)
    licensors_out = Identity()

    # How to preprocess studios field
    studios_in = MapCompose(str.strip, str.title)
    studios_out = Identity()
