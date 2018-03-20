class BaseConfig():
    SECRET_KEY = 'make sure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/ss_sale?charset=utf8'
    
class ProductionConfig(BaseConfig):
    pass


configs = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    }
