for i in 1000 10000 100000 1000000 10000000;
do
	for j in 10 100 1000 10000;
	do

		if [[("$i" -le 10000) && ("$j" -ge "$i")]];
			then break
		fi
		python test-hash.py $i $j "f1" "collision"_"f1"_${i}"_"${j}
		python test-hash.py $i $j "f2" "collision"_"f2"_${i}"_"${j}
		python test-hash.py $i $j "f3" "collision"_"f3"_${i}"_"${j}
		python test-hash.py $i $j "f4" "collision"_"f4"_${i}"_"${j}
	done
done