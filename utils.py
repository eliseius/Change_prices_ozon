def process_data(data):
    data_list = data.split(sep=';')
    dict_data = {
        'offer_id': data_list[0],
        'price': data_list[1],
        'old_price': data_list[2],
        'min_price': data_list[3]
    }
    return dict_data
