#! /bin/sh
git pull
python /home/neo/10kWords/temp.py
git add README.md
m=`date +%Y-%m-%d`
git commit -m $m
git push
