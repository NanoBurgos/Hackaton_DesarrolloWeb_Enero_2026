from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import login_required, current_user
from app.models.database import obtener_negocios, guardar_negocio, exportar_csv
from app.services.google_places import buscar_negocios

# Blueprint principal de la aplicación
# Contiene las rutas principales y funcionalidades centrales
main_bp = Blueprint('main', __name__)
