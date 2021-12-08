#/usr/bin/env bash
day=$1
if [ -z "$day" ]
then
   echo "Day not provided."
   exit
fi

echo "Creating Day ${day} Folder"
mkdir Day_$day
cd Day_$day

echo "Creating Day ${day} script and text files"
touch day${day}constants.py
touch day${day}part1.py
touch day${day}data.txt
touch day${day}part2.py

