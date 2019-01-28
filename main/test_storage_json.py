from generate_data import generateData
from utils import clearPreviousData, storeDataInJsonFile

import time


# Usual input (1 s of data for 5 minutes = 300 data values)
n_data = 5 * 60
time_delta_seconds = 1
data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds)

clearPreviousData()
initial_time = time.time()
storeDataInJsonFile(data_list)
elapsed_seconds = time.time() - initial_time
print '\nElapsed seconds for usual input (n_data=%s, time_delta_seconds=%s): %.3f' % \
              (n_data, time_delta_seconds, elapsed_seconds)

# Max input (1 s of data for 24 hours = 86400 data values)
n_data = 60 * 60 * 24
time_delta_seconds = 1
data_list = generateData(id=1, n_data=n_data, time_delta_seconds=time_delta_seconds)

clearPreviousData()
initial_time = time.time()
storeDataInJsonFile(data_list)
elapsed_seconds = time.time() - initial_time
print '\nElapsed seconds for max input (n_data=%s, time_delta_seconds=%s): %.3f' % \
              (n_data, time_delta_seconds, elapsed_seconds)