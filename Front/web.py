import sys
sys.path.append('.')
from Back.models.categories import Category
from Back.controller.controller_sellers import *
from Back.controller.controller_products import *
from Back.controller.controller_marketplaces import *
from Back.controller.controller_logs import *
from Back.controller.controller_categories import *
from flask import Flask, render_template, request


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
            save_cat(category)
            log = Log("Saved", "Category")
            save_l(log)
            saved = "Category"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_category.html')

    @app.route('/list_categories')
    def list_categories():
        categories = list_cat()
        log = Log("Listed", "Category")
        save_l(log)
        return render_template("list_categories.html", categories=categories)

    @app.route('/list_logs')
    def listed_log():
        list_log = list_l()
        return render_template('list_logs.html', list=list_log)

    @app.route('/insert_marketplace')
    def insert_marketplace():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            save_mkp(input_name, input_description)
            log = Log("Saved", "Marketplace")
            save_l(log)
            saved = "Marketplaces"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_marketplace.html')

    @app.route('/list_mktplaces')
    def list_mktplaces():
        mktplaces = list_mkp()
        log = Log("Listed", "Marketplaces")
        save_l(log)
        return render_template("list_mktplaces.html", mktplaces=mktplaces)

    @app.route('/insert_product')
    def insert_product():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            input_price = request.args.get('input_price')
            product = Product(input_name, input_description, input_price)
            save_prod(product)
            log = Log("Saved", "Product")
            save_l(log)
            saved = "Product"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_product.html')

    @app.route('/list_products')
    def list_products():
        products_list = list_prod()
        log = Log("Listed", "Products")
        save_l(log)
        return render_template("list_products.html", products=products_list)

    @app.route("/insert_seller")
    def insert_sellers():
        if request.args:
            input_name = request.args.get('name')
            input_phone = request.args.get('phone')
            input_email = request.args.get('email')
            save_sell(input_name, input_phone, input_email)
            log = Log("Saved", "Seller")
            save_l(log)
            saved = "Seller"
            return render_template('inserted.html', saved=saved)
        return render_template("insert_seller.html")

    @app.route("/list_sellers")
    def list_sellers():
        sellers = list_sell()
        log = Log("Listed", "Sellers")
        save_l(log)
        return render_template("list_sellers.html", sellers=sellers)

    @app.route('/inserted')
    def inserted():
        return render_template("inserted.html", saved=saved)

    app.run(debug=True)
