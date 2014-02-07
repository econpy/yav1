from pandas import read_csv
import os
import sys

from libv1.logparser import CleanLogData

"""
ABOUT:
    This script parses a single YaV1 log located in the `rawlogs` folder. Just
    pass the date of the log file you want to clean and it will output a new
    CSV file in the `cleanlogs` folder.

USE:
    python parse_log.py 2014-02-01

"""

basedir = os.path.realpath('.')

# Take the date of the log file from the command line
if len(sys.argv) == 2:
    logdate = sys.argv[1]
    logfilepath = '%s/rawlogs/%s_alert.log' % (basedir, logdate)
    if not os.path.exists(logfilepath):
        sys.exit('ERROR: %s does not exist.' % logfilepath)

    # Read a raw log file into a DataFrame.
    in_df = read_csv(logfilepath)

    # Clean the log and export it to a CSV file.
    out_df = CleanLogData(in_df)
    outfilepath = '%s/cleanlogs/%s_alert.csv' % (basedir, logdate)
    out_df.to_csv(outfilepath, index=False)
    print 'Success! Cleaned log file saved to: %s' % outfilepath
else:
    sys.exit('''
    **** ERROR ****
    ---------------
    Please run the script again by passing the date of a log file in your
    rawlogs folder. For example:

         python parse_log.py 2013-02-01

    which will clean the log file located at

        ./rawlogs/2014-02-01_alert.log

    and create a new file at

        ./cleanlogs/2014-02-01_alert.csv
    ''')
