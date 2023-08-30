from db.models import Price


def get_prices_for_change():
    query = Price.query

    if query:
        product_prices = []
        for element in query:
            one_product = {
            'offer_id': element.offer_id,
            'price': element.price,
            'old_price': element.old_price,
            'min_price': element.min_price,
            'rate': element.rate
            }
            product_prices.append(one_product)
        return product_prices
    else:
        return None


if __name__ == '__main__':
    print(get_prices_for_change())
  