from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # validate_on_submit return false if call GET.
    if form.validate_on_submit():
        # show a message. must be handled in html files (look at base.html) 
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        # best way use url
        return redirect(url_for('index'))   
    return render_template('login.html', title='Sign In', form=form)

