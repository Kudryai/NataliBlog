from wtforms import Form, StringField, TextAreaField
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField

class PostForm(Form):
    title = StringField('Title')
    body = CKEditorField('Body')
    