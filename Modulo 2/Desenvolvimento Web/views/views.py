from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/obras')
def obras():
    return render_template('obras.html')
