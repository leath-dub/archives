#!/bin/sh

wget -q -O - https://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=$1 \
    | tr -d '\015' \
    | tr "\n" " " \
    | sed -e 's/.*\(Last:<\/span>\)/\1/g' -e 's/\(<\/div>\).*/\1/g' -e 's/.*<div>\(.*\)<\/div>.*/\1/g' \
    | sed -e 's/,//g'
