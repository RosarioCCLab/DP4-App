# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import subprocess

subprocess.run('pip install dp4plus-app') 

try: 
  subprocess.run('sudo apt-get update')
  subprocess.run('sudo apt-get install python3-tk')

except: pass
