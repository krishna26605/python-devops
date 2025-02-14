#!/bin/bash

echo "enter your name "

read name

echo " enter your age:"

read age


echo "your name is $name and age is $age"


sudo useradd -m $name


echo "user added successfully"
