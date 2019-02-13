from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def hello_world():
    # user_agent = request.headers.get('User-Agent')
    # return '<h1>Hello World!</h1>' + '\n<p>Your browser is {}'.format(user_agent)
    # return redirect('http://www.example.com')
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    comments = list()
    for i in range(10):
        comments.append("comment" + str(i))
    return render_template('user.html', name=name, comments=comments)


@app.errorhandler(404)
def page_not_founde(e):
    return render_template("404.html")


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")


if __name__ == '__main__':
    app.run(debuge=True)
