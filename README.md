# Writing Project 4 - Machine Learning Project README

The Project is a Readme for code written for a Machine Learning Project.

## Table of Contents
* [Overview](#overview)
* [System Setup](#system-setup)
    * [Linux Command Line Setup](#linux-command-line-setup)
    * [Windows Command Line Setup](#windows-command-line-setup)
    * [IDE Setup](#command-line-setup)
* [Running](#running)
    * [Command Line Running](#Command-Line-Running)
    * [IDE Running](#IDE-Running)
* [Unit Testing/Results](#unit-testing-and-results)
    * [Unit Testing](#Unit-Testing)
    * [Results](#Results)
* [TODOs](#todos)
* [Authors](#authors)

## Overview

The purpose of this code is to find the likelihood that a vehicle is at a position given measurements from reference points. The vehicle is generated to be somewhere random in the unit circle, with some user specified number of reference points on tht unit circle. The robot then takes a measurement to each measurement, which is done using Euclidean distance. These measurements also consist of some added Gaussian noise, which leads to some uncertainty around the robots position.

Then, using Maximum a posteriori (MAP) estimation, The code assigns a value to each point in a grid surrounding the unit circle in which the vehicle is located. The lowest value on this grid is the most likely spot of the vehicle given the noisy measurements. The code displays this in terms of a contour plot, which has descending values as the true vehicle location is approached, while overlaying the true vehicle location and the reference points (see results for images).

## System Setup

### Linux Command Line Setup
Run these commands in the terminal to install python3 and pip3 
```
sudo apt update
sudo apt install python3.8
sudo apt-get -y install python3-pip
```
Run these commands to install the required libraries via the terminal
```
pip3 install matplotlib
pip3 install numpy
```

### Windows Command Line Setup

Download and install the most recent version of python from this website: https://www.python.org/downloads/ and run the following command in the command prompt/powershell to install pip
```
py -m pip install -U pip
```

Run the following commands in the comman prompt/powershell to install the required libraries
```
pip install matplotlib
pip install numpy
```

### IDE Setup

This IDE setup is for the pycharm IDE and may vary across different IDEs.

The first step is to click `file`:
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/idestep1.JPG" width="588" height="60"/>
</p>

In the dropdown select `Settings` and in the settings click the `Project:WriteProj` and `Project Interpreter`. From there click the `+` button:
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/idestep2-3.JPG" width="779" height="556"/>
</p>

In the window that pops up, add the `numpy` and `matplotlib` packages and click `Install Package`:
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/idestep4.JPG" width="719" height="601"/>
</p>

Then Check to make sure the packages installed and click `Apply` and `Ok`:
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/idestep5.JPG" width="775" height="556"/>
</p>

## Running
    
### Command Line Running
Run the followings commands from the base folder with the number references arguments you want in the command line of your system in order to cd into the folder with the script and to run the code. 
```
cd scripts
python3 code.py -r $NUM_OF_REFS
```
If you are running on windows run these commands from the base folder of the repo in powershell/command prompt with these commands. 
```
cd scripts
py code.py -r $NUM_OF_REFS
```
Replace $NUM_OF_REFS with the number of reference points as an integer that you would like to use. For example: 
```
python3 code.py -r 3
```
or for windows
```
py code.py -r 3
```
### IDE Running

These instructions are again for the PyCharm IDE.

This first step is to set up the run configuration. First either click on the `Run` menu and choose `Edit Configurations` or Click on `Add Configuration` in the upper right:

<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/ideRunStep1.JPG" width="960" height="41"/>
</p>

Then Click the `+` button and choose `Python`. Then choose a name for the Configuration. Then specify the file path to the script, which can be done by clicking the folder icon on the `Script path` entry and navigating to the location of the `code.py` file. Then input the Parameters by entering `-r $NUM_OF_REFS` where the number is the number of reference points, like 3 in the image shown below. Then click `OK` to save the configurations:

<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/ideRunStep2.JPG" width="834" height="528"/>
</p>

Lastly to run the code either select the `Run` menu and choose `Run` or Click on the Green triangle icon in the upper right:
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/ideRunStep3.JPG" width="960" height="44"/>
</p>

These Run configurations can be edited by following these steps again.

## Unit Testing/Results
### Unit Testing
* See TODOs section
### Results
<p align="center">
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/Result3.PNG" width="250" height="250" />
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/Result1.PNG" width="250" height="250" />
<img src="https://github.com/Gabe-Jentis/WritingProj4/blob/main/Images/Result2.PNG" width="250" height="250" />
</p>

These images show the code becoming more confident on the true location of the vehicle. As the number on the inner ring decreases, and the plus sign representing the true vehicle location gets closer to the center of the innermost contour ring, the program is more confident on the true location of the vehicle based on the measurements to the reference points.
   
## TODOs
* __Add comments__ : Make the code easier to understand
* __Improve Organization and Structure__ : Make the code easier to parse through and follow code format guidelines.
* __Plotting Function__ : Create function for plotting to reduce redundancy and length of code
* __Clean up repo__ : Squash Commits and clean up history
* __Implement Unit Testing__ : Needs implementation to ensure new updates to code do not break code

## Authors
* Gabe Jentis - Northeastern University Department of Electrical and Computer Engineering
* Michael Shen - Northeastern University Department of Electrical and Computer Engineering
* Arbid Yusuf - Northeastern University Department of Electrical and Computer Engineering
