from flask import Flask, render_template

app = Flask(__name__)

# передаем длину введенной сторки


@app.route('/str/<some_str>')
def get_str(some_str):
    context = {
        'title': 'lesson 1',
        'result': len(some_str),
    }
    return render_template('index.html', context=context)


@app.route('/')
def hello_world():
    context = {
        'title': 'Моя первая страница',
        'p1': 'Hello world'
    }
    return render_template('index.html', context=context)


@app.route('/students/')
def student():
    context = {
        'name': ['Alexander', 'Andrey', 'Anastasia'],
        'surname': ['Ivanov', 'Petrov', 'Belova'],
        'age': ['35', '27', '36'],
        'average': ['4.6', '5.7', '5.0']
    }
    return render_template('index.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)

