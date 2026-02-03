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

@main_bp.route('/scrapear', methods=['POST'])
@login_required
def scrapear():
    # Obtiene el texto de búsqueda desde el formulario
    query = request.form.get('query', 'restaurant in Asunción')

    # Llama al servicio externo (Google Places) para buscar negocios
    resultados = buscar_negocios(query)

    # Procesa y guarda cada resultado en la base de datos
    for lugar in resultados:
        # Extrae datos relevantes del lugar (API v1)
        nombre = lugar.get("displayName", {}).get("text", "Sin nombre")
        direccion = lugar.get("formattedAddress", "Sin dirección")
        web = lugar.get("websiteUri")  # Puede ser None

        # Guarda el negocio en la base de datos
        guardar_negocio(
            nombre=nombre,
            direccion=direccion,
            tiene_web=bool(web),
            categoria=str(lugar.get("types", [])),
            rating=lugar.get("rating"),
            telefono=None,  # No disponible en la API básica
            lat=lugar.get("location", {}).get("latitude"),
            lon=lugar.get("location", {}).get("longitude")
        )

    # Redirige al inicio mostrando los resultados
    return redirect(url_for('main.index', show='1'))


@main_bp.route('/exportar')
@login_required
def exportar():
    # Genera el archivo CSV y lo envía al usuario
    path = exportar_csv()
    return send_file(path, as_attachment=True)
