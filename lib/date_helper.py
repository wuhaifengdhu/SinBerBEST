#!/usr/bin/python
# -*- coding: utf-8 -*-
import time


class DateHelper(object):
    @staticmethod
    def get_current_date():
        return time.strftime('%Y_%m_%d')

if __name__ == '__main__':
    print (DateHelper.get_current_date())

