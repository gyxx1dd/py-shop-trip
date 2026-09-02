from app.shop import Shop
import math


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]
        self.fuel_price_of_1_l = 2.4
        self.cheapest_shop_for_customer = None

    def how_much_money(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def full_price_in_shop(self, shop: Shop) -> float | int:
        result = ((self.product_cart["milk"] * shop.products["milk"])
                  + (self.product_cart["bread"] * shop.products["bread"])
                  + (self.product_cart["butter"] * shop.products["butter"]))
        return round(result, 2)

    def full_price_of_trip(self, shop: Shop) -> int | float:
        price_of_product = self.full_price_in_shop(shop)
        km_to_shop = math.sqrt((shop.location[0] - self.location[0]) ** 2
                               + (shop.location[1] - self.location[1]) ** 2)
        fuel_needed = km_to_shop / 100 * self.car["fuel_consumption"]
        fuel_cost = fuel_needed * self.fuel_price_of_1_l
        result = price_of_product + fuel_cost * 2
        return round(result, 2)

    def cheapest_shop(self, shop: list[Shop]) -> str:
        my_dict = {}
        for i in range(len(shop)):
            my_dict[shop[i].name] = self.full_price_of_trip(shop[i])
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        shop_name_cheap = next(iter(sorted_dict))
        for i in shop:
            if i.name == shop_name_cheap:
                self.cheapest_shop_for_customer = i
                break
        return f"{self.name} rides to {shop_name_cheap}"

    def have_money_for_product(self) -> bool:
        how_much_need_money_for_shop = (
            self.full_price_of_trip(self.cheapest_shop_for_customer))
        if self.money < how_much_need_money_for_shop:
            return False
        return True

    def how_money_have_after_shopping(self, shop: Shop) -> int:
        money_now = self.money - self.full_price_of_trip(shop)
        return round(money_now, 2)
