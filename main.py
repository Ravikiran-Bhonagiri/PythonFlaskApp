from flask import Flask
from my_blueprint1 import my_blueprint1
from my_blueprint2 import my_blueprint2

app = Flask(__name__)
app.register_blueprint(my_blueprint1, url_prefix='/myblueprint1')
app.register_blueprint(my_blueprint2, url_prefix='/myblueprint2')

@app.route('/')
def hello():
    return 'Hello, Flask!'


if __name__ == '__main__':
    app.run()


