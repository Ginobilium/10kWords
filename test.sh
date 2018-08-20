#! /bin/sh
git pull
python /home/neo/10kWords/temp.py
git add README.md
m=$(date +%Y-%m-%d)` updated`
git commit -m $m
git push
