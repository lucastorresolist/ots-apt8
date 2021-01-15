import sys
sys.path.append('.')
from Back.models.model_categories import Category
from Back.models.model_products import Product
from Back.models.model_sellers import Seller
from Back.models.model_marketplaces import Marketplace
from Back.controller.controller_sellers import *
from Back.controller.controller_products import ControllerProduct
from Back.controller.controller_marketplaces import *
from Back.controller.controller_logs import ControllerLog
from Back.controller.controller_categories import ControllerCategory
from flask import Flask, render_template, request, redirect


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index() -> None:
        return render_template('index.html')

    @app.route('/insert_category')
    def category_created():
        if request.args:
            name = request.args.get('name')
            description = request.args.get('description')
            category = Category(name, description)
            ControllerCategory(Log('Saved', 'Category')).create(category)
            saved = "Category"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_category.html')

    @app.route('/update_category')
    def update_category():
        msg = ''
        if request.args:
            id = request.args.get('id')
            print(id)
            name = request.args.get('name')
            description = request.args.get('description')
            if id is not None and name is None:
                category = ControllerCategory().read_by_id(id)
                return render_template("update_category.html", id_=id, name_=category.name, description_=category.description)
            category = Category(name, description, id)
            if ControllerCategory(Log('Update', 'Category')).update(category):
                msg = "Categoria atualizada com sucesso!"
                return render_template("update_category.html", message=msg)
            else:
                msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
                return render_template("update_category.html", message=msg)
        return render_template("update_category.html")

    @app.route('/list_categories')
    def list_categories():
        msg = ''
        if request.args:
            id = request.args.get('id')
            if id is not None:
                if ControllerCategory(Log('Delete', 'Category')).delete(id):
                    msg = "Categoria deletada com sucesso!"
                else:
                    msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
        categories = ControllerCategory(Log('Listed', 'Category')).read_all()
        return render_template("list_categories.html", categories=categories, message=msg)

    @app.route('/list_logs')
    def listed_log():
        list_log = ControllerLog().read_all()
        return render_template('list_logs.html', list=list_log)

    @app.route('/insert_marketplace')
    def insert_marketplace():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            marketplace = Marketplace(input_name, input_description)
            save_mkp(marketplace)
            saved = "Marketplaces"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_marketplace.html')

    @app.route('/list_mktplaces')
    def list_mktplaces():
        mktplaces = list_mkp()
        return render_template("list_mktplaces.html", mktplaces=mktplaces)

    @app.route('/update_marketplace/<id>')
    def update_marketplace(id):
        marketplace = get_mkp_by_id(id)
        if request.args:
            new_name = request.args.get('input_name')
            new_description = request.args.get('input_description')
            marketplace = Marketplace(new_name, new_description, id)
            update_mkp(marketplace)
            return redirect("/list_mktplaces")
        return render_template('update_marketplace.html', marketplace=marketplace)

    @app.route("/delete_marketplace/<int:id>")
    def delete_marketplace(id):
        delete_mkp(id)
        return redirect('/list_mktplaces')

    @app.route('/insert_product')
    def insert_product():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            input_price = request.args.get('input_price')
            product = Product(input_name, input_description, input_price)
            ControllerProduct(Log('Saved', 'Product')).create(product)
            saved = "Product"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_product.html')

    @app.route('/update_product')
    def update_products():
        msg = ''
        if request.args:
            id = request.args.get('id')
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            input_price = request.args.get('input_price')
            if id is not None and input_name is None:
                product = ControllerProduct().read_by_id(id)
                return render_template("update_product.html", id_=id, name=product.name, description=product.description, price=product.price)
            product = Product(input_name, input_description, input_price, id)
            if ControllerProduct(Log('Update', 'Product')).update(product):
                msg = "Produto atualizada com sucesso!"
                return render_template("update_product.html", message=msg)
            else:
                msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
                return render_template("update_product.html", message=msg)
        return render_template("update_product.html")

    @app.route('/list_products')
    def list_products():
        msg = ''
        if request.args:
            id = request.args.get('id')
            if id is not None:
                if ControllerProduct(Log('Delete', 'Product')).delete(id):
                    msg = "Produto deletado com sucesso!"
                else:
                    msg = "Ops, tivemos um problema. Tente novamente mais tarde!"
        products_list = ControllerProduct(Log('Listed', 'Product')).read_all()
        return render_template("list_products.html", products=products_list, message=msg)

    @app.route("/insert_seller")
    def insert_sellers():
        if request.args:
            input_name = request.args.get('name')
            input_phone = request.args.get('phone')
            input_email = request.args.get('email')
            seller = Seller(input_name, input_phone, input_email)
            save_sell(seller)
            saved = "Seller"
            return render_template('inserted.html', saved=saved)
        return render_template("insert_seller.html")

    @app.route("/list_sellers")
    def list_sellers():
        sellers = list_sell()
        return render_template("list_sellers.html", sellers=sellers)

    @app.route("/update_seller/<int:id>")
    def update_seller(id):
        seller = get_seller_by_id(id)
        if request.args:
            new_name = request.args.get('name')
            new_phone = request.args.get('phone')
            new_email = request.args.get('email')
            seller = Seller(new_name, new_phone, new_email, id)
            update_sell(seller)
            return redirect('/list_sellers')
        return render_template("update_seller.html", seller=seller)

    @app.route("/delete_seller/<int:id>")
    def delete_seller(id):
        delete_sell(id)
        return redirect('/list_sellers')

    @app.route('/inserted')
    def inserted():
        return render_template("inserted.html", saved=saved)

    app.run(debug=True)
