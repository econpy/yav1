from glob import glob
from multiprocessing import Pool
from pandas import read_csv
import os

from libv1.logparser import CleanLogData

"""
ABOUT:
    This script is for parsing all YaV1 logs in the `rawlogs` folder. It uses
    the multiprocessing module to do this in parallel, which is admittedly a
    bit of overkill since the log files generally aren't very big, but why not?

USE:
    python parse_all_logs.py

"""


def ParseLogFile(raw_log):
    in_df = read_csv(raw_log)
    out_df = CleanLogData(in_df, dropnans=True)
    if out_df is None:
        print 'ERROR: Failed to parse: %s' % raw_log.split('/')[-1]
        pass
    else:
        out_file = raw_log.replace('raw', 'clean').replace('.log', '.csv')
        out_df.to_csv(out_file, index=False)

if __name__ == '__main__':
    raw_logs = glob('%s/rawlogs/*_alert.log' % os.path.realpath('.'))
    pool = Pool()
    pool.map(ParseLogFile, raw_logs)
    pool.close()
    pool.join()
