from mail import Mailing
from address import Address
to_address = Address(420145, "Казань", "Баумана", 48, 25)
from_address = Address(458952, "Саратов", "Горная", 58, 36)
cost = 4589
track = 111111

new_mailing = Mailing(to_address, from_address, cost, track)
print(
    "Отправление",
    new_mailing.track,
    "из",
    new_mailing.from_address.index,
    ",",
    new_mailing.from_address.city,
    ",",
    new_mailing.from_address.street,
    ",",
    new_mailing.from_address.house,
    "-",
    new_mailing.from_address.flat,
    "в",
    new_mailing.to_address.index,
    ",",
    new_mailing.to_address.city,
    ",",
    new_mailing.to_address.street,
    ",",
    new_mailing.to_address.house,
    "-",
    new_mailing.to_address.flat,
    ". Стоимость",
    new_mailing.cost,
    "рублей.")
