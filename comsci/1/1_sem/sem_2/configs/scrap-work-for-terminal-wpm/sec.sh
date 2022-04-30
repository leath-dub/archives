#!/bin/bash

cd 
declare -i i=0
while [i<20]; do
    r=$[$RANDOM % 200 + 1]
    t=$(cat english_words/english | sed -n ''$r'p')
    echo $t
    $i++

x=$(date +%M)
y=$(date +%S)
declare -i z=$[$x*60+$y]
echo $z
