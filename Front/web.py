from flask import Flask, render_template, request

from Back.archive import *
from Back.logfile import *

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index() -> None:
        saved = None
        input_name = request.args.get('input_name')
        input_description = request.args.get('input_description')
        input_price = request.args.get('input_price')

        if (input_name is not None) and (input_description is not None):
            if input_price is not None:
                write("../Data/product.txt", f"{input_name};{input_description};{input_price}")
                save_log(f"Product inserted - Name: {input_name}; Description: {input_description}; "
                         f"Price: {input_price}")
                saved = "Product"
            else:
                write("../Data/marketplaces.txt", f"{input_name};{input_description}")
                save_log(f"Marketplace inserted - Name: {input_name}; Description: {input_description}; ")
                saved = "Marketplace"

        return render_template('index.html', saved=saved)


    @app.route('/insert-marketplace')
    def insert_marketplace():
        return render_template('insert_marketplace.html')


    @app.route('/insert-product')
    def insert_product():
        return render_template('insert_product.html')

    app.run(debug=True)
