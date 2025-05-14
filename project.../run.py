from app import create_app, db
from app.models.cita import Cita
from app.models.usuario import Usuario
import os

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Proporciona contexto adicional para el shell de Flask"""
    return {
        'db': db,
        'Cita': Cita,
        'Usuario': Usuario,
        # Puedes agregar más modelos aquí según crezca tu aplicación
    }

if __name__ == '__main__':
    # Configura el puerto y host para el entorno de desarrollo
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)