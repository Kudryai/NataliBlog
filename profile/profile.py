import os
from datetime import datetime, timedelta
from time import process_time_ns

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_security import current_user, login_required, roles_required
from werkzeug.utils import secure_filename

from app import db
from models import Lessons, Post, User

ALLOWED_EXTENSIONS = ["jpg", "gif", "jpeg", "png"]
profile = Blueprint(
    "profile",
    __name__,
    template_folder="templates",
)


@profile.route("/")
@login_required
def index():
    date_limit = datetime.now() - timedelta(days=10)
    posts_limit5 = Post.query.filter(Post.created > date_limit)
    lessons = current_user.lessons
    return render_template(
        "prf/index.html",
        current_user=current_user,
        posts_limit=posts_limit5,
        lessons=lessons,
        cnt=len(lessons),
    )


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route("/", methods=["GET", "POST"])
@login_required
def upload_pic():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
    if file.filename == "":
        flash("No selected file")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(
            os.path.join(
                "static/image/avatar",
                f"{current_user.id}.{file.filename.split('.')[1]}",
            )
        )
        user_pic = User.query.filter(current_user.id == User.id).first()
        user_pic.pic_url = (
            f"/static/image/avatar/{current_user.id}.{file.filename.split('.')[1]}"
        )
        db.session.add(user_pic)
        db.session.commit()
        return redirect(request.url)
