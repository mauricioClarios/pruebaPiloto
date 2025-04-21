from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
usuario = os.getenv("user")
contraseña = os.getenv("pass")

print(f"Usuario: {usuario}")

