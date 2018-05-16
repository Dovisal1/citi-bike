#!/bin/bash

rm -f loc.txt res

for i in `seq 9`; do
	f="20160$i-citibike-tripdata"
	if ! test -f $f.csv; then
		if ! test -f $f.zip; then
			wget http://witestlab.poly.edu/bikes/$f.zip
		fi
		unzip $f.zip
	fi
	awk -F "\"*,\"*" '{print $5}' $f.csv >> loc.txt
	awk -F "\"*,\"*" '{print $9}' $f.csv >> loc.txt
done

cat loc.txt | sort | uniq -c | sort -nr | head -n1 > res
rm loc.txt *zip *csv