#!/bin/bash

# for loop

for ((num=$2; num<=$3; num++))
do
	mkdir "$1$num"
done
