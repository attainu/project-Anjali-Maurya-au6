# Parking Lot System

## Introduction:-

parking is an important part of the transportation system. As it is very difficult to manage and maintain the huge parking lot so there were this project comes in the scenario. This project can keep the record based on the Registration number(Number Plate no.) and the Color of the car.

## Dependencies:-

You just need Python. Visit the link https://www.python.org/downloads/ to install Python.

## Description:-

This repository gives an overview of how we can design a basic parking lot in Python. It allocate parking Slots to vehicle. We can keep track of vehicle based on that slot

Parkinglot.py script passes the following testcases:-  
It gives a choice to user for manual or file input.  
create_parking_lot 6  
park KA-01-HH-1234 White  
park KA-01-HH-9999 White  
park KA-01-BB-0001 Black  
park KA-01-HH-7777 Red  
park KA-01-HH-2701 Blue  
park KA-01-HH-3141 Black  
leave 4  
status  
park KA-01-P-333 White  
park DL-12-AA-9999 White  
registration_numbers_for_cars_with_colour White  
slot_numbers_for_cars_with_colour White  
slot_number_for_registration_number KA-01-HH-3141  
slot_number_for_registration_number MH-04-AY-1111

The above testcases defines the following term-

1. `create_parking_lot n` - Given n number of slots, create a parking lot
2. `park car_regno car_color` - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
3. `status` - Prints the slot number, registration number and color of the parked vehicles.
4. `leave x` - Removes vehicle from slot number x
5. There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.

To create your own ParkingLot -

1. Clone the repository

2. Run `python Parkinglot.py` The below image shows the terminal window where I have given input on my path to python script.Thus it is showing two choices either Manual Input or File Input.

![](https://github.com/attainu/project-Anjali-Maurya-au6/blob/dev/Screenshot/1.png)

3. This is how the menu driven program appears shown below when Manual Input is chosen. First of all, no. of total slots has to be created so from the testcase I have taken 6 slots as input. After that program is asking either to park or to perform the remaining task according to the choice no.

![](https://github.com/attainu/project-Anjali-Maurya-au6/blob/dev/Screenshot/2.png)

4. In this image shows the file input option, where path for the testcase.txt is given. Then automatically code fetches the input and gives the output.

![](https://github.com/attainu/project-Anjali-Maurya-au6/blob/dev/Screenshot/3.png)
