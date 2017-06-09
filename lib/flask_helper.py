from bib_reader import BibReader
from system_helper import SystemHelper
from http_helper import HttpHelper
import time
import os
import json


class FlaskHelper(object):
    @staticmethod
    def start_read_service(data_directory, data_store_file, read_frequency=15, server_url=None):
        reader = BibReader(data_directory)
        print ("Start service reading bib device records!")
        while True:
            new_data = reader.read_new_data()
            print ("READING....NEW...DATA<<<<")
            print (os.linesep.join(new_data))
            print ("Finished reading!")
            SystemHelper.append_to_file(data_store_file, os.linesep.join(new_data))
            # send data to server back-end
            if server_url is not None:
                HttpHelper.post(server_url, json.dumps(new_data))
            time.sleep(read_frequency)