from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    whatsapp = StringField('WhatsApp', validators=[DataRequired()])
    login = StringField('Login | E-mail', validators=[DataRequired()])
    senha = StringField('Senha', validators=[DataRequired()])
    provedor = SelectField('Serviço | Provedor', choices=[('provedor1', 'Provedor 1'), ('provedor2', 'Provedor 2')])
    plano = StringField('Plano', validators=[DataRequired()])
    fatura = SelectField('Fatura', choices=[('pago', 'Pago'), ('pendente', 'Pendente')])
    data_validade = DateField('Data de Validade', format='%d/%m/%Y', validators=[DataRequired()])
    renovacao_automatica = BooleanField('Renovação Automática')
    observacoes = StringField('Observações')
    submit = SubmitField('Salvar')
