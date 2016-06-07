#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.util.common import BASE_DIR
import tushare as ts
import datetime as dt


class Cache:

    def __init__(self):
        pass

    def _get_cache_file_name(self, code, ktype, date):
        pass

    def _get_last_cache(self, *args, **kwargs):
        print kwargs

    def _get_earliest_cache(self, code, ktype, date):
        pass

    def is_data_in_cache(self, code, ktype, date):
        '''
        判断数据是否在Cache目录
        :param ktype:
        :param date:
        :return:
        '''
        pass

    def _write_data_to_cache(self, code, ktype, month):
        pass

    def get_kline_data(self, *args, **kwargs):
        self._get_last_cache(*args, **kwargs)
        # one_day = dt.timedelta(days=1)
        # start = processing = dt.datetime.strptime(kwargs['start'], '%Y-%m-%d')
        # end = dt.datetime.strptime(kwargs['end'], '%Y-%m-%d')
        # while processing is None or processing <= end:
        #     month_str = processing.strftime('%Y-%m')
        #     save_path = BASE_DIR + '/cache/30/' + month_str + '%' + kwargs['code']+'.csv'
        #     ts.get_hist_data(code=kwargs['code'], ktype='30', start=month_str + '-01', end=month_str + '-31').to_csv(save_path)
        #     processing = processing + one_day
        # return func(*args, **kwargs)
        return kwargs


def read_cache(func):

    cache = Cache()

    def wrap_function(*args, **kwargs):
        return cache.get_kline_data(*args, **kwargs)
        # return func(*args, **kwargs)

    return wrap_function


