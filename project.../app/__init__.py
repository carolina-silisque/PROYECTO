from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Crear instancias de extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar blueprints (rutas)
    from app.routes.inicio import inicio_bp
    from app.routes.recursos import recursos_bp
    from app.routes.recomendaciones import recomendaciones_bp
    from app.routes.citas import citas_bp
    
    app.register_blueprint(inicio_bp)
    app.register_blueprint(recursos_bp)
    app.register_blueprint(recomendaciones_bp)
    app.register_blueprint(citas_bp)
    
    # Crear la base de datos si no existe
    with app.app_context():
        db.create_all()
    
    return app
