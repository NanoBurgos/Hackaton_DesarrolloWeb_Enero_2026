import sqlite3
import pandas as pd
import os

DB_NAME = "negocios.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def db_init():
    conn = conectar()
    cursor = conn.cursor()

 # Tabla Negocios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS negocios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        direccion TEXT,
        tiene_web INTEGER,
        categoria TEXT,
        rating REAL,
        telefono TEXT,
        lat REAL,
        lon REAL,
        status TEXT DEFAULT 'Pendiente'
    )
    """)

    # Tabla Usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'freelancer'
    )
    """)