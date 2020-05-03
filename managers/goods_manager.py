from typing import List

from models.kind_of_product import KindOfProduct
from models.pen import Pen
from models.Pencil import Pencil
from models.mosaic import Mosaic
from models.goods import Goods
import doctest


class GoodsManager:
    def __init__(self):
        self.list_of_all_goods = []

    def find_good_by_country_of_producing (self, country_of_producing_for_search):
        """
        looks for goods with  country of producing returns list of goods which we founded
        >>> goods_manager = GoodsManager()
        >>> goods_manager.list_of_all_goods.append(Pencil(KindOfProduct.DRAWING, 9.0, "Columbia", 9))
        >>> goods_manager.list_of_all_goods.append(Pen(KindOfProduct.DRAWING, 10.0, "Germany", 6))
        >>> goods_manager.list_of_all_goods.append(Mosaic(KindOfProduct.MOSAIC, 20.0, "USA", 3))
        >>> list_of_found_goods = goods_manager.find_good_by_country_of_producing ("USA")
        >>> len(list_of_found_goods)
        1
        """
        list_of_found_goods: List[Goods] = []
        for good in self.list_of_all_goods:
            if good.country_of_producing == country_of_producing_for_search:
                list_of_found_goods.append(good)
        return list_of_found_goods

    def find_good_with_price(self, price_for_search):
        """
        looks for goods with  price returns list  goods which founded
        >>> goods_manager = GoodsManager()
        >>> goods_manager = GoodsManager()
        >>> goods_manager.list_of_all_goods.append(Pencil(KindOfProduct.DRAWING, 9.0, "Columbia", 9))
        >>> goods_manager.list_of_all_goods.append(Pen(KindOfProduct.DRAWING, 10.0, "Germany", 6))
        >>> goods_manager.list_of_all_goods.append(Mosaic(KindOfProduct.MOSAIC, 20.0, "USA", 3))
        >>> list_of_found_goods = goods_manager.find_good_with_price(10.0)
        >>> [good.price_in_uah for good in list_of_found_goods]
        [10.0]
        """
        list_of_found_goods = []
        for good in self.list_of_all_goods:
            if good.price_in_uah == price_for_search:
                list_of_found_goods.append(good)
        return list_of_found_goods


if __name__ == '__main__':
    doctest.testmod(verbose=True)