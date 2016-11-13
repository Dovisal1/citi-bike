
rm -f loc.txt final.txt *zip *csv
touch loc.txt

for i in `seq 9`; do
	f="20160$i-citibike-tripdata"
	wget http://witestlab.poly.edu/bikes/$f.zip
	unzip $f.zip
	awk -F "\"*,\"*" '{print $5}' $f.csv >> loc.txt
	awk -F "\"*,\"*" '{print $9}' $f.csv >> loc.txt
done

cat loc.txt | sort | uniq -c | sort -nr | head -n1
rm loc.txt *zip *csv