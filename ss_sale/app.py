from flask import Flask
from ss_sale.config import configs
from ss_sale.models import db
from flask_login import LoginManager
from flask_migrate import Migrate
from ss_sale.models import User,Server



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    app.config['JSON_AS_ASCII']=False
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)
    login_manager.login_view = 'front.login'

def register_blueprints(app):
    from .handlers import front, admin , server, api, coin, code
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(server)
    app.register_blueprint(api)
    app.register_blueprint(coin)
    app.register_blueprint(code)
