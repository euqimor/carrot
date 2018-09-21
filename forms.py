from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class InputForm(FlaskForm):
    name_1 = StringField('Юзер 1')
    val_1 = IntegerField('Сумма 1', validators=[DataRequired(),NumberRange(0,999999999)])
    name_2 = StringField('Юзер 2')
    val_2 = IntegerField('Сумма 2', validators=[DataRequired(),NumberRange(0,999999999)])
    name_3 = StringField('Юзер 3')
    val_3 = IntegerField('Сумма 3', validators=[DataRequired(),NumberRange(0,999999999)])
    name_4 = StringField('Юзер 4')
    val_4 = IntegerField('Сумма 4', validators=[DataRequired(),NumberRange(0,999999999)])
    submit = SubmitField('Клац')