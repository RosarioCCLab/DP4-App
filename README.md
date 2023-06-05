# DP4+ App
## A tool for DP4+, MM-DP4+ and Custom DP4+ probability calculation
**DP4+App** is a comprehensive software tool designed to facilitate DP4+ and MM-DP4+ calculations with ease. With its user-friendly graphical interface, users can seamlessly handle multiple Gaussian calculations and leverage automated data processing for accurate probabilistic analysis. The software offers the flexibility to perform Custom-DP4+ calculations, enabling parameterization of theory levels as per individual requirements.

Experience the convenience and efficiency of DP4+ App as it streamlines the entire workflow of parameterized calculations. From data input to result generation, this powerful tool simplifies the process, ensuring accurate and reliable probabilistic analyses.

>> <picture>
 <img alt="Show" src="https://user-images.githubusercontent.com/118339488/226717260-a4139596-0d8d-4b5f-b06c-ca1cf6b531be.png" width="192" height="237"/>
</picture>

## Characteristics
### Functionalities

The **DP4+ App** utilizes advanced calculation methods to determine the probability of correlation between experimental information and two or more sets of calculated magnetic tensors from a group of candidate molecules under study. These probabilities are determined using both raw and scaled data, following the mathematical formalism of Bayesian methods.

To perform a calculation, you need to provide the one-dimensional spectrum of the carbon (C) and/or hydrogen (H) atoms of the molecule you are studying, along with the Gaussian "nmr" calculations of its plausible isomers (candidates).

It is important to note that the theory level used in the Gaussian calculations must match the level used in the DP4+ App. To accommodate various requirements, the software offers a wide range of options, including 24 DP4+ levels, 36 MM-DP4+ levels, and, if needed, the ability to parameterize your own custom level using Custom DP4+. For detailed information about the available functions and levels, please refer to the [DP4+ App user guide](https://github.com/RosarioCCLab/DP4plus-App/blob/main/UserGuide.pdf)

### Installation Requirements 
To run the DP4+ App, you will need Python 3.8 or a later version. If you don't have Python installed on your system, you can download it from <https://www.python.org/downloads/>.

Please make sure to add Python to your system's PATH environment variable to ensure correct usage of the DP4+ App. The following steps explain how to enable Python in your system's PATH:

1. Download and install Python from the provided link.

2. During the installation process, you will come across an option called "Add Python to PATH" or something similar. Make sure to check this option before proceeding with the installation. 

>> <picture>
<img alt="Show" src=https://user-images.githubusercontent.com/118339488/227255604-00cdfa72-6613-4f15-b2d6-08d2880a0899.png width="250" height="155"/>
</picture>

3. By enabling this option, Python will be added to your system's PATH, allowing you to run Python commands and scripts from any location in your command prompt or terminal.

By following these instructions and ensuring Python is correctly added to your system's PATH, you will be able to use the DP4+ App without any issues.

### Install DP4+App
To get started with the **DP4+ App**, you can choose from two installation methods:
* **Running the Installer Script:** Install the DP4+ App by running the provided installer script available at [DP4+App_Installer](https://github.com/RosarioCCLab/DP4plus-App/blob/main/dp4plus-installer.py). Simply save the code by opening it in raw format and right-clicking on the website screen to choose "Save as". Then, run the saved script on your system.

* **Using the OS Console (Command Line):** Alternatively, you can install the *DP4+App* by executing the following command in your operating system's console (command line):

> `pip install dp4plus-app` 

###### Linux (Ubuntu) users be aware that Python module *tkinter* is not installed with `pip` in your OS. In case your want to install **DP4+ App** by command line, make sure to also install tk with  > `sudo apt-get install python3-tk` . If you prefer the installer script, this issue is already addressed within it.

Choose the installation method that suits you best, and you'll be ready to use the DP4+ App for your probabilistic analysis needs.

### Running DP4+App

Once you have successfully installed the DP4+ App, you can execute it using the following methods:

* If you have installed the program via the command line, you can run it directly in the same console by using the command:

> `dp4plus`
 
* In case you have used the [DP4+App_Installer](https://github.com/RosarioCCLab/DP4plus-App/blob/main/dp4plus-installer.py) is used, the program can be executed either through the command line or by double-clicking on the shortcut named `dp4plus.exe` that has been created on your desktop. 


If the executable is missing or not created yet, the `dp4plus.exe` shortcut can be generated using command line: 
> `dp4plus-exe`


### User Guide and Examples
To help you get started with the DP4+ App and learn how to use its features effectively, we provide a comprehensive [DP4+ App user guide](https://github.com/RosarioCCLab/DP4plus-App/blob/main/UserGuide.pdf). It is available in the repository and can also be accessed directly within the program by clicking on the `User Guide` button.

>> <picture>
<img alt="Show" src=https://user-images.githubusercontent.com/118339488/227007210-463ec618-7067-4e88-ba7e-6b00fafbf388.png width="477.5" height="220"/>
</picture>

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
* ¿ One ?
* ¿ Two ?
* ¿ Three ?
