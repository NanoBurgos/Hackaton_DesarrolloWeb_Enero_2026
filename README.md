# **🚀 Proyecto Hackathon 2026 – Plataforma de Búsqueda de Clientes Potenciales**

📌 **Descripción general**

Este proyecto es una aplicación web orientada a la categoría Desarrollo Web, cuyo objetivo es ayudar a freelancers (desarrolladores, diseñadores web, agencias pequeñas) a identificar clientes potenciales utilizando datos reales obtenidos desde la API oficial de Google Places.

La aplicación analiza negocios locales (por ejemplo restaurantes, comercios, servicios) y muestra información clave como:

•	Nombre del negocio

•	Dirección

•	Teléfono

•	Sitio web (si existe)

👉 El valor central del proyecto es que, cuando el campo “sitio web” aparece vacío, esto indica una oportunidad directa para el freelancer, ya que ese negocio no cuenta con presencia web y puede beneficiarse de servicios como:

•	Creación de páginas web

•	Landing pages

•	Presencia digital básica

•	Optimización online

De esta manera, la plataforma funciona como una herramienta de prospección inteligente, permitiendo a freelancers detectar oportunidades reales de negocio basadas en datos públicos y actualizados, en lugar de búsquedas manuales o aproximaciones poco precisas.
________________________________________

🏗️ **Arquitectura del proyecto**

Navegador (Frontend)

        │

        ▼

Flask (Routes / Controllers)

        │

        ├── Models (SQLite)

        └── Services (Google Places API)

                │

                ▼

        Google Places (API externa)
________________________________________

📁 **Estructura del proyecto**

Hackaton-2026_APImaps_sinAPIkey/

│

├── app/

│   ├── __init__.py        # Fábrica de la app Flask

│   │

│   ├── models/            # Acceso a base de datos

│   │   ├── database.py

│   │   └── user.py

│   │

│   ├── routes/            # Rutas / controladores

│   │   ├── auth.py

│   │   └── main.py

│   │

│   ├── services/          # Integración con APIs externas

│   │   └── google_places.py

│   │

│   ├── templates/         # Vistas HTML

│   │   ├── index.html

│   │   └── login.html

│   │

│   └── static/            # CSS

│       └── estilos.css

│

├── negocios.db            # Base de datos SQLite

├── requirements.txt       # Dependencias

├── run.py                 # Punto de entrada

└── README.md
________________________________________

⚙️ **Requisitos previos**

Antes de ejecutar el proyecto, asegurate de tener instalado:

•	Python 3.10 o superior

•	pip (incluido con Python)

•	Una API Key válida de Google Places
________________________________________

🔑 **Configuración de la API Key (IMPORTANTE)**

⚠️ La API Key NO está incluida en el repositorio por seguridad.

**Paso 1:** Crear la variable de entorno

En tu sistema operativo, crear una variable de entorno llamada:
GOOGLE_API_KEY

Con el valor de tu API Key de Google.

En Windows (PowerShell):

                setx GOOGLE_API_KEY "TU_API_KEY_AQUI"

En Linux / macOS:

                export GOOGLE_API_KEY="TU_API_KEY_AQUI"

Luego de configurarla, cerrar y volver a abrir la terminal.
________________________________________

▶️ **Cómo ejecutar el proyecto en cualquier máquina**

1️⃣ Clonar el repositorio

                git clone https://github.com/tu-usuario/tu-repositorio.git
                
                cd tu-repositorio
________________________________________

2️⃣ Crear un entorno virtual (recomendado)
                        
                python -m venv .venv

Activar el entorno:

•	Windows:
                
                .venv\Scripts\activate

•	Linux / macOS:
        
                source .venv/bin/activate
________________________________________

3️⃣ Instalar dependencias

                pip install -r requirements.txt
________________________________________

4️⃣ Ejecutar la aplicación

                python run.py

La aplicación estará disponible en:

                http://localhost:5000
________________________________________

🔐 **Autenticación**

•	El sistema incluye una pantalla de login.

•	Los usuarios se validan contra una base de datos SQLite 

•	La sesión se maneja mediante cookies firmadas por Flask.

⚠️ Para fines de hackathon, las contraseñas no están hasheadas. Esto es justificable como MVP.
________________________________________

🛡️ **Seguridad**

Buenas prácticas aplicadas:

•	✅ API Key almacenada en variables de entorno

•	✅ Clave sensible fuera del repositorio

•	✅ Frontend sin acceso directo a Google Places

•	✅ Separación de responsabilidades
________________________________________

📌 Proyecto desarrollado con fines educativos y de competencia (Hackathon 2026).
