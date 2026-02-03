from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user
from app.models.database import obtener_negocios, guardar_negocio, exportar_csv
from app.services.google_places import buscar_negocios

# Blueprint principal de la aplicación
# Contiene las rutas principales y funcionalidades centrales
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    # Verifica si se debe mostrar el resultado de una búsqueda
    show_results = request.args.get('show', '0') == '1'

    # Obtiene los negocios solo si se solicitó mostrar resultados
    negocios = obtener_negocios() if show_results else []

    # Renderiza la vista principal con los datos obtenidos
    return render_template('index.html', negocios=negocios)


@main_bp.route('/limpiar')
@login_required
def limpiar():
    # Conecta a la base de datos
    from app.models.database import conectar
    conn = conectar()

    # Elimina todos los registros de negocios
    conn.execute("DELETE FROM negocios")
    conn.commit()
    conn.close()

    # Redirige nuevamente a la página principal
    return redirect(url_for('main.index'))
