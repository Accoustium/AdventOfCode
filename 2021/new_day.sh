#/usr/bin/env bash
day=$1
if [ -z "$day" ]
then
   echo "Day not provided."
   exit
fi

echo "Creating Day $day Folder"
mkdir Day_$day
cd Day_$day

echo "Creating Part1/2 Folders"
mkdir Part_1
mkdir Part_2

echo "Creating Day $day script and text files"
touch Part_1/day${day}part1.py
touch Part_1/day${day}part1.txt
touch Part_2/day${day}part2.py
touch Part_2/day${day}part2.txt

