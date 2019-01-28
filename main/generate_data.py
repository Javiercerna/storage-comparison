# default_structure = ['ID', 'timestamp', 'sensor1', 'sensor2', 'sensor3', ..., 'sensor15']

import pprint
import random
import datetime

MAX_VALUE = 1e10
N_SENSORS = 15


def generateData(id, n_data, time_delta_seconds, initial_time=datetime.datetime.now()):
    data_list = []
    for data_index in range(n_data):
        new_data = {'ID': id}
        timestamp = initial_time + datetime.timedelta(seconds=time_delta_seconds*data_index)
        new_data['timestamp'] = str(timestamp)

        for sensor_index in range(1, N_SENSORS + 1):
            new_data['sensor' + str(sensor_index)] = MAX_VALUE * random.random()

        data_list.append(new_data)
    return data_list


if __name__ == '__main__':
    pprint.pprint(generateData(id=1, n_data=100, time_delta_seconds=2))

