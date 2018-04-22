# rsr2csv
Converts Varian spectrophotometer .rsr reports to csv format

Tested with the Cary 50 UV-Vis spectrophotometer and Python 3.

Usage: `python rsr2csv.py <input .rsr file>`

Automatically returns csv in the same folder as the input file, as `YYYYMMDD_HHMM_specdata.csv` (HHMM is in 24 hour time).
