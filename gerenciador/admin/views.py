from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from gerenciador import db
from gerenciador.models import User
from . import admin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, ValidationError

class CreateUserForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    confirm = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password', message='Senhas devem coincidir')])
    is_admin = BooleanField('Administrador')
    submit = SubmitField('Criar Usuário')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nome de usuário já está em uso.')

@admin.route('/admin/users', methods=['GET', 'POST'])
@login_required
def manage_users():
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('dashboard.index'))
    
    form = CreateUserForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            is_admin=form.is_admin.data
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuário criado com sucesso.')
        return redirect(url_for('admin.manage_users'))
    
    users = User.query.all()
    return render_template('manage_users.html', form=form, users=users)
