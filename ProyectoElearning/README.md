# Tercera pre-entrega Fernando Flores

## Descripción
Este proyecto es una plataforma e-learning desarrollada con Django que permite gestionar cursos, profesores y alumnos.

## Requisitos
- Python 3.8 o superior
- Django 5.0.7

## Instalación
1. Clonar el repositorio:
    '''sh
    git clone https://github.com/fernandoefrain/tercera-pre-entrega-fernando-flores.git
    '''
2. Crear y activar un entorno virtual:
    '''sh
    python -m venv entornoV
    source entornoV/bin/activate  # En Windows usa `entornoV\Scripts\activate`
    '''
3. Instalar las dependencias:
    '''sh
    pip install -r requirements.txt
    '''
4. Ejecutar las migraciones:
    '''sh
    python manage.py makemigrations
    python manage.py migrate
    '''
5. Iniciar el servidor de desarrollo:
    '''sh
    python manage.py runserver
    '''

## Funcionalidades
- **Inicio**: Muestra los cursos disponibles.
- **Buscar**: Permite buscar cursos por nombre.
- **Agregar**: Permite agregar nuevos cursos, profesores y alumnos.

## Orden para probar
1. Iniciar el servidor de desarrollo.
2. Acceder a la página principal: `http://127.0.0.1:8000/`
3. Navegar a través de las opciones del menú: Inicio, Buscar, Agregar.
