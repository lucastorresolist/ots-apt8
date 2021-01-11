import re

def list_sellers(path):
    arquivo = open(path, 'r')

    sellers_list = []

    for data in arquivo.readlines():
        clean_data = data.strip().split(";")
        seller = {"name": clean_data[0], "phone": phone_format(clean_data[1]) , "email":clean_data[2]}
        sellers_list.append(seller)

    arquivo.close()

    return sellers_list

def phone_format(numero):
    print(numero)
    if numero != "":
        pattern = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
        answer = re.split(pattern,numero)
        clean_answer = list(filter(None, answer))
        print(clean_answer)

        formatted_number = f"({clean_answer[0]}){clean_answer[1]}-{clean_answer[2]}"

        return formatted_number
    else:
        return "Number not registered"
    