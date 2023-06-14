# Алина Кударенко, 5-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Тест 1. Успешное получение информации о заказе по треку
def test_get_order_info_get_success_response():
    # В переменную order_response сохраняется результат запроса на создание заказа
    order_response = sender_stand_request.post_new_order(data.order_body)
    # В переменную track сохраняется трек созданного заказа
    track = order_response.json()['track']
    # В переменную order_info_response сохраняется результат запроса на получение заказа по треку
    order_info_response = sender_stand_request.get_order_info(track)
    # Проверяется, что код ответа равен 200
    assert order_info_response.status_code == 200
