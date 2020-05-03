from models.goods import Goods
from models.kind_of_product import KindOfProduct


class Pencil(Goods):
    def __init__(self, kind_of_product, price_in_uah=0.0, country_of_producing="not specified",
                 min_age_for_using=0):
        super().__init__(kind_of_product, price_in_uah, country_of_producing, min_age_for_using)


if __name__ == '__main__':
    a = Pencil(KindOfProduct.DRAWING, 30.5, "Columbia", 3)
    print(a)