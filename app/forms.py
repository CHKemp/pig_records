from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class WeanForm(Form):
    n_weaned = IntegerField('n_weaned', validators=[DataRequired()])
    n_litters = IntegerField('n_litters', validators=[DataRequired()])

