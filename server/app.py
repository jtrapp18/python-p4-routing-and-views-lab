#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return str(parameter)

@app.route('/count/<int:parameter>')
def count(parameter):
    html = ''.join([f'{i}\n' for i in range(parameter)])

    return html

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    op = "/" if operation == 'div' else operation
    val = eval(f"{num1} {op} {num2}")
    return str(val)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
