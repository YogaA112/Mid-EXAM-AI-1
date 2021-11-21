#!/bin/bash


local_random=$(($RANDOM%7))
echo $local_random


for index in `seq 0 3`; do
    random_result[$index]=1
done

for index in `seq 4 5`; do
	random_result[$index]=2
done

random_result[6]=3
random_result[7]=4


echo ${random_result[$local_random]}
