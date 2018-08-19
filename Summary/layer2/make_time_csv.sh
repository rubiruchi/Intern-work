for f in k*.log
do
    echo $f >> a.temp
    cat $f |  grep "Training Total Time:" | cut -c22- | paste -sd+ | bc >> a.temp
    cat $f |  grep "Predict Total Time:" | cut -c21- | paste -sd+ | bc >> a.temp
done
python make_time.py a.temp
rm a.temp
