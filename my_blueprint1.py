from flask import Blueprint, render_template

my_blueprint1 = Blueprint('my_blueprint1', __name__)

@my_blueprint1.route('/')
def index():
    return 'This is the index page of my blueprint.'

@my_blueprint1.route('/about')
def about():
    return 'This is the about page of my blueprint.'

@my_blueprint1.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

