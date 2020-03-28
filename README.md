# Bluetooth_Module
This repo is for connecting a blutooth module(high/low) with python and arduino.
## Description for the files:
### For high energy bluetooth module:
* [blue1.py]() is the python file that works to read from arduino or write on it (single chars, array of numbers)
* [Bluetooth_module_arduino.ino]() is the arduino file that sends to python through bluetooth. (the file that completes the job of the first file)
* [blue3_file.py]() is the python file that works to read from .csv file

### For low enery bluetooth module:
* [myble_rawfile.m]() is the raw matlab file for connecting matlab to ble (bluetooth low enery), this needs matlab 2019b version.
* [bluetooth.m]() is the matlab file with its gui.
* [myble_bleak.py]() is a python file as a trial file, trying to communicate with ble using the "bleak" library (it didn't work well)
