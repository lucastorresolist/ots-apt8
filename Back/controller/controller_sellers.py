from Back.dao_txt.dao_sellers import save_seller, list_sellers

def save_sell(name: str, phone: str, email: str) -> None:
    save_seller(name, phone, email)

def list_sell() -> list:
    list_sel = list_sellers()
    return list_sel
