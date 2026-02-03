from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

# Rutas de autenticación
auth_bp = Blueprint('auth', __name__)