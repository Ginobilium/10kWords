# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
from datetime import datetime

date_object = datetime.now()
# convert object to the format we want
today = date_object.strftime('%m_%d')
today += ".md"
file_list = os.listdir("/home/neo/10kWords")
