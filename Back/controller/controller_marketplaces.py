from Back.dao_db.dao_marketplaces import save_mkplace, list_mkplaces

def save_mkp(name: str, description: str) -> None:
    save_mkplace(name, description)

def list_mkp() -> list:
    list_mkp = list_mkplaces()
    return list_mkp
