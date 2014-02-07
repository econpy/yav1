from datetime import datetime
from pandas import isnull


def convert_time(tstamp):
    """ Convert Unix timestamp to YYYY-MM-DD HH:MM:SS string """
    if isinstance(tstamp, int):
        dt = datetime.fromtimestamp(tstamp)
        if dt.year >= 2013:
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        else:
            print 'WARNING: Found timestamp from %s: %s' % (dt.year, tstamp)
            return None
    else:
        print 'WARNING: Found non-integer timestamp: %s' % tstamp
        return None


def convert_freq(freq):
    if isinstance(freq, int):
        freq_str = str(freq)
        if len(freq_str) == 5:
            freq_float_str = '%s.%s' % (freq_str[:2], freq_str[2:])
            return float(freq_float_str)
        else:
            print 'WARNING: Found frequency of < 5 characters: %s' % freq
            return None
    else:
        print 'WARNING: Found non-integer frequency: %s' % freq
        return None


def convert_direction(direction):
    dirdct = {0: 'Front', 1: 'Rear', 2: 'Side'}
    if direction in dirdct:
        return dirdct[direction]
    else:
        print 'WARNING: Found value for direction equal to %s.' % direction
        return None


def convert_flag(flag):
    flagdct = {1: 'Priority', 2: 'Hasbox', 4: 'Inbox', 8: 'Lockoutable',
               16: 'Lockout', 32: 'Mute', 64: 'Filter', 128: 'Log1',
               129: 'Log2', 256: 'Checkable', 512: 'True', 1024: 'False',
               2048: 'Moving', 4096: 'Static', 8192: 'IO'}
    if flag in flagdct:
        return flagdct[flag]
    else:
        print 'WARNING: Found value for flag equal to %s.' % flag
        return None


def convert_speed(speed):
    """ Convert meters per second to MPH """
    if isinstance(speed, float) or isinstance(speed, int):
        if speed >= 0:
            return round(speed*2.23693629, 3)
        elif speed < 0:
            print 'WARNING: Found value for speed equal to %s.' % speed
            return 0  # Perhaps this should be None. What causes speed < 0?
        elif isnull(speed):
            return None
        else:
            print 'WARNING: Encountered a strange speed value: %s' % speed
            return None
    else:
        return None


def CleanLogData(dframe, dropnans=False):
    dframe['timestamp'] = dframe['timestamp'].map(convert_time)
    dframe['frequency'] = dframe['frequency'].map(convert_freq)
    dframe['direction'] = dframe['direction'].map(convert_direction)
    dframe['flag'] = dframe['flag'].map(convert_flag)
    dframe['speed'] = dframe['speed'].map(convert_speed)
    if dropnans:
        dframe.dropna(how='any', inplace=True)
        dframe.reset_index(inplace=True)
        if len(dframe.index) > 0:
            return dframe
        else:
            return None
    else:
        return dframe
