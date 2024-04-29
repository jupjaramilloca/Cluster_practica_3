@echo off

:: Script de configuración

:: Cambiar al directorio del script
cd /d %~dp0

:: Ejecutar el script de configuración (setup.py)
echo Ejecutando script de configuración...
python setup.py

echo Configuración completada.
pause
