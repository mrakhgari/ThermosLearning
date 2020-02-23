from flask import render_template
from app import app

# when called http://127.0.0.1:5000/ or http://127.0.0.1:5000/index called this method
@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'MuhmdrezA'}
    # to render the index.html in template folder use this method.
    return render_template( 'index.html', title='Home', user=user)
