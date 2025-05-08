from flask import Flask, render_template
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Añadir una ruta simple para pruebas
    @app.route('/test')
    def test_page():
        return "La aplicación funciona correctamente"
    
    # Registrar blueprints (rutas)
    from app.routes.inicio import inicio_bp
    from app.routes.recursos import recursos_bp
    from app.routes.recomendaciones import recomendaciones_bp
    from app.routes.citas import citas_bp
    
    app.register_blueprint(inicio_bp)
    app.register_blueprint(recursos_bp)
    app.register_blueprint(recomendaciones_bp)
    app.register_blueprint(citas_bp)
    
    return app
