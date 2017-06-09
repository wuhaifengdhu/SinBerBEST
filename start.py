from threading import Thread
from lib.config_helper import ConfigHelper
from lib.flask_helper import FlaskHelper
import subprocess
from time import sleep


def start_server_thread():
    subprocess.call(['java', '-Djava.util.logging.config.file=logging.properties', '-jar', 'BIB_Briefcase_Server.jar'])


def start_bib_reader(config_file='configuration.properties'):
    property_dict = ConfigHelper.parse(config_file)
    bib_data_folder = property_dict['SFTPWORKINGDIR']
    log_file = property_dict['BIB_READ_LOG_FILE']
    _server_url = property_dict['POST_SERVER_URL']

    # step 2. Start service to read
    try:
        FlaskHelper.start_read_service(bib_data_folder, log_file, server_url=_server_url)
    except KeyboardInterrupt:
        print ("Service stopped as user interrupt from user command!")


if __name__ == '__main__':
    print ("Starting BIB reader!")
    bib_reader_thread = Thread(target=start_bib_reader)
    bib_reader_thread.start()
    print ("BIB reader start finished!")
    sleep(30)

    print ("Starting BIB server!")
    bib_server_thread = Thread(target=start_server_thread)
    bib_server_thread.start()
    print ("BIB server start finished!")

    # bib_reader_thread.join()
    # bib_server_thread.join()




