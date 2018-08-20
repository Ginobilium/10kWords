# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
from datetime import datetime, timedelta

now = datetime.now()
# convert object to the format we want
today = now.strftime('%m_%d')
today += ".md"
filelist = os.listdir("/home/neo/10kWords")
deltalist = [1,2,4,7,15,30]

with open("/home/neo/10kWords/README.md",'w') as f:
    f.write("# 10kWords\n")
    f.write("曲根万词班笔记\n\n")
    for d in deltalist:
        date =  now - timedelta(days = d)
        filename = date.strftime('%m_%d')+".md"
        if filename in filelist:
            text = date.strftime("[%b. %d]")
            f.write(text+"(\\"+filename+")"+"\n")