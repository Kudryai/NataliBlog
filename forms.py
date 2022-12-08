from flask_security import RegisterForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError

import app


class MyRegisterForm(RegisterForm):
    first_name = StringField("Имя", [DataRequired()])
    last_name = StringField("Фамилия", [DataRequired()])
    email = StringField("Email", [DataRequired()])

    def validate_email(self, field) -> None:
        if app.User.query.filter_by(email=field.data).first():
            raise ValidationError("Почта уже занята")
