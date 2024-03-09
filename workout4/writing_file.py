'''writing down the data from web API into a file named by a user'''
import json


def write_in_file(data, name):
    '''writing data in a file'''
    file_out = open(name, 'w', encoding = 'utf-8')
    json.dump(data,file_out)
    file_out.close()
