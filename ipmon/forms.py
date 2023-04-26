'''Web Forms'''
import os
import sys

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')
from ipmon import config


class FirstTimeSetupForm(FlaskForm):
    password_policy = 'Password Policy: Minimum Length ({}), Minimum Uppercase ({}), Minimum Non-Letters ({}).'.format(
        config['Password_Policy']['Length'],
        config['Password_Policy']['Uppercase'],
        config['Password_Policy']['Nonletters']
    )
    username = StringField('Nombre de Usuario', validators=[DataRequired(message="Nombre de Usuario requerido")])
    email = StringField('Email', validators=[DataRequired(message="Email requerido"), Email(message="Invalid email address")])
    password = PasswordField('Contraseña', description=password_policy, validators=[DataRequired(message="Contraseña requerida")])
    verify_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Verificación contraseña  requerida")])
    poll_interval = IntegerField('Intervalo de consultas (segundos)', validators=[DataRequired(message="Intervalo de consultas requerido")])
    retention_days = IntegerField('Tiempo de almacenamiento de información (Días)', validators=[DataRequired(message="Tiempo de almacenamiento requerido")])
    enable_smtp = BooleanField('Enable SMTP Alerts')
    smtp_server = StringField('Servidor')
    smtp_port = StringField('Puerto')
    smtp_sender = StringField('Dirección remitente')
    submit = SubmitField('Enviar')


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(message="Nombre de Usuario requerido")])
    password = PasswordField('Contraseña', validators=[DataRequired(message="Contraseña requerida")])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Iniciar Sesión')


class UpdatePasswordForm(FlaskForm):
    desc = 'Password Policy: Minimum Length ({}), Minimum Uppercase ({}), Minimum Non-Letters ({}).'.format(
        config['Password_Policy']['Length'],
        config['Password_Policy']['Uppercase'],
        config['Password_Policy']['Nonletters']
    )
    current_password = PasswordField('Current Password', validators=[DataRequired(message="Current password required")])
    new_password = PasswordField('New Password', description=desc, validators=[DataRequired(message="New password required")])
    verify_password = PasswordField('Verify Password', validators=[DataRequired(message="Password verification required")])
    submit = SubmitField('Update')


class UpdateEmailForm(FlaskForm):
    email = StringField('New Email Address', validators=[DataRequired(message="Email address required"), Email(message="Invalid email address")])
    email_verify = StringField('Verify Email Address', validators=[DataRequired(message="Verify Email address required"), Email(message="Invalid email address")])
    password = PasswordField('Password', validators=[DataRequired(message="Password required")])
    submit = SubmitField('Update')


class SmtpConfigForm(FlaskForm):
    server = StringField('Server', validators=[DataRequired(message="Server required")])
    port = IntegerField('Port', validators=[DataRequired(message="Port required"), NumberRange(min=0, message="Invalid port number")])
    sender = StringField('Sender Address', validators=[DataRequired(message="Sender address required"), Email(message="Invalid email address")])
    submit = SubmitField('Update')


class AddHostsForm(FlaskForm):
    ip_address = TextAreaField('Dirección IP', validators=[DataRequired(message="IP Address required")])
    submit = SubmitField('Agregar')


class SelectThemeForm(FlaskForm):
    theme = SelectField('Tema', config['Web_Themes'].items())
    submit = SubmitField('Update')


class PollingConfigForm(FlaskForm):
    interval = StringField('Intervalo de consultas')
    retention_days = StringField('Días de almacenamiento de consultas')
    submit = SubmitField('Actualizar')
