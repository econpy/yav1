### About ###

This repo currently contains Python scripts for cleaning the raw log files from the [YaV1](https://play.google.com/store/apps/details?id=com.franckyl.yav1) app for Android.

[YaV1]((https://play.google.com/store/apps/details?id=com.franckyl.yav1)), which stands for *Yet Another V1* application, enhances the capabilities of your Valentine One Radar Detector when used in conjunction with the V1Connection Bluetooth adapter, and allows you to tailor its performance to fit your driving style.


### Dependencies ###

* [pandas](https://github.com/pydata/pandas)


### Usage ###

Copy the files in the YaV1 logs folder on your phone to the `rawlogs` folder in this repository.


### Syncing Data ###

As of right now, there isn't an elegant way of syncing the data being logged by YaV1 to a remote location. Currently, I'm considering one of the following:

1. Use an app like [DropSync](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync) to sync the YaV1 logs folder with a Dropbox folder.
2. Use a script that runs periodically on the phone to rsync/ssh the changes in the YaV1 log files.
3. Convince the developer of YaV1 to integrate real-time logging to a webserver, similar to what [Torque](https://play.google.com/store/apps/details?id=org.prowl.torque) does.

My ideal solution is #3 as it does not depend on any other apps (as #1 does) or that the user has a rooted phone (as #2 does).


### Coming Soon ###

* Create Google Maps using the static YaV1 log data.
