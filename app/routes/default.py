from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/coursehome')
def coursehome():
    return render_template('coursehome.html')

@app.route('/unit1')
def unit1():
    return render_template('unit1.html')