# DP4+ App
## A tool for DP4+, MM-DP4+ and Custom DP4+ probability calculation
DP4+ App is an integrated software capable of performing already parameterized DP4+ and MM-DP4+ calculations. Furthermore, Custom-DP4+ calculations can be performed, where any level of theory required can be parameterized. Its friendly graphical interface allows easy manipulation of multiple Gaussian calculations and automatic information processing to perform the probabilistic calculus.

>> <picture>
 <img alt="Show" src="https://user-images.githubusercontent.com/118339488/226717260-a4139596-0d8d-4b5f-b06c-ca1cf6b531be.png" width="192" height="237"/>
</picture>

## Characteristics
### Functionalities
The DP4+ App calculation methods determine probability of correlation between experimental information and two or more sets of calculated magnetic tensors from a group of candidate molecules in study. Probabilities are determined using raw as well as scaled data, following the mathematical formalism of Bayesian methods. 
To carry out a calculation, you must have the one-dimensional spectrum of C and/or H of your molecule under study and the Gaussian "nmr" calculations of its plausible isomers (candidates).
The theory level used in the Gaussian calculations must match the level used in the DP4+ App. Therefore, the software offers 24 DP4+ levels, 36 MM-DP4+ levels and in case this is not enough, the possibility to parameterize your own level with Custom DP4+. For more details on available functions and levels, access the [DP4+ App user guide](https://github.com/RosarioCCLab/DP4plus-App/blob/main/UserGuide.pdf)

### Installation Requirements 
**DP4+ App** needs python 3.8 or later to work. Find it in <https://www.python.org/downloads/>

The programme can be installed in two ways:
* using the operating system console with the command: 
> `pip install dp4plus-app` 

* running the following script [DP4+App_Installer](https://raw.githubusercontent.com/RosarioCCLab/DP4plus-App/main/dp4plus-installer.py) (Save the code with right click on the website screen -> 'save as').

### Execute DP4+ App

If the programme is installed via command line, it can be excuted in the same console using: 
> `dp4plus`

In case [DP4+App_Installer](https://raw.githubusercontent.com/RosarioCCLab/DP4plus-App/main/dp4plus-installer.py) is used, the programme can be run also by command line or by doble click in the shortcut (`dp4plus.py`) that has been created on your desktop.

If the executable is missing or not created yet, the `dp4plus.py` shortcut can generated using command line: 
> `dp4plus-exe`


## User Guide and Examples
[DP4+ App user guide](https://github.com/RosarioCCLab/DP4plus-App/blob/main/UserGuide.pdf) is available in this repository and also inside the programme finding the `User Guide` button. Along with it, you can find a corroborated case study to use as an example and learn how to use the tool. 

>> <picture>
<img alt="Show" src=https://user-images.githubusercontent.com/118339488/227007210-463ec618-7067-4e88-ba7e-6b00fafbf388.png width="477.5" height="220"/>
</picture>

### Bugs and malfuntions
In case you find a faulty operation of DP4+ App, please report your situation in detail to the following emails:
* brunoafranco@uca.edu.ar
* zanardi@inv.rosario-conicet.gov.ar
* sarotti@iquir-conicet.gov.ar

###### You can also comment in this repository, but know we check the emails more frequently

