#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

counter = 0
 
@app.route('/about')
def hello():
    return '<h3> Hello, Solntsev Vitaly!</h3>'

@app.route('/')
def print_counter():
    global counter
    return 'Counter: ' + str(counter)

@app.route('/start')
def add_count():
    global counter
    counter = counter + 1
    return 'Counter: ' + str(counter)
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')