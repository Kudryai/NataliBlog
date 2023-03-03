import os

from flask import render_template, request, send_from_directory, url_for
from flask_ckeditor import upload_fail, upload_success

from app import app, current_user
from models import Post


@app.route("/")
def index():
    q = request.args.get("q")
    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        posts = Post.query.filter(
            Post.title.contains(q) | Post.body.contains(q)
        )  # .all()
        pages = posts.paginate(page=page, per_page=5)
        return render_template("posts/index.html", posts=posts, pages=pages)
    else:
        posts = Post.query.order_by(Post.created.desc())
    if "AnonymousUser" in str(current_user):
        return render_template("index.html")
    return render_template("index.html", cnt=len(current_user.lessons))


@app.route("/contact")
def contact():
    if "AnonymousUser" in str(current_user):
        return render_template("contact.html")
    return render_template("contact.html", cnt=len(current_user.lessons))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/static/image/<path:filename>")
def uploaded_files(filename):
    path = "static/image/"
    return send_from_directory(path, filename)


@app.route("/upload", methods=["POST"])
def upload():
    f = request.files.get("upload")
    extension = f.filename.split(".")[-1].lower()
    if extension not in ["jpg", "gif", "png", "jpeg"]:
        return upload_fail(message="Image only!")
    f.save(os.path.join("./static/image/", f.filename))
    url = url_for("uploaded_files", filename=f.filename)
    return upload_success(url, filename=f.filename)
