from app import app # import app instance from app package
from flask import render_template

# 2 routes
@app.route('/')
@app.route('/index')
# a view function
def index():
    user = {'username': 'Muguel'}
    
    posts = [
        {
            'author': {'username': 'a'},
            'body': 'What a nice day!'
        },
        {
            'author': {'username': 'b'},
            'body': '!JAJA!'
        }
    ]

    return render_template('index.html', title = 'Home', user = user, posts = posts)