import configuration
import requests
import data


# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# Функция получения заказа по треку
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params={'t': track})

