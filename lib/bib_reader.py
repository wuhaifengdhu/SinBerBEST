#!/usr/bin/python
# -*- coding: utf-8 -*-
from date_helper import DateHelper
from system_helper import SystemHelper


class BibReader(object):
    def __init__(self, data_directory, processed_gz_folder='old_gz'):
        self.directory = data_directory
        self.last_read_date = None
        self.new_data = []
        self.processed_gz_folder_name = processed_gz_folder

    def _get_processed_gz_folder(self, parent_folder):
        return SystemHelper.join_path(parent_folder, self.processed_gz_folder_name)

    def _get_folder_by_date(self, date_str):
        return SystemHelper.join_path(self.directory, date_str)

    def _is_date_change(self):
        now_date = DateHelper.get_current_date()
        if self.last_read_date is not None and self.last_read_date != now_date:
            return True
        return False

    def _read_file_in_folder(self, date_folder):
        # step 1, get folder path, create if not exist
        processed_gz_folder = self._get_processed_gz_folder(date_folder)

        # step 2, get all gz file list
        gz_file_list = [f for f in SystemHelper.list_files_in_directory(date_folder) if f.endswith('.gz')]
        print (gz_file_list)

        # step 3, read data from gz file
        for gz_file in gz_file_list:
            self.new_data.append(SystemHelper.read_gz_file(gz_file))
            SystemHelper.move_to_folder(gz_file, processed_gz_folder)

    def _read_last_date_file(self):
        last_date_folder = self._get_folder_by_date(self.last_read_date)
        self._read_file_in_folder(last_date_folder)

    def read_new_data(self):
        self.new_data = []
        if self._is_date_change():
            self._read_last_date_file()
        self._read_today_data()
        return self.new_data

    def _read_today_data(self):
        self.last_read_date = DateHelper.get_current_date()
        self._read_last_date_file()


if __name__ == '__main__':
    reader = BibReader("../resource/data")
    print (reader.read_new_data())
