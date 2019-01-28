from main.generate_data import generateData
from main.utils import clearPreviousData, storeDataInJsonFile

import datetime
import json
import random
import time


def generateRandomTimestampInRange(initial_timestamp_str, final_timestamp_str):
    initial_timestamp = datetime.datetime.strptime(initial_timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    final_timestamp = datetime.datetime.strptime(final_timestamp_str, '%Y-%m-%d %H:%M:%S.%f')

    return initial_timestamp + datetime.timedelta(
        seconds=random.randint(0, int((final_timestamp - initial_timestamp).total_seconds()))
    )


def isDataInTimestampRange(data, initial_timestamp_str, final_timestamp_str):
    initial_timestamp = datetime.datetime.strptime(initial_timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    final_timestamp = datetime.datetime.strptime(final_timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
    data_timestamp = datetime.datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

    return initial_timestamp <= data_timestamp <= final_timestamp


def queryJsonFile(initial_desired_timestamp, final_desired_timestamp, filename):
    with open(filename, 'r') as f:
        data_query = [data for data in json.load(f) \
                      if isDataInTimestampRange(data, initial_desired_timestamp, final_desired_timestamp)]
    return data_query


# Usual input: Simulated 24 hour file (1 s of data for 24 hours = 86400 data values)
n_data = 60 * 60 * 24
time_delta_seconds = 1
data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds)

clearPreviousData()
storeDataInJsonFile(data_list)

first_timestamp = data_list[0]['timestamp']
last_timestamp = data_list[-1]['timestamp']

worst_time_seconds = -1
for _ in range(10):
    initial_timestamp = str(generateRandomTimestampInRange(first_timestamp, last_timestamp))
    final_timestamp = str(generateRandomTimestampInRange(str(initial_timestamp), last_timestamp))

    print 'Initial timestamp: %s' % (initial_timestamp)
    print 'Final timestamp: %s' % (final_timestamp)

    initial_time = time.time()
    data_query = queryJsonFile(initial_timestamp, final_timestamp, 'data000.json')
    elapsed_seconds = time.time() - initial_time
    print '\nElapsed seconds for usual input 1 (total_data=%s, data_query=%s): %.3f' % \
                  (len(data_list), len(data_query), elapsed_seconds)

    if elapsed_seconds > worst_time_seconds:
        worst_time_seconds = elapsed_seconds

print '\nWorst time in seconds: %.3f' % (worst_time_seconds)

# Max input: Simulated 24 hour file (0.2 s of data for 24 hours = 432000 data values)
n_data = 5 * 60 * 60 * 24
time_delta_seconds = 0.2
data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds)

clearPreviousData()
storeDataInJsonFile(data_list)

first_timestamp = data_list[0]['timestamp']
last_timestamp = data_list[-1]['timestamp']

worst_time_seconds = -1
for _ in range(10):
    initial_timestamp = str(generateRandomTimestampInRange(first_timestamp, last_timestamp))
    final_timestamp = str(generateRandomTimestampInRange(str(initial_timestamp), last_timestamp))

    print 'Initial timestamp: %s' % (initial_timestamp)
    print 'Final timestamp: %s' % (final_timestamp)

    initial_time = time.time()
    data_query = queryJsonFile(initial_timestamp, final_timestamp, 'data000.json')
    elapsed_seconds = time.time() - initial_time
    print '\nElapsed seconds for max input (total_data=%s, data_query=%s): %.3f' % \
                  (len(data_list), len(data_query), elapsed_seconds)

    if elapsed_seconds > worst_time_seconds:
        worst_time_seconds = elapsed_seconds

print '\nWorst time in seconds: %.3f' % (worst_time_seconds)