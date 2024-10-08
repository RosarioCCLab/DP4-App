# DP4+ App

This repository contains the tool presented in the publication titled **DP4+App: Finding the Best Balance between Computational Cost and Predictive Capacity in the Structure Elucidation Process by DP4+. Factors Analysis and Automation**, published in the Journal of Natural Products on September 18, 2023. 

For all work using **DP4+App** please cite the primary publication: 

* J. Nat. Prod. 2023, 86, 10, 2360–2367 . https://doi.org/10.1021/acs.jnatprod.3c00566

## A tool for DP4+, MM-DP4+ and Custom DP4+ probability calculation
The **DP4+App** is a powerful tool designed to assist researchers in the structure elucidation process by balancing computational cost and predictive capacity using DP4+ factors analysis and automation. It provides valuable insights and streamlines the decision-making process, making it a valuable asset for chemists and researchers working in natural product chemistry and related fields.

This is a comprehensive software was designed to facilitate DP4+ and MM-DP4+ calculations. With its user-friendly graphical interface, you can handle multiple Gaussian calculations and leverage automated data processing for accurate probabilistic analysis. The software also offers the flexibility to perform Custom-DP4+ calculations, enabling parameterization of theory levels as per individual requirements.

 <img alt="Show" src="https://github.com/Sarotti-Lab/DP4plus-App/assets/101182775/a459f018-78c8-4e43-b7de-0dd92eb40a48 " width="192" height="237"/>

## Characteristics
### Functionalities

The **DP4+ App** utilizes advanced calculation methods to determine the probability of correlation between experimental information and two or more sets of calculated magnetic tensors from a group of candidate molecules under study. These probabilities are determined using both raw and scaled data, following the mathematical formalism of Bayesian methods.

To perform a calculation, you need to provide carbon (C<sup>13</sup>) and/or hydrogen (H<sup>1</sup>) atoms one-dimensional NMR spectrum of the molecule you are studying, along with the Gaussian "nmr" calculations of its plausible isomers (candidates).

