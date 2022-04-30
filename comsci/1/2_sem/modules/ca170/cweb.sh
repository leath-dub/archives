#!/bin/sh

OLDSTRING=$1
NEWSTRING=$2
shift
shift
for file in $*
do
    cat $file | sed "s/$OLDSTRING/$NEWSTRING/g" > out.sh
    cp out.sh $file
done
