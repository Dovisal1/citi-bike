#!/bin/bash

for i in `seq 9`; do
	f="20160$i-citibike-tripdata"
	if ! test -f $f.csv; then
		if ! test -f $f.zip; then
			wget http://witestlab.poly.edu/bikes/$f.zip
		fi
		unzip $f.zip
	fi
done