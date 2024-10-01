from flask import render_template
from flask_login import login_required
from . import dashboard
from gerenciador.models import Cliente, Financeiro
from gerenciador import db

@dashboard.route('/')
@login_required
def index():
    # Obter os dados reais do banco de dados
    total_clientes = Cliente.query.count()
    clientes_ativos = Cliente.query.filter_by(status='Ativo').count()
    clientes_esgotados = Cliente.query.filter_by(status='Esgotado').count()

    # Obter dados financeiros
    lucro = db.session.query(db.func.sum(Financeiro.lucro)).scalar() or 0
    entrada = db.session.query(db.func.sum(Financeiro.entrada)).scalar() or 0
    despesas = db.session.query(db.func.sum(Financeiro.despesas)).scalar() or 0

    return render_template('dashboard.html',
                           total_clientes=total_clientes,
                           clientes_ativos=clientes_ativos,
                           clientes_esgotados=clientes_esgotados,
                           lucro=lucro,
                           entrada=entrada,
                           despesas=despesas)
