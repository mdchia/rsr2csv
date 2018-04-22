#!/usr/bin/env python

import sys
import re
import csv
from datetime import datetime
import os

# get filename
rsr_in=sys.argv[1]

# add stuff we want to these, but the actual reads are going to a csv
data_lines = []
metadata = []

with open(rsr_in, mode="rb") as rsr_file:
    for line in rsr_file.readlines():
        line=str(line.decode('latin-1'))
        if not line.startswith("\par"):
            next
        else:
            # Remove things like "\par \f1\fs16"
            newline = re.sub(r"\\[A-Za-z0-9]*","",line)
            # Remove the line in the middle and the trailing curly brace
            newline = re.sub(r"[_\}]*","",newline)
            newline = newline.strip()
            # ignore empty lines
            if newline == "":
                continue
            # Consider line as data if its the first line "Read, Abs, nm"
            # or if its a calibration entry starting with "Zero" for read
            if re.search(r"^(Read|Zero|[0-9])", newline):
                data_lines.append(newline)
            # Takes the first few lines as run metadata
            else:
                metadata.append(newline)

collection_time = datetime.strptime(metadata[0],
                                    "Collection Time: %d/%m/%Y %I:%M:%S %p")
# Probably doesn't work on Windows
dir_path = os.path.dirname(rsr_in) + "/"

# Might work on Windows, but untested
#dir_path = os.path.dirname(os.path.abspath(rsr_in)) + "\"

# write csv to the same directory as input file
csv_name = dir_path + collection_time.strftime("%Y%m%d_%H%M") + "_specdata.csv"

with open(csv_name, mode="w", newline='') as csv_file:
    csv_writeout = csv.writer(csv_file)
    for record in data_lines:
        csv_writeout.writerow(record.split())

# debug info
print("Conversion success! "+str(len(data_lines)-1)+" records written to "+collection_time.strftime("%Y%m%d_%H%M") + "_specdata.csv")
