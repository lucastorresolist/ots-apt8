from flask import Flask, render_template, request

import sys
sys.path.append('.')

from Back.archive import *
from Back.log import *
from Back.controller.controller_categories import *
from Back.controller.controller_logs import *
from Back.controller.controller_marketplaces import *
from Back.controller.controller_products import *
from Back.controller.controller_sellers import *


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index() -> None:
        return render_template('index.html')


    @app.route('/create_category')
    def category_created():
        if request.args:
            name = request.args.get('name')
            description = request.args.get('description')
            save_category(name, description)
            save_l("Saved", "Category")
            saved = "Category"
            return render_template("inserted.html", saved=saved)
        return render_template('category.html')

    @app.route('/list_category')
    def category_listed():
        categories = list_cat()
        save_l("Listed", "Category")
        return render_template("list_category.html", categories=categories)


    @app.route('/insert-marketplace')
    def insert_marketplace():
        if request.args:
            input_name = request.args.get('input_name')
            input_description = request.args.get('input_description')
            save_mkp(input_name, input_description)
            save_l("Saved", "Marketplace")
            saved = "Marketplaces"
            return render_template("inserted.html", saved=saved)
        return render_template('insert_marketplace.html')


    @app.route('/mktplaces_list')
    def list_mktplaces():
        mktplaces = list_mkp()
        save_l("Listed", "Marketplaces")
        return render_template("mktplaces_list.html", mktplaces=mktplaces)
    

    @app.route('/insert-product')
    def insert_product():
        return render_template('insert_product.html')


    @app.route('/inserted')
    def inserted():
        saved = None
        # input_name = request.args.get('input_name')
        # input_description = request.args.get('input_description')
        input_price = request.args.get('input_price')

        if (input_name is not None) and (input_description is not None):
            if input_price is not None:

                write("../Data/products.txt", f"{input_name};{input_description};{input_price}")
                save_log(f"Product inserted - Name: {input_name}; Description: {input_description}; "
                         f"Price: {input_price}", "create")
                saved = "Product"
            else:
                write("../Data/marketplaces.txt", f"{input_name};{input_description}")
                save_log(f"Marketplace inserted - Name: {input_name}; Description: {input_description}; ", "create")

                write("./Data/products.txt", f"{input_name};{input_description};{input_price}")
                save_log(f"Product - Name: {input_name}; Description: {input_description}; "
                         f"Price: {input_price}", "Insert")
                saved = "Product"
            # else:
            #     write("./Data/marketplaces.txt", f"{input_name};{input_description}")
            #     save_log(f"Marketplace - Name: {input_name}; Description: {input_description}; ", "Insert")

            #     saved = "Marketplace"
        return render_template("inserted.html", saved=saved)
    
    @app.route('/products')
    def products():
        products_list = list_products("./Data/product.txt")
        save_log("Products", "List")
        return render_template("products.html", products=products_list)
    
    @app.route("/insert-sellers")
    def insert_sellers():
        input_name = request.args.get('name')
        input_phone = request.args.get('phone')
        input_email = request.args.get('email')

        if input_name != None and input_phone != None and input_email != None:
            write("./Data/sellers.txt", f"{input_name};{input_phone};{input_email}")
            save_log(f"Seller - Name: {input_name}; Phone: {input_phone}; E-mail: {input_email} ", "Insert")

        return render_template("sellers.html")

    @app.route("/sellers-listing")
    def sellers_listing():
        sellers = list_sellers("./Data/sellers.txt")
        save_log("Sellers", "List")
        return render_template("seller-listing.html", sellers=sellers)


    @app.route('/logs')
    def logs():
        logs_list = read_log()
        return render_template("logs_list.html", logs_list=logs_list)




    @app.route('/log_list')
    def listed_log():
        list = read_log()
        return render_template('log_list.html', list=list)

    app.run(debug=True)

