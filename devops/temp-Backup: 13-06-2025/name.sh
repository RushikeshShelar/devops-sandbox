#!/bin/bash

showname(){
	echo Hello $1;
	if [ ${1,,} = rushi ]; then
		return 0;
	else
		return 1;
	fi
}

showname $1
if [ $? = 1 ]; then
	echo "Unknown"
else 
	echo Hello $1
fi
