from Back.models.model_sellers import Seller


root = 'Data/sellers.txt'

def save_seller(seller:Seller) -> None:
    try:
        data = f'{seller.name};{seller.phone};{seller.email}\n'
        with open(root, 'a') as file_seller:
            file_seller.write(data) 
        return True
    except Exception as e:
        return False

def list_sellers():
    list_seller = []
    with open(root, 'r') as file_seller:
        for f in  file_seller:
            temp_seller = f.strip().split(';')
            seller = Seller(temp_seller[0], temp_seller[1], temp_seller[2])
            list_seller.append(seller)
    return list_seller
