rm time_s3.log
for n in {5000,10000,50000}; do
	echo "random$n.txt output" >>time_s3.log
	{ time ./sort3 random$n.txt 2>1; } 2>>time_s3.log
	printf "\n\n\n" >>time_s3.log
done
for i in {5000,10000,50000}; do
	echo "reversed$i.txt output" >>time_s3.log
	{ time ./sort3 reversed$i.txt 2>1; } 2>>time_s3.log
	printf "\n\n\n" >>time_s3.log
done

for i in {5000,10000,50000}; do
	echo "sorted$i.txt output" >>time_s3.log
	{ time ./sort3 sorted$i.txt 2>1; } 2>>time_s3.log
	printf "\n\n\n" >>time_s3.log
done
