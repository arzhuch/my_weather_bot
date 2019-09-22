import json


def get_city_id_by_name(city_name, city_list_file='city.list.json'):
    def get_city_id():
        with open(city_list_file) as city_lst_file:
            city_list = json.load(city_lst_file)
        for record in city_list:
            if record['name'] == city_name:
                local_city_id = (record['id'])
                return local_city_id

    city_id = get_city_id()
    return city_id


def city_checker(city_name):
    with open('city.list.json') as city_lst_file:
        city_list = json.load(city_lst_file)
        names = []
    for record in city_list:
        names.append(record['name'])
    if city_name in names:
        return "OK"
    else:
        return None
