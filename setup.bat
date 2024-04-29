@echo off

:: Cambiar al directorio del repositorio clonado
cd /d "C:\Users\Usuario\Repositorio"

:: Ejecutar el script de configuración (setup.py)
echo Ejecutando script de configuración...
python setup.py

:: Desconectar el repositorio remoto
git remote rm origin
echo Repositorio remoto desconectado.

echo Configuración completada.
pause
