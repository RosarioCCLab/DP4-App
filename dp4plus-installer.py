# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import subprocess
import os 

def create_exe():
    '''Creates a direc acces executable file in the user desktop'''
    #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    dir_acc = os.path.join(desktop,'dp4plus.py')

    with open (dir_acc, 'w') as file:
        file.write('# -*- coding: utf-8 -*-\n\n')
        file.write('import os, shutil\n\n')
        file.write('exe = shutil.which("dp4plus")\n\n')
        file.write('os.system(exe)\n\n')



subprocess.run('pip install dp4plus-app') 

try: 
  subprocess.run('sudo apt-get update')
  subprocess.run('sudo apt-get install python3-tk')

except: pass

