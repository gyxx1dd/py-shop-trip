from app.customer import Customer, Shop
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        dict_if_info = json.load(file)

    new_dict = dict_if_info["customers"]
    new_dict_of_shops = dict_if_info["shops"]

    price_of_fuel = dict_if_info["FUEL_PRICE"]

    list_of_customers = []
    list_of_shops = []

    for i in new_dict:
        list_of_customers.append(Customer(i, price_of_fuel))

    for i in new_dict_of_shops:
        list_of_shops.append(Shop(i))

    for i in list_of_customers:
        res = i.how_much_money()
        print(res)
        for shop in list_of_shops:
            result = i.full_price_of_trip(shop)
            print(f"{i.name}'s trip to the {shop.name} costs {result}")

        res = i.cheapest_shop(list_of_shops)
        check = i.have_money_for_product()
        if check is False:
            print(f"{i.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(res)
        print()
        i.cheapest_shop_for_customer.print_receipt(i)
        print()
        print(f"{i.name} rides home")
        money_left = i.how_money_have_after_shopping(
            i.cheapest_shop_for_customer
        )
        print(f"{i.name} now has {money_left} dollars\n")
