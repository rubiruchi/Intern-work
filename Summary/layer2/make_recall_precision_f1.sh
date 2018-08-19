for f in k*.log
do
    echo $f >> a.temp
    cat $f | grep -A1 "Confusion matrix= " >> a.temp
done
python make_rrf1.py a.temp
