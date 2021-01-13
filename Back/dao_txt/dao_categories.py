from Back.models.model_categories import Category


ROOT = 'Data/categories.txt'


def save_category(category: Category) -> None:
    try:
        data = f'{0};{category.name};{category.description}\n'
        with open(ROOT, 'a') as file_category:
            file_category.write(data)
        return True
    except Exception as e:
        return False


def list_categories():
    list_category = []
    with open(ROOT, 'r') as file_category:
        for f in file_category:
            result = f.strip().split(';')
            category = Category(result[1], result[2], result[0])
            list_category.append(category)
    return list_category
