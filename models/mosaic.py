from models.goods import Goods
from models.kind_of_product import KindOfProduct


class Mosaic(Goods):
    def __init__(self, kind_of_product, price_in_uah=0.0, country_of_producing="not specified",
                 min_age_for_using=0):
        super().__init__(kind_of_product, price_in_uah, country_of_producing, min_age_for_using)