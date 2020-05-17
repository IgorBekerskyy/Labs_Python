from models.kind_of_product import KindOfProduct
from models.pen import Pen
from models.Pencil import Pencil
from models.mosaic import Mosaic
from models.sorttype import SortType
import doctest


class GoodsManagerUtils:

    def __init__(self, list_of_all_goods):
        self.list_of_all_goods = list_of_all_goods

    def sort_by_price_in_uah(self, sort_type):
        """
        Sorts goods list in given order, returns this list
        >>> parker_pencil = Pencil(KindOfProduct.DRAWING, 20.0, "Columbia", 3)
        >>> global_pen = Pen(KindOfProduct.DRAWING, 35.0, "USA", 12)
        >>> child_mosaic = Mosaic(KindOfProduct.MOSAIC, 10.0, "Germany", 6)
        >>> goods_list = [parker_pencil, global_pen, child_mosaic]
        >>> goods_manager_utils = GoodsManagerUtils(goods_list)
        >>> list_of_goods_sorted_by_price = goods_manager_utils.sort_by_price_in_uah(SortType.ASC)
        >>> [good.price_in_uah for good in list_of_goods_sorted_by_price]
        [10.0, 20.0, 35.0]
        >>> list_of_goods_sorted_by_price = goods_manager_utils.sort_by_price_in_uah(SortType.DSC)
        >>> [good.price_in_uah for good in list_of_goods_sorted_by_price]
        [35.0, 20.0, 10.0]
        """
        if sort_type == SortType.ASC:
            list_of_goods_sorted_by_price = sorted(self.list_of_all_goods, key = lambda good: good.price_in_uah, reverse= False)
        if sort_type == SortType.DSC:
            list_of_goods_sorted_by_price = sorted(self.list_of_all_goods, key = lambda good: good.price_in_uah, reverse= True)
        return list_of_goods_sorted_by_price

    def sort_by_country_of_producing(self, sort_type):
        """
        Sorts goods list in given order, returns this list
        >>> parker_pencil = Pencil(KindOfProduct.DRAWING, 20.0, "Columbia", 3)
        >>> global_pen = Pen(KindOfProduct.DRAWING, 35.0, "Germany", 12)
        >>> child_mosaic = Mosaic(KindOfProduct.MOSAIC, 10.0, "USA", 6)
        >>> goods_list = [parker_pencil, global_pen, child_mosaic]
        >>> goods_manager_utils = GoodsManagerUtils(goods_list)
        >>> list_of_goods_sorted_by_country_of_producing = goods_manager_utils.sort_by_country_of_producing(SortType.ASC)
        >>> [good.country_of_producing for good in list_of_goods_sorted_by_country_of_producing]
        ['Columbia', 'Germany', 'USA']
        >>> list_of_goods_sorted_by_country_of_producing = goods_manager_utils.sort_by_country_of_producing(SortType.DSC)
        >>> [good.country_of_producing for good in list_of_goods_sorted_by_country_of_producing]
        ['USA', 'Germany', 'Columbia']
        """
        if sort_type == SortType.ASC:
            list_of_goods_sorted_by_country_of_producing = sorted(self.list_of_all_goods, key = lambda good: good.country_of_producing, reverse= False)
        if sort_type == SortType.DSC:
            list_of_goods_sorted_by_country_of_producing = sorted(self.list_of_all_goods, key = lambda good: good.country_of_producing, reverse= True)
        return list_of_goods_sorted_by_country_of_producing


if __name__ == '__main__':
    doctest.testmod(verbose=True)