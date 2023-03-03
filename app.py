import datetime

from flask import Flask, redirect, render_template_string, request, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditor
from flask_mailman import Mail
from flask_migrate import Migrate
from flask_security import (
    Security,
    SQLAlchemyUserDatastore,
    auth_required,
    current_user,
    hash_password,
)
from flask_security.models import fsqla_v2 as fsqla
from flask_sqlalchemy import SQLAlchemy

from config import Configuration
from forms import MyRegisterForm

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config.from_object(Configuration)
app.config["CKEDITOR_FILE_UPLOADER"] = "upload"
db = SQLAlchemy(app)
fsqla.FsModels.set_db_info(db)
migrate = Migrate(app, db)
mail = Mail(app)

from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role("admin")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("security.login", next=request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if type(model) not in (User, Lessons):
            model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    @expose("/")
    def index(self):
        lst_lessons = Lessons.query.filter(Lessons.date_lessons >= datetime.today())
        user_name = (
            db.session.query(Lessons, User, user_lessons_m2m)
            .filter(
                User.id == user_lessons_m2m.c.user_id,
                Lessons.id == user_lessons_m2m.c.lessons_id,
            )
            .filter(Lessons.date_lessons >= datetime.today())
            .all()
        )
        print(user_name)
        return self.render("admin/index.html", lst_lessons=lst_lessons, usr=user_name)


class LessonAdminView(AdminMixin, BaseModelView):
    form_columns = ["name", "date_lessons"]


class UserAdminView(AdminMixin, BaseModelView):
    form_columns = ["username", "first_name", "last_name", "lessons"]
    column_list = [
        "username",
        "first_name",
        "last_name",
        "create_datetime",
        "update_datetime",
    ]


class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ["title", "body", "tags"]


class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ["name", "posts"]


admin = Admin(app, "VsemEng", url="/", index_view=HomeAdminView(name="Home"))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(LessonAdminView(Lessons, db.session))

# Flask-Sec ###

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=MyRegisterForm)
