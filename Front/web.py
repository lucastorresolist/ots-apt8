from flask import Flask, render_template, request
import sys

sys.path.append('f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla2\ots-apt9')

from Back.archive import *
from Back.logfile import *
from Back.products_listing import *

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    @app.route('/')
    def index() -> None:
        return render_template('index.html')


    @app.route('/insert-marketplace')
    def insert_marketplace():
        return render_template('insert_marketplace.html')


    @app.route('/insert-product')
    def insert_product():
        return render_template('insert_product.html')


    @app.route('/inserted')
    def inserted():
        saved = None
        input_name = request.args.get('input_name')
        input_description = request.args.get('input_description')
        input_price = request.args.get('input_price')

        if (input_name is not None) and (input_description is not None):
            if input_price is not None:
                write("f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla2\ots-apt9\Data\product.txt", f"{input_name};{input_description};{input_price}")
                save_log(f"Product inserted - Name: {input_name}; Description: {input_description}; "
                         f"Price: {input_price}")
                saved = "Product"
            else:
                write("f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla2\ots-apt9\Data\marketplaces.txt", f"{input_name};{input_description}")
                save_log(f"Marketplace inserted - Name: {input_name}; Description: {input_description}; ")
                saved = "Marketplace"
        return render_template("inserted.html", saved=saved)
    
    @app.route('/products')
    def products():
        products_list = list_products("f:\projetos\olistprojetos\marketplacesduplas\marketplace-dupla2\ots-apt9\Data\product.txt")
        save_log(f"Products listed")
        return render_template("products.html", products=products_list)

    app.run(debug=True)
