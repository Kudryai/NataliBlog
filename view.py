from flask import render_template
from app import app
from models import Post
from flask import request
from posts.forms import PostForm
import os
from flask import url_for,send_from_directory
from flask_ckeditor import upload_success, upload_fail

@app.route('/')
def index():    
    q = request.args.get('q')
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)) #.all()
        pages = posts.paginate(page=page, per_page = 5)
        return render_template('posts/index.html',posts=posts, pages=pages)
    else:
        posts = Post.query.order_by(Post.created.desc())
    name = 'Алексей'
    return render_template('index.html', n = name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/static/image/<path:filename>')
def uploaded_files(filename):
    path = 'static/image/'
    return send_from_directory(path, filename)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    f.save(os.path.join('./static/image/', f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url, filename=f.filename) 