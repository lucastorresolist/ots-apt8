from Back.models.model_products import Product


ROOT = 'Data/products.txt'


def save_product(product: Product):
    try:
        data = f'{0};{product.name};{product.description};{product.price}\n'
        with open(ROOT, 'a') as file_product:
            file_product.write(data)
        return True
    except Exception as e:
        return False


def list_products():
    list_prod = []
    with open(ROOT, 'r') as file_prod:
        for f in file_prod:
            result = f.strip().split(';')
            product = Product(result[1], result[2], result[3], result[0])
            list_prod.append(product)
    return list_prod
