#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>", 200

@app.route("/print/<string:string>")
def print_string(string):
    print(string)
    return string

@app.route("/count/<int:number>")
def count(number):
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    return count;

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = 1.0
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = float(num1) / float(num2)
    elif operation == "%":
        result = num1 % num2
    return str(result)


if __name__ == '__main__':
    app.run()
