### About ###

This repo currently contains Python scripts for cleaning the raw log files from the [YaV1](https://play.google.com/store/apps/details?id=com.franckyl.yav1) app for Android.

The current value-added of these scripts is minimal. As of right now, the scripts are pretty much only useful for cleaning your raw log files. Very soon I will be adding a method to plot this data in a Google Map, so stay tuned.

### Dependencies ###

* [pandas](https://github.com/pydata/pandas)

### Usage ###

After cloning this repo, copy the files in the YaV1 logs folder on your phone to the `rawlogs` folder in this repository. The names of these files will have the structure `YYYY-MM-DD_alert.log`

Then you can clean a single log file (e.g. *rawlogs/2014-02-01_alert.log*) by running:
```
python parse_log.py 2014-02-01
```
or clean all the logs in your `rawlogs` folder by running:
```
python parse_all_logs.py
```
The cleaned logs will be created in the `cleanlogs` folder as CSV files. If you want to aggregate all your cleaned log files together into a single file, simply run:
```
python agg_logs.py
```

### What Gets Cleaned? ###

When I say these scripts *clean* your raw log files, I'm referring to the following transformations on the data:

* Convert Unix timestamps into human readable dates
* Convert frequencies from integers to appropriate floats (e.g. 35519 -> 35.519)
* Convert direction indicator from (0, 1, 2) to (Front, Rear, Side)
* Convert flag to more meaningful string
* Convert speed from meters per second to miles to hour

All of these conversions can be found in the [yav1/logparser.py](https://github.com/econpy/yav1/blob/master/libv1/logparser.py) file.


### Syncing Data ###

As of right now, there isn't an elegant way of syncing the data being logged by YaV1 to a remote location. Currently, I'm considering one of the following:

1. Use an app like [DropSync](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync) to sync the YaV1 logs folder with a Dropbox folder.
2. Use a script that runs periodically on the phone to rsync/ssh changes in the YaV1 log files.
3. Convince the developer of YaV1 to integrate real-time logging to a webserver, similar to what [Torque](https://play.google.com/store/apps/details?id=org.prowl.torque) does.

My ideal solution is #3 as it does not depend on any other apps (as #1 does) or that the user has a rooted phone (as #2 does).


### Coming Soon ###

* Create Google Maps using the static YaV1 log data.
