#import sys
#print(sys.version)

import subprocess
import sys
import os

# Asegúrate de que pip esté actualizado
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

# Instala Jupyter Notebook
subprocess.check_call([sys.executable, "-m", "pip", "install", "notebook"])

print("¡Instalación completada!")

# Lanza Jupyter Notebook automáticamente
notebook_dir = os.getcwd()  # Carpeta actual (puedes cambiarla si lo necesitas)
subprocess.run([sys.executable, "-m", "notebook", notebook_dir])
