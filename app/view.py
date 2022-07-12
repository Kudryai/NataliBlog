from flask import render_template
from app import app
from models import Post
from flask import request
from posts.forms import PostForm


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
