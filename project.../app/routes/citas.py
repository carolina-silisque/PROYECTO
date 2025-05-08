from flask import Blueprint, render_template, request, flash, redirect, url_for

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

@citas_bp.route('/', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        tipo_consulta = request.form.get('tipo_consulta')
        
        # Aquí normalmente guardarías la cita en una base de datos
        # Por ahora, solo mostraremos un mensaje de éxito
        
        flash('Tu cita ha sido agendada correctamente. Te contactaremos para confirmar.', 'success')
        return redirect(url_for('citas.agendar'))
        
    return render_template('citas.html', titulo='Agendar Cita')
