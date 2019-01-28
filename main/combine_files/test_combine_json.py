from main.generate_data import generateData

import datetime
import json
import time
import os


def combineJsonData(candidate_files):
    combined_json = []
    for filename in candidate_files:
        with open(filename, 'r') as f:
            combined_json += json.load(f)

    return combined_json


def combineJsonFiles():
    filenames = os.listdir(os.getcwd())
    candidate_files = []
    for filename in filenames:
        if filename.endswith('.json'):
            candidate_files.append(filename)

    combined_json = combineJsonData(candidate_files)
    with open('results.json', 'w') as f:
        json.dump(combined_json, f)

def clearPreviousData():
    filenames = os.listdir(os.getcwd())
    for filename in filenames:
        if filename.endswith('.json'):
            os.remove(filename)


def storeDataInJsonFile(data_list, file_suffix):
    with open('data%03d.json' % (file_suffix), 'w') as f:
        json.dump(data_list, f)


# Usual input (1 s of data for 5 minutes = 300 data values
#              12 files each hour for 24 hours = 288 files)
n_data = 5 * 60
time_delta_seconds = 1
n_files = 12 * 24

clearPreviousData()

print 'Creating new json files...'
initial_time = datetime.datetime.now()
for file_index in range(n_files):
    data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds,
                             initial_time=initial_time)
    initial_time = datetime.datetime.strptime(data_list[-1]['timestamp'], '%Y-%m-%d %H:%M:%S.%f') + \
                    datetime.timedelta(seconds=time_delta_seconds)
    storeDataInJsonFile(data_list, file_index)
print 'New json files have been created (n_files=%s)' % (n_files)

initial_time = time.time()
combineJsonFiles()
elapsed_seconds = time.time() - initial_time
print '\nElapsed seconds for usual input (n_data=%s, time_delta_seconds=%s, n_files=%s): %.3f' % \
              (n_data, time_delta_seconds, n_files, elapsed_seconds)

# Max input (0.2 s of data for 5 minutes = 1500 data values)
#            12 files each hour for 24 hours = 288 files)
n_data = 5 * 5 * 60
time_delta_seconds = 0.2
n_files = 12 * 24

clearPreviousData()

print 'Creating new json files...'
initial_time = datetime.datetime.now()
for file_index in range(n_files):
    data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds,
                             initial_time=initial_time)
    initial_time = datetime.datetime.strptime(data_list[-1]['timestamp'], '%Y-%m-%d %H:%M:%S.%f') + \
                    datetime.timedelta(seconds=time_delta_seconds)
    storeDataInJsonFile(data_list, file_index)
print 'New json files have been created (n_files=%s)' % (n_files)

initial_time = time.time()
combineJsonFiles()
elapsed_seconds = time.time() - initial_time
print '\nElapsed seconds for max input (n_data=%s, time_delta_seconds=%s, n_files=%s): %.3f' % \
              (n_data, time_delta_seconds, n_files, elapsed_seconds)
