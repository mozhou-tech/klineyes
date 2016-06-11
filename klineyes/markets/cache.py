#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.util.common import BASE_DIR
import tushare as ts
import datetime as dt
import os.path
from dateutil.relativedelta import relativedelta
from time import sleep
import pandas as pd

class Cache:

    def __init__(self):
        pass

    @classmethod
    def _get_date_range_of_month(self, date, dtype='str'):
        '''
        获取某个日期所在月的开始日期和结束日期
        :param date: 日期
        :param dtype: 返回数据类型，str  or  datetime
        :return:
        '''
        one_day = dt.timedelta(days=1)
        month_start = dt.datetime.strptime(date[:7], '%Y-%m')
        month_end = (month_start + relativedelta(months=1)) - one_day
        if dtype == 'str':
            return month_start.strftime('%Y-%m-%d'), month_end.strftime('%Y-%m-%d')
        elif dtype == 'datetime':
            return month_start, month_end

    @classmethod
    def _get_cache_filename(self, code, date, ktype):
        '''
        获取缓存文件名称
        :param code: 股票代码
        :param date: 日期
        :param ktype: k线type
        :return:
        '''
        return BASE_DIR + '/cache/' + ktype + '/' + date[:7] + '%' + code + '.csv'

    @classmethod
    def _cache_monthly(self, code, ktype, date):
        '''
        缓存date所在月的数据，等缓存成功后返回True
        :param code:
        :param ktype:
        :param date:
        :return:
        '''
        start, end = self._get_date_range_of_month(date, 'str')
        df = ts.get_hist_data(code=code, ktype=ktype, start=start, end=end, retry_count=6)
        if df is not None:
            df.to_csv(self._get_cache_filename(code, date, ktype))

        waiting_seconds = 0
        while not self._in_cache(ktype=ktype, code=code, date=date):
            sleep(1)
            waiting_seconds += 1
            if waiting_seconds > 30:
                self._cache_monthly(code=code, ktype=ktype, date=date)
        return True


    @classmethod
    def _in_cache(self, ktype, code, date):
        '''
        判断数据是否在Cache目录
        :param ktype:
        :param date:
        :return:
        '''
        filename = self._get_cache_filename(code=code, date=date, ktype=ktype)
        return os.path.isfile(filename)

    @classmethod
    def _date_range_to_month_list(self, start, end):
        '''
        时间范围转换成月份列表（准备要加载的缓存文件）
        :param start:
        :param end:
        :return:
        '''
        processing = dt.datetime.strptime(start, '%Y-%m-%d')   # start date
        end = dt.datetime.strptime(end, '%Y-%m-%d')
        month_list = []
        while processing <= end:
            month_list.append(processing.strftime('%Y-%m-%d'))
            processing = processing + relativedelta(months=1)
        month_list.append(processing.strftime('%Y-%m-%d'))
        return month_list

    def _read_from_cache(self, code, ktype, date):
        '''
        从缓存中，读取对应类型的数据
        :param code:
        :param ktype:
        :param date:
        :return:
        '''
        return pd.read_csv(self._get_cache_filename(code=code, ktype=ktype, date=date))

    def _is_cache_file_whole(self, *args, **kwargs):
        print kwargs

    @classmethod
    def _apply_daterange(self, df, start, end):
        '''
        根据传入的dataframe 切分出具体想要的时间范围
        :param df:
        :param start:
        :param end:
        :return:
        '''
        df = df.sort_values(by='date')
        return df[(start <= df.date) & (end >= df.date)].reset_index(drop=True)

    def get_kline_data(self, ktype, code, start, end):
        months = self._date_range_to_month_list(start, end)
        ret_df = None
        for date in months:
            if self._in_cache(ktype=ktype, code=code, date=date) is not True:   # 缓存里找不到，就从网络获取
                print 'caching....'
                self._cache_monthly(code=code, ktype=ktype, date=date)
            date_df = self._read_from_cache(code=code, ktype=ktype, date=date)
            if ret_df is None:
                ret_df = date_df
            else:
                ret_df = ret_df.append(date_df, ignore_index=True)
        return self._apply_daterange(ret_df, start, end)


def read_cache(func):

    def wrap_function(*args, **kwargs):
        cache = Cache()
        return cache.get_kline_data(ktype=kwargs['ktype'], code=kwargs['code'], start=kwargs['start'], end=kwargs['end'])
        # return func(*args, **kwargs)

    return wrap_function


