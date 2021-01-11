def list_products(path):
    arquivo = open(path, 'r')

    products_list = []

    for data in arquivo.readlines():
        clean_data = data.strip("\n").split(";")
        product = {"name": clean_data[0], "description": clean_data[1], "price":clean_data[2]}
        products_list.append(product)

    arquivo.close()

    return products_list