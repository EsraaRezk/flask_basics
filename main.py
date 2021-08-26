from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SECRET_KET='topsecret',
    SQLAlchemy_DATABASE_URI='<database>://<user_id>:<password>@server>/<database_name>',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

@app.route('/')
@app.route('/index')
def hello_flask():
    return 'Hello oooks'

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug = True)