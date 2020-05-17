import datetime
from models.kind_of_product import KindOfProduct


class Goods:
    def __init__(self, kind_of_product=KindOfProduct.DRAWING, price_in_uah = 0.0, country_of_producing ="not specified", min_age_for_using = 0):
        self.kind_of_product = kind_of_product
        self.price_in_uah = price_in_uah
        self.country_of_producing = country_of_producing
        self.min_age_for_using = min_age_for_using

    def __str__(self):
        return ',\n'.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])+'\n'

