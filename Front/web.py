from flask import Flask,render_template

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index() -> None:
        return render_template('index.html')

    @app.route('/insert-marketplace')
    def insert_marketplace():
        return render_template('insert_marketplace.html')


    @app.route('/insert-product')
    def insert_product():
        return render_template('insert_product.html')

    app.run(debug=True)
