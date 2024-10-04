# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import platform
import subprocess
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

operating_system = platform.system()

#-----------------------------------------------------------------

# Detectar el sistema operativo y realizar la instalación del paquete dp4plus-app
if 'Windows' in operating_system:
    try:
        subprocess.run('pip install --upgrade dp4plus-app', shell=True)
    except:
        subprocess.run('pip3 install --upgrade dp4plus-app', shell=True)

elif 'Darwin' in operating_system:
    try:
        subprocess.run(['pip', 'install', '--upgrade', 'dp4plus-app'])
    except:
        subprocess.run(['pip3', 'install', '--upgrade', 'dp4plus-app'])

elif 'Linux' in operating_system:
    os.system('sudo apt install python3-pip')
    os.system('pip install --upgrade dp4plus-app')

#-----------------------------------------------------------------

def create_exe():
    '''Creates a direct access executable file on the user's desktop'''
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    exe = shutil.which("dp4plus")
    
    if exe:
        shutil.copy(exe, desktop)
        return True
    return False

# Intentar crear el acceso directo
print('\n\n\n\n\nCreating direct access "dp4plus.exe" . . .\n\n\n\n\n\n')
success = create_exe()

#-----------------------------------------------------------------

# Crear una ventana con PyQt5
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DP4+ App')

        # Crear los widgets de la interfaz
        layout = QVBoxLayout()

        label1 = QLabel(u'Process completed \u2713')
        label1.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(label1)

        label2 = QLabel('DP4+ App has been installed successfully')
        layout.addWidget(label2)

        if success:
            label3 = QLabel('Run it with dp4plus.exe on your desktop')
        else:
            label3 = QLabel('Executable not found. Please check installation.')
        layout.addWidget(label3)

        label4 = QLabel('Press Exit to finish')
        layout.addWidget(label4)

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

#-----------------------------------------------------------------

# Inicializar la aplicación PyQt5
app = QApplication([])

# Crear la ventana principal
window = AppWindow()
window.show()

# Ejecutar el loop principal de la aplicación
app.exec_()
