head -n 1 ./layer1/rrf1-a.temp >> rrf1-t2.csv
tail -n +2 ./layer1/rrf1-a.temp >> rrf1-t2.csv
tail -n +2 ./layer2/rrf1-a.temp >> rrf1-t2.csv
tail -n +2 ./layer3/rrf1-a.temp >> rrf1-t2.csv
tail -n +2 ./layer4/rrf1-a.temp >> rrf1-t2.csv
mv rrf1-t2.csv ../
head -n 1 ./layer1/n-summary1.log >> acc-t2.csv
tail -n +2 ./layer1/n-summary1.log >> acc-t2.csv
tail -n +2 ./layer2/n-summary2.log >> acc-t2.csv
tail -n +2 ./layer3/n-summary3.log >> acc-t2.csv
tail -n +2 ./layer4/n-summary4.log >> acc-t2.csv
mv  acc-t2.csv ../
head -n 1 ./layer1/t-a.temp >> time-t2.csv
tail -n +2 ./layer1/t-a.temp >> time-t2.csv
tail -n +2 ./layer2/t-a.temp >> time-t2.csv
tail -n +2 ./layer3/t-a.temp >> time-t2.csv
tail -n +2 ./layer4/t-a.temp >> time-t2.csv
mv time-t2.csv ../


