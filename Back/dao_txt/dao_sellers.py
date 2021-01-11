root = 'Data/sellers.txt'

def save_seller(name:str, phone: str, email: str) -> None:
    try:
        data = f'{name}; {phone}; {email}\n'
        file_seller = open(root, 'a')
        file_seller.write(data) 
        return True
    except Exception as e:
        return False
    finally:
        file_seller.close()


def list_sellers():
    list_seller = []
    file_seller = open(root, 'r')
    for f in  file_seller:
        seller = f.strip().split(';')
        list_seller.append(seller)
    return list_seller
