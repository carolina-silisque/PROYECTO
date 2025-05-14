from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from app import db
from app.models.cita import Cita
from app.forms.cita_form import CitaForm
from datetime import datetime

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

@citas_bp.route('/', methods=['GET', 'POST'])
def agendar():
    form = CitaForm()
    
    if form.validate_on_submit():
        # Crear una nueva cita
        cita = Cita(
            nombre=form.nombre.data,
            email=form.email.data,
            telefono=form.telefono.data,
            fecha=form.fecha.data,
            hora=form.hora.data,
            tipo_consulta=form.tipo_consulta.data,
            comentarios=form.comentarios.data
        )
        
        # Guardar en la base de datos
        db.session.add(cita)
        db.session.commit()
        
        flash('Tu cita ha sido agendada correctamente. Te contactaremos para confirmar.', 'success')
        return redirect(url_for('citas.agendar'))
    
    return render_template('citas/form.html', titulo='Agendar Cita', form=form)

@citas_bp.route('/lista')
def lista():
    # Esta ruta se podría proteger con autenticación para el personal médico
    citas = Cita.query.order_by(Cita.fecha, Cita.hora).all()
    return render_template('citas/lista.html', titulo='Lista de Citas', citas=citas)

@citas_bp.route('/<int:id>')
def detalle(id):
    # Esta ruta se podría proteger con autenticación
    cita = Cita.query.get_or_404(id)
    return render_template('citas/detalle.html', titulo='Detalle de Cita', cita=cita)

@citas_bp.route('/<int:id>/cambiar-estado/<estado>')
def cambiar_estado(id, estado):
    # Esta ruta se podría proteger con autenticación para el personal médico
    estados_validos = ['pendiente', 'confirmada', 'cancelada', 'completada']
    
    if estado not in estados_validos:
        abort(400)
    
    cita = Cita.query.get_or_404(id)
    cita.estado = estado
    db.session.commit()
    
    flash(f'El estado de la cita ha sido actualizado a: {estado}', 'success')
    return redirect(url_for('citas.lista'))

