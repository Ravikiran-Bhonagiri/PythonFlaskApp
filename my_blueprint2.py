from flask import Blueprint, render_template

my_blueprint2 = Blueprint('my_blueprint2', __name__)

@my_blueprint2.route('/')
def index():
    return 'This is the index page of my blueprint.'

@my_blueprint2.route('/about')
def about():
    return 'This is the about page of my blueprint.'

@my_blueprint2.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

