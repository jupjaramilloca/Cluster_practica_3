import os
import subprocess


VIRTUAL_ENV_NAME = ".venv"

def ambiente_virtual_existe():
    # Comprobar si el ambiente virtual ya existe
    return os.path.exists(VIRTUAL_ENV_NAME)

def crear_ambiente_virtual():
    if ambiente_virtual_existe():
        print("El ambiente virtual ya existe.")
        return
    print("Creando ambiente virtual...")
    # Crear ambiente virtual
    subprocess.run(["python", "-m", "venv", VIRTUAL_ENV_NAME])
    print("Ambiente virtual creado.")

def activar_ambiente_virtual():
    print("Activando ambiente virtual...")
    # Activar el ambiente virtual
    if os.name == 'nt':  # Para Windows
        subprocess.run([f"{VIRTUAL_ENV_NAME}\\Scripts\\activate.bat"], shell=True)
    else:  # Para sistemas Unix (Linux, macOS)
        subprocess.run(["source", f"{VIRTUAL_ENV_NAME}/bin/activate"], shell=True)
    print("Ambiente virtual activado.")

def instalar_dependencias():
    print("Instalando dependencias...")
    # Activar el ambiente virtual
    activar_ambiente_virtual()
    # Instalar dependencias del archivo requirements.txt
    subprocess.run([f"{VIRTUAL_ENV_NAME}\\Scripts\\pip", "install", "-r", "requirements.txt"])
    print("Dependencias instaladas.")

def carpetas_existen():
    # Comprobar si las carpetas ya existen
    return os.path.exists("dataset") and os.path.exists("src")

def crear_carpetas():
    if carpetas_existen():
        print("Las carpetas ya existen.")
        return
    print("Creando carpetas...")
    # Crear carpeta dataset
    os.makedirs("dataset", exist_ok=True)
    # Crear carpeta src
    os.makedirs("src", exist_ok=True)
    print("Carpetas creadas.")

def crear_gitignore():
    contenido_gitignore = [
        "*.pyc",
        "__pycache__/"
    ]
    # Si ya existe el archivo .gitignore, abrirlo y agregar la exclusión del directorio .venv
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r+") as archivo:
            lineas = archivo.readlines()
            if ".venv/" not in lineas:
                archivo.write(".venv/\n")
        print("Archivo .gitignore actualizado.")
    else:
        # Si no existe, crear un nuevo archivo .gitignore con el contenido deseado
        contenido_gitignore.append(".venv/")
        with open(".gitignore", "w") as archivo:
            archivo.write("\n".join(contenido_gitignore))
        print("Archivo .gitignore creado.")


if __name__ == "__main__":
    total_pasos = 5  # Número total de pasos
    paso_actual = 0  # Inicializar el paso actual

    crear_ambiente_virtual()
    paso_actual += 1
    print(f"Progreso: {paso_actual}/{total_pasos}")

    activar_ambiente_virtual()
    paso_actual += 1
    print(f"Progreso: {paso_actual}/{total_pasos}")

    instalar_dependencias()
    paso_actual += 1
    print(f"Progreso: {paso_actual}/{total_pasos}")

    crear_carpetas()
    paso_actual += 1
    print(f"Progreso: {paso_actual}/{total_pasos}")

    crear_gitignore()
    paso_actual += 1
    print(f"Progreso: {paso_actual}/{total_pasos}")



    print("Configuración completada.")
