from Back.models.model_marketplaces import Marketplace


root = 'Data/marketplaces.txt'

def save_mkplace(marketplace:Marketplace) -> None:
    try:
        data = f'{marketplace.name};{marketplace.description}\n'
        with open(root, 'a') as file_mkp:
            file_mkp.write(data)
        return True
    except Exception as e:
        return False

def list_mkplaces():
    list_mkp = []
    with open(root, 'r') as file_mkp:
        for f in  file_mkp:
            temp_mkp = f.strip().split(';')
            mkp = Marketplace(temp_mkp[0], temp_mkp[1])
            list_mkp.append(mkp)
    return list_mkp
