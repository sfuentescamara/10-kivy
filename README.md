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

Help
   https://www.youtube.com/watch?v=WofR48auycs&t=0s
    
Debuger .apk
-cmd
   cd "05. Proyectos\11 kivy general\platform-tools_r27.0.0-windows\platform-tools"
   adb devices
   adb tcpip 5555
-ubuntu
   adb connect 192.168.1.133
   cd "/mnt/d/05. Proyectos/10 kivy/"
   adb -s 192.168.1.133:5555 install *
   adb -s 192.168.1.133:5555 logcat *:S python:D