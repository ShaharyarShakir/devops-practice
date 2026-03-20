#!/bin/bash

# read -p "Enter your name: " name
name=$(whoami)
day=$(date)
greeting() {
	echo "How you doing $name"
	sleep 1
	echo "you are looking today $name"
	sleep 1
	echo "You have the best beard I have ever seen $name!!"
	sleep 1
	echo "Today is $day"
	# Get private IP
	PRIVATE_IP=$(hostname -I | awk '{print $1}')

	# Get public IP
	PUBLIC_IP=$(curl -s ifconfig.me)

	# Output
	echo "Private IP: $PRIVATE_IP"
	echo "Public IP:  $PUBLIC_IP"
}
greeting
