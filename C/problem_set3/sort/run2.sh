rm time_s2.log
for n in {5000,10000,50000}; do
	echo "random$n.txt output" >>time_s2.log
	{ time ./sort2 random$n.txt 2>1; } 2>>time_s2.log
	printf "\n\n\n" >>time_s2.log
done
for i in {5000,10000,50000}; do
	echo "reversed$i.txt output" >>time_s2.log
	{ time ./sort2 reversed$i.txt 2>1; } 2>>time_s2.log
	printf "\n\n\n" >>time_s2.log
done

for i in {5000,10000,50000}; do
	echo "sorted$i.txt output" >>time_s2.log
	{ time ./sort2 sorted$i.txt 2>1; } 2>>time_s2.log
	printf "\n\n\n" >>time_s2.log
done
exit
