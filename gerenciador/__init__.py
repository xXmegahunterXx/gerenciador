from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SECRET_KEY'] = 'sua_chave_secreta'  # Substitua por uma chave secreta real
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Substitua pelo URI do seu banco de dados
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensões
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'  # Endpoint da rota de login

    # Importar e registrar blueprints
    from gerenciador.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from gerenciador.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    return app

@login_manager.user_loader
def load_user(user_id):
    from gerenciador.models import User
    return User.query.get(int(user_id))
