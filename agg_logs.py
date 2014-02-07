from datetime import datetime
from glob import glob
from pandas import read_csv, concat
import os

"""
ABOUT:
    This script is for reading in all your YaV1 log files (that have already
    been cleaned using the other scripts in this repository) and aggregating
    them into a single CSV file.

USE:
    python agg_logs.py

"""

basedir = os.path.realpath('.')

# Read all CSV files in ./cleanlogs/ and concatenate them into a DataFrame
dflist = [read_csv(log) for log in glob('%s/cleanlogs/*.csv' % basedir)]
df = concat(dflist, ignore_index=True)

# Save the DataFrame as a CSV file
today = datetime.now().strftime('%Y-%m-%d_%Hhr')
df.to_csv('%s/all_logs_%s.csv' % (basedir, today), index=False)
