#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


class TextHelper(object):
    @staticmethod
    def get_time_from_file_path(file_path):
        result = re.findall(r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', file_path)
        return result[0] if len(result) >=1 else None


if __name__ == '__main__':
    print TextHelper.get_time_from_file_path("/Users/hfwu/Desktop/bib/BIB29/data/2017_05_11/2017_04_25_17_03_09_BIB_BRIEFCASE_29_data.csv")