#! /bin/sh
git pull
python /home/neo/10kWords/temp.py
git add README.md
git commit -m "update README"
git push