It is important to note that the theory level used in the Gaussian calculations must match the level used in the DP4+ App. To accommodate various requirements, the software offers a wide range of options, including 24 DP4+ levels, 36 MM-DP4+ levels, and, if needed, the ability to parameterize your own custom level using Custom DP4+. For detailed information about the available functions and levels, please refer to the [DP4+ App User guides and Example](https://github.com/Sarotti-Lab/DP4plus-App/tree/main/User%20Guides%20and%20Examples)

### Installation Requirements 
This package is confirmed to work with Python versions between **3.8 and 3.11.9**. The most recent tested version is 3.11.9, which works smoothly across Windows, Linux, and macOS. If you don't have Python installed on your system, you can download it from [Python 3.11.9](https://www.python.org/downloads/release/python-3119/)

######  Please note that Python 3.12 and 3.13 are not supported at the moment. If your system has Python 3.12 or later installed, we highly recommend setting up a virtual environment with Python 3.11.9 or an earlier version. You can consult your most trusted AI assistant for step-by-step guidance on creating virtual environments.

Please make sure to add Python to your system's PATH environment variable to ensure correct usage of the DP4+ App. The following steps explain how to enable Python in your system's PATH:

1. Download and install Python from the provided link.

2. During the installation process, you will come across an option called "Add Python to PATH" or something similar. Make sure to check this option before proceeding with the installation. 

<img alt="Show" src=https://user-images.githubusercontent.com/118339488/227255604-00cdfa72-6613-4f15-b2d6-08d2880a0899.png width="250" height="155"/>

3. By enabling this option, Python will be added to your system's PATH, allowing you to run Python commands and scripts from any location in your command prompt or terminal.

By following these instructions and ensuring Python is correctly added to your system's PATH, you will be able to use the DP4+ App without any issues.

### Install DP4+App
To get started with the **DP4+ App**, you can choose from two installation methods:
* **Running the Installer Script:** Install the DP4+ App by running the provided installer script available at [DP4+App_Installer](https://github.com/RosarioCCLab/DP4plus-App/blob/main/dp4plus-installer.py). Simply save the code by opening it in raw format and right-clicking on the website screen to choose "Save as". Then, run the saved script on your system.

* **Using the OS Console (Command Line):** Alternatively, you can install the *DP4+App* by executing the following command in your operating system's console (command line):

> `pip install --upgrade dp4plus-app` 

###### From version 0.2.8, there is no need to install the *tkinter* module, as the package now uses *PyQt5* for the UI. If you are installing a version prior to 0.2.8 and using Linux (Ubuntu) be aware that Python module *tkinter* is not installed with `pip` in your OS. In case your want to install **DP4+ App** by command line, make sure to also install tk with  > `sudo apt-get install python3-tk` . If you prefer the installer script, this issue is already addressed within it.

Choose the installation method that suits you best, and you'll be ready to use the DP4+ App for your probabilistic analysis needs.

### Running DP4+App

Once you have successfully installed the DP4+ App, you can execute it using the following methods:

* If you have installed the program via the command line, you can run it directly in the same console by using the command:

> `dp4plus`
 
* In case you have used the [DP4+App_Installer](https://github.com/RosarioCCLab/DP4plus-App/blob/main/dp4plus-installer.py) is used, the program can be executed either through the command line or by double-clicking on the shortcut named `dp4plus.exe` that has been created on your desktop. 


If the executable is missing or not created yet, the `dp4plus.exe` shortcut can be generated using command line: 
> `dp4plus-exe`



### User Guide and Examples
To help you get started with the DP4+ App and learn how to use its features effectively, we provide a comprehensive [DP4+ App User Guides](https://github.com/Sarotti-Lab/DP4plus-App/tree/main/User%20Guides%20and%20Examples). It is available in the repository and can also be accessed directly within the program by clicking on the `User Guide` button.

<img alt="Show" src=https://github.com/user-attachments/assets/c12bfbaf-661b-49f0-b712-cb390bd286ef width="555" height="559"/>

The user guide offers detailed instructions, explanations, and step-by-step tutorials to assist you in navigating the DP4+ App and making the most of its functionalities. It serves as a valuable resource to enhance your understanding of the tool and perform accurate probabilistic analyses.

Additionally, within the DP4+ App, you will find a corroborated study case that serves as an example. This study case demonstrates how to utilize the tool effectively, providing practical insights into its usage and showcasing its capabilities.

By referring to the user guide and exploring the example study case, you can quickly familiarize yourself with the DP4+ App and gain confidence in performing probabilistic analyses for your research or projects.

### Bugs and malfuntions
If you encounter any issues or experience faulty operations while using the *DP4+App*, we encourage you to report your situation in detail. By providing comprehensive information about the problem, you can assist us in improving the software. Please reach out to us using the following email addresses:
* brunoafranco@uca.edu.ar
* zanardi@inv.rosario-conicet.gov.ar
* sarotti@iquir-conicet.gov.ar

###### While you have the option to comment in this repository, we recommend using the email addresses mentioned above, as we monitor them more frequently.

### F.A.Q.
1. How can I uninstall DP4+App ? 

  In your terminal run the code:
  > `pip uninstall dp4plus_app` or `pip3 uninstall dp4plus_app`
  > 
2. Why I get this error: `pip is not recognized as an internal or external command, operable program or batch file.` ?
 
  This error occurs when the pip command or any other command is not recognized in the terminal. It typically happens when the required executable modules are not included in the system's PATH list.

  To resolve this issue, you have a couple of options:

  Reinstall Python, ensuring that you enable the option to add it to your computer's PATH during the installation process. 
  
  Manually add the appropriate directories to the PATH environment variable on your computer. This will involve modifying the system settings and adding the paths of the required executable modules. You can find step-by-step instructions on how to do this in the following resources: [Link 1](https://realpython.com/add-python-to-path/) y [Link 2](https://www.mygreatlearning.com/blog/add-python-to-path/)

