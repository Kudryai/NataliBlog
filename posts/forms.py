from wtforms import Form, StringField, TextAreaField
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms.validators import ValidationError, DataRequired


class PostForm(Form):
    title = StringField(label=('Заголовок: '),
    validators=[DataRequired()])
    body = CKEditorField('Body')
    