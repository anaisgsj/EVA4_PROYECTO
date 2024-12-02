EVA4 Backend
Descripción de la aplicación

EVA4 Backend es una aplicación web desarrollada en Python utilizando el framework Django. 
Está diseñada para gestionar proyectos, o proveer una API REST para
El proyecto incluye conexión a base de datos, endpoints API.

La aplicación se despliega de forma pública en Render y permiteadministrar de manera eficiente proyectos y tareas asociadas. 
Está construida con una arquitectura moderna que separa el front-end y el back-end, permitiendo una experiencia de usuario fluida e interactiva.
Características Principales

    CRUD de Proyectos:
        Crear nuevos proyectos.
        Consultar la lista de proyectos existentes.
        Actualizar información de un proyecto.
        Eliminar proyectos que ya no sean necesarios.

    Interfaz Intuitiva:
        El front-end, desarrollado con HTML, CSS y JavaScript, proporciona una experiencia visual y accesible para los usuarios.
        Uso de fetch para realizar solicitudes HTTP a la API de manera asíncrona.

    API RESTful:
        El back-end expone una API que permite la gestión de proyectos.
        La API incluye endpoints específicos para operaciones como creación, lectura, actualización y eliminación de proyectos.

    Comunicación Front-End y API:
        El front-end interactúa con la API utilizando métodos HTTP como GET, POST, PUT y DELETE.
        Se utilizan fetch en JavaScript para manejar las solicitudes, asegurando una integración ágil y sin interrupciones.
---

Instrucciones para ejecutar el proyecto localmente

Requisitos previos

Asegúrate de tener instalados los siguientes programas:
- Python 3.9 o superior
- Pip (gestor de paquetes de Python)
- Git (opcional, si planeas clonar el repositorio)
- Virtualenv (opcional, para crear un entorno virtual)

Pasos para la ejecución local

Configuración inicial

Este proyecto requiere Python 3.9 o superior para ejecutarse correctamente. Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto.

    Clonar el repositorio
    Descarga el proyecto desde el repositorio de GitHub para trabajar con los archivos de la aplicación.

    Crear un entorno virtual (opcional)
    Configurar un entorno virtual permite mantener las dependencias organizadas y evita conflictos con otros proyectos en tu sistema.

    Instalar las dependencias
    Se utiliza el archivo requirements.txt para instalar todas las librerías necesarias para el proyecto, incluyendo Django y otras dependencias.

    Configurar las variables de entorno
    El proyecto utiliza un archivo .env para definir configuraciones clave como la SECRET_KEY, el estado de depuración (DEBUG), los hosts permitidos (ALLOWED_HOSTS), y la configuración de la base de datos (DATABASE_URL).

    URL pública del despliegue en Render

El proyecto está desplegado públicamente en Render. Puedes acceder a la aplicación en la siguiente URL:


