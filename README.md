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
* [TODOs](#todos)
* [Authors](#authors)

## Overview

The purpose of this code is to find the likelihood that a vehicle is at a position given measurements from reference points. The vehicle is generated to be somewhere random in the unit circle, with some user specified number of reference points on tht unit circle. The robot then takes a measurement to each measurement, which is done using Euclidean distance. These measurements also consist of some added Gaussian noise, which leads to some uncertainty around the robots position.

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

Download the most recent version of python from this website: https://www.python.org/downloads/ and run the following command in the command prompt/powershell to install pip
```
py -m pip install -U pip
```

Run the following commands in the comman prompt/powershell to install the required libraries
```
pip install matplotlib
pip install numpy
```

### IDE Setup
* Placeholder for information

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
### IDE Running

## Unit Testing/Results
* Placeholder for information

## TODOs
* Placeholder for information

## Authors
* Gabe Jentis - Department of Electrical and Computer Engineering
  * Placeholder for more specific information
* Michael Shen - Department of Electrical and Computer Engineering
  * Computer Engineering
* Arbid Yusuf - Department of Electrical and Computer Engineering
  * Placeholder for more specific information
