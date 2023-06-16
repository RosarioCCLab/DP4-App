# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:45:03 2023

@author: Franco, Bruno Agustín 

This is a helper script to install a PyPI module, designed for users who are not familiar with operating system command line usage.
"""

import platform
operating_system = platform.system()

#-----------------------------------------------------------------
import platform
operating_system = platform.system()

#-----------------------------------------------------------------
import subprocess, os, shutil

if 'Windows' in operating_system: 
   try:
      subprocess.run('pip install --upgrade dp4plus-app')
   except:
      subprocess.run('pip3 install --upgrade dp4plus-app')

if 'Darwin' in operating_system:
   try:
      subprocess.run(['pip','install','--upgrade','dp4plus-app'])
   except:
      subprocess.run(['pip3','install','--upgrade','dp4plus-app'])
      
elif 'Linux' in operating_system: 
  os.system('sudo apt install python3-pip')
  os.system('sudo apt install python3-tk')
  os.system('pip install --upgrade dp4plus-app') 

#-----------------------------------------------------------------

def create_exe():
    '''Creates a direc acces executable file in the user desktop'''
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    exe = shutil.which("dp4plus")
    
    shutil.copy(exe, desktop)
    return 

print ('\n\n\n\n\nCreating direct access "dp4plus.exe" . . .\n\n\n\n\n\n')
create_exe()

#-----------------------------------------------------------------
import tkinter as tk
byby = tk.Tk()
byby.wm_title("DP4+ App")

tk.Label(byby,text = u' Procces completed \u2713', 
         font = ("Arial Black", "12")).grid(row=0,padx=10, pady=(10,0))
tk.Label(byby,text ='DP4+ App has been installed successfully', 
         font = ("Arial Bold", "10")).grid(row=1,padx=10, pady=5)
tk.Label(byby,text ='Run it whith dp4plus.exe on your desktop', 
         font = ("Arial Bold", "10")).grid(row=2,padx=10, pady=5)
tk.Label(byby,text ='Press Exit to finish', 
         font = ("Arial Bold", "10")).grid(row=3,padx=10, pady=5)
tk.Button(byby, text='Exit', 
          command= byby.destroy).grid(row=4, pady=(5,10))

byby.mainloop()
