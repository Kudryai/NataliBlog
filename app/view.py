from flask import render_template
from app import app
from flask import render_template
from models import Post

@app.route('/')
def index():
    name = 'Алексей'
    return render_template('index.html', n = name)