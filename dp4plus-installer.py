# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import subprocess, os, shutil


try: 
  subprocess.run('sudo apt-get update')
  subprocess.run('sudo apt-get install python3-tk')

except: pass

subprocess.run('pip install dp4plus-app') 

def create_exe():
    '''Creates a direc acces executable file in the user desktop'''
    #desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    exe = shutil.which("dp4plus")
    
    shutil.copy(exe, desktop)
    return 
  
  create_exe()
