from datetime import datetime

from flask import Flask, request, session, g
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SECRET_KEY='topsecret',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:kony2012@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
db = SQLAlchemy(app)

@app.before_request
def func():
    g.string = '<br> This code runs before any request'

@app.route('/')
@app.route('/index')
def hello_flask():
    return 'Hello oooks <br>' + g.string

@app.route('/new/')
def query_string(greeting = 'hello'):
    query_string = request.args.get('greeting',greeting)
    return "<h1>The Greeting is: {0}</h1>".format(query_string)

@app.route('/user')
@app.route('/user/<name>')
def no_query(name = "oooky"):
    return "<h1>Hello user! {}</h1>".format(name)

@app.route('/numbers/<int:num>')
def integer(num):
    return "<h1>Hello user! {}</h1>".format(str(num))


@app.route('/temp/')
def temp():
    return render_template('temp.html')

@app.route('/movies')
def movies():
    movie_list = [
        'harry potter and the half blood prince',
        'Fried GreenTomatoes',
        'The baby-sitters club'
    ]
    return render_template('movies.html', movies=movie_list, name='Esraa')

@app.route('/dur')
def durations():
    movie_list = {
        'harry potter and the half blood prince':1.4,
        'Fried GreenTomatoes':2,
        'The baby-sitters club':4.3
    }
    return render_template('durations.html', movies=movie_list, name='Esraa')
@app.route('/filters')
def filters():
    movie_list = {
        'harry potter and the half blood prince': 1.4,
        'Fried GreenTomatoes': 2,
        'The baby-sitters club': 4.3
    }
    return render_template('filter-data.html', movies=movie_list, name=None, film="a christmas charol")

@app.route('/macros')
def macros():
    movie_list = {
        'autopsy of jane doe': 02.14,
        'neon demon': 3.20,
        'ghost in a shell': 1.50,
        'kong: skull island': 3.50,
        'john wick 2': 02.52,
        'spiderman - homecoming': 1.48
    }
    return render_template('using_macros.html', movies=movie_list)


@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'harry'
    return render_template('session.html', session=session, name=session['name'])


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Name is {}'.format(self.name)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)