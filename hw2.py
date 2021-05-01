import csv
import re
import datetime
import json
import yaml

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_data():
    def extract(pattern, line):
        result = re.sub(pattern, '', line)
        if result is not line:
            return result.strip('\n')
        return

    os_prod_list, os_name_list, os_code_list, os_type_list, = [], [], [], []
    row_names = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    prod_pat = re.compile(r"Изготовитель ОС:\s*")
    name_pat = re.compile(r"Название ОС:\s*")
    code_pat = re.compile(r"Код продукта:\s*")
    type_pat = re.compile(r"Тип системы:\s*")
    patterns = [prod_pat, name_pat, code_pat, type_pat]

    for _ in range(1, 4):
        results = []
        with open(f'files/info_{_}.txt', encoding='cp1251') as f:
            data = f.readlines()
        for line in data:
            for pat in patterns:
                result = extract(pat, line)
                if result:
                    results.append(result)

        os_prod, os_name, os_code, os_type = results
        os_prod_list.append(os_prod)
        os_name_list.append(os_name)
        os_code_list.append(os_prod)
        os_type_list.append(os_type)

    main_data = [row_names, os_prod_list, os_name_list, os_code_list, os_type_list]
    return main_data


def write_to_csv(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(get_data())


write_to_csv('./files/some.csv')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def write_order_to_json(item, quantity, price, buyer, date=datetime.datetime.now()):
    order = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": str(date)
    }
    with open('files/orders.json', 'w') as f:
        json.dump(order, f, indent=4)

write_order_to_json('Лейка', 1, 100, 'Виталик')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
data = {
    "key1": [str(i) + 'kek' for i in range(10)],
    "key2": 123456,
    "key3": {"€": "euro",
             "$": "dollar",
             "₽": "ruble"}
}


def write_to_yaml(data):
    with open('./files/file.yaml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def read_from_yaml(path):
    with open(path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)


write_to_yaml(data)
read_from_yaml('./files/file.yaml')
