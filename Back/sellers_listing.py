def list_sellers(path):
    arquivo = open(path, 'r')

    sellers_list = []

    for data in arquivo.readlines():
        clean_data = data.strip().split(";")
        seller = {"name": clean_data[0], "phone": clean_data[1], "email":clean_data[2]}
        sellers_list.append(seller)

    arquivo.close()

    return sellers_list