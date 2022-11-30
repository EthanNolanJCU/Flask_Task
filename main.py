from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f'Hello {name}'

@app.route('/f')
@app.route('/f/<temp>')
def temp(temp=0):
    return f'{temp} Celsius = {ctof(float(temp))} Fahrenheit'


def ctof(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
