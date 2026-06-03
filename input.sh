#!/bin/bash
read -p "Enter your age: " age
if [[ $age -ge 18 ]]; then
	echo "$age is eligble to vote "
elif [[ $age -le 0 ]]; then
	echo "age is $age, can't be negative or zero"
else
	echo "$age is not eligble to vote"
fi
