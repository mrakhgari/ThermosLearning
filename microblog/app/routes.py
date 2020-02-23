from flask import render_template
from app import app

# when called http://127.0.0.1:5000/ or http://127.0.0.1:5000/index called this method
@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'MuhmdrezA'}
    # fake post for my user
    posts = [
        {
            'author': { 'username': 'Friend1'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'username': 'Friend2'},
            'body' : 'The Avangers movie was so cool'
        }
    ]
    # to render the index.html in template folder use this method.
    return render_template( 'index.html', title='Home', user=user, posts=posts)
