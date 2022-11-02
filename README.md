Crear entorno virtual para python

 1. Iniciar entorno virtual en el directorio:
    py -m venv .
 2. Dar permisos al directorio para activar el entorno virtual y descargar paquetes:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
 3. Activar entorno virtual
    .\Scripts\activate

Instalaciónd de librerias

    - pip install pygame
    - pip install kivy