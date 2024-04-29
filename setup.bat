@echo off

:: Script de configuración

:: Cambiar al directorio del script
cd /d %~dp0

:: Ejecutar el script de configuración (setup.py)
echo Ejecutando script de configuración...
python setup.py

:: Desconectar el repositorio remoto
git remote rm origin
echo Repositorio remoto desconectado.

:: Eliminar la carpeta Setup
echo Eliminando la carpeta Setup...
rmdir /s /q "%cd%\Setup"
echo Carpeta Setup eliminada.

echo Configuración completada.
pause
