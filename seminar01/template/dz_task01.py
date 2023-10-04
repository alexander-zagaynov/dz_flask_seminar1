from flask import Flask, render_template

app = Flask(__name__)


@app.route('/clothes/')
def clothes():
    context = {
        'jacket': ['пальто', 'куртка', 'пуховик'],
        'cardigan': ['свитер', 'рубашка', 'кофта'],
        'footwear': ['кросовки', 'ботинки', 'полуботинки'],
        'accessories': ['шарф', 'перчатки', 'шапка']
    }
    return render_template('dz_index.py.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)