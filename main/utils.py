import json
import os


def clearPreviousData():
    filenames = os.listdir(os.getcwd())
    for filename in filenames:
        if filename.endswith('.json'):
            os.remove(filename)


def storeDataInJsonFile(data_list, file_suffix=0):
    with open('data%03d.json' % (file_suffix), 'w') as f:
        json.dump(data_list, f)
