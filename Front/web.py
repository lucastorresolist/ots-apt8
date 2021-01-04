from flask import Flask,render_template

if __name__ == '__main__':
    app = Flask(__name__)

    @app.route('/')
    def index() -> None:
        return render_template('index.html')
    app.run(debug = True)