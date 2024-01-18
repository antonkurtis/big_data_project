def make_button_lists(lst):
  lst_len = len(lst) // 3
  lst_1 = lst[:lst_len]
  lst_2 = lst[lst_len:lst_len*2]
  lst_3 = lst[lst_len*2:]

  return lst_1, lst_2, lst_3


def transfer_city_to_region(city):
  if city == 'Moscow':
    return 'Москва'
  elif city == 'St.Petersburg':
    return 'Санкт-Петербург'
  elif city == 'Kazan':
    return 'Татарстан'
  elif city == 'Krasnodar':
    return 'Краснодарский край'
  elif city == 'Ekaterinburg':
    return 'Свердловская обл.'
  elif city == 'Tumen':
    return 'Тюменская обл.'
