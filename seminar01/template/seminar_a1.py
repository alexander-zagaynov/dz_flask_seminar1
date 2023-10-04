from flask import Flask, render_template

app = Flask(__name__)


@app.route('/mysite/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return'Мой первый сайт'


@app.route('/number/<int:a>/<int:b>/')
def number(a, b):
    return render_template("index.html", sum=a + b)


if __name__ == '__main__':
    app.run(debug=True)

