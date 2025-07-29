
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/<name1>/and/<name2>')
def hello_name(name1, name2):
   return name1 +' went for shopping with ' + name2


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


if __name__ == '__main__':
    app.run(debug=True)