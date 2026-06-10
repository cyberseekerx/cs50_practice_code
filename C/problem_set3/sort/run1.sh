rm time_s1.log
for n in {5000,10000,50000}; do
	echo "random$n.txt output" >>time_s1.log
	{ time ./sort1 random$n.txt 2>1; } 2>>time_s1.log
	printf "\n\n\n" >>time_s1.log
done
for i in {5000,10000,50000}; do
	echo "reversed$i.txt output" >>time_s1.log
	{ time ./sort1 reversed$i.txt 2>1; } 2>>time_s1.log
	printf "\n\n\n" >>time_s1.log
done

for i in {5000,10000,50000}; do
	echo "sorted$i.txt output" >>time_s1.log
	{ time ./sort1 sorted$i.txt 2>1; } 2>>time_s1.log
	printf "\n\n\n" >>time_s1.log
done
