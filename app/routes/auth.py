from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

# Rutas de autenticación
auth_bp = Blueprint('auth', __name__)

# Login de usuario (GET: formulario, POST: procesa datos)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        from app.models.user import User
        username = request.form.get('username')

        # Login simplificado solo para demo
        if username == 'admin':
            user = User("1", "admin", "admin")
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html')

# Logout de usuario
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))