#!/usr/bin/python
# -*- coding: UTF-8 -*-

from klineyes.util.common import BASE_DIR
import tushare as ts
import datetime as dt
import os.path
from dateutil.relativedelta import relativedelta
from time import sleep,ctime,strftime,gmtime
import pandas as pd

class Cache:

    def __init__(self, ktype, code, start, end):
        self.ktype = ktype
        self.code = code
        self.start = start
        self.end = end

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

    def _get_cache_filename(self, date):
        '''
        获取缓存文件名称
        :param code: 股票代码
        :param date: 日期
        :param ktype: k线type
        :return:
        '''
        return BASE_DIR + '/cache/' + self.ktype + '/' + date[:7] + '%' + self.code + '.csv'

    def _cache_monthly(self, date):
        '''
        缓存date所在月的数据，等缓存成功后返回True
        :param code:
        :param ktype:
        :param date:
        :return:
        '''
        print 'caching...'
        start, end = self._get_date_range_of_month(date, 'str')
        df = ts.get_hist_data(code=self.code, ktype=self.ktype, start=start, end=end, retry_count=6)
        if df is not None:
            df.to_csv(self._get_cache_filename(date))

        waiting_seconds = 0
        while not self._in_cache(date=date):
            sleep(1)
            waiting_seconds += 1
            if waiting_seconds > 30:
                self._cache_monthly(date=date)
        return True

    def _in_cache(self, date):
        '''
        判断数据是否在Cache目录
        :param date:
        :return:
        '''
        filename = self._get_cache_filename(date=date)
        return os.path.isfile(filename)

    def _date_range_to_month_list(self):
        '''
        时间范围转换成月份列表（准备要加载的缓存文件）
        :return:
        '''
        # start date, use bigest day value,for check cache in self._is_cache_file_updated
        processing = dt.datetime.strptime(self.start[:7] + self.end[7:], '%Y-%m-%d')
        end = dt.datetime.strptime(self.end, '%Y-%m-%d')
        month_list = []
        while processing <= end:
            month_list.append(processing.strftime('%Y-%m-%d'))
            processing = processing + relativedelta(months=1)
        return month_list

    def _read_from_cache(self, date):
        '''
        从缓存中，读取对应类型的数据
        :param code:
        :param ktype:
        :param date:
        :return:
        '''
        if self._is_cache_file_updated(date) is False:
            print 'refresh caching of month '+ date[:7]
            self._cache_monthly(date)
        return pd.read_csv(self._get_cache_filename(date=date))


    def _is_cache_file_updated(self, date):
        '''
        判断缓存文件是不是最新的，如果不是的话要刷新
        :param date:
        :return:
        '''
        cache_date = dt.datetime.strptime(strftime('%Y-%m-%d', gmtime(os.path.getmtime(self._get_cache_filename(date)))), '%Y-%m-%d')
        date = dt.datetime.strptime(date, '%Y-%m-%d')
        # 如果当天更新过，就返回是最新的，否则下载日期大于索取的数据的日期的就是最新的
        if cache_date == dt.datetime.strptime(strftime('%Y-%m-%d'), '%Y-%m-%d'):
            return True
        return date < cache_date


    def _apply_daterange(self, df):
        '''
        根据传入的dataframe 切分出具体想要的时间范围
        :param df:
        :param start:
        :param end:
        :return:
        '''
        df = df.sort_values(by='date')
        return df[(self.start <= df.date) & (self.end >= df.date)].reset_index(drop=True)

    def get_kline_data(self):
        '''
        入口函数
        :return:
        '''
        months = self._date_range_to_month_list()
        ret_df = None
        for date in months:
            if self._in_cache(date=date) is not True:   # 缓存里找不到，就从网络获取
                print 'caching....'
                self._cache_monthly(date=date)
            date_df = self._read_from_cache(date=date)
            if ret_df is None:
                ret_df = date_df
            else:
                ret_df = ret_df.append(date_df, ignore_index=True)
        return self._apply_daterange(ret_df)


def read_cache(func):

    def wrap_function(*args, **kwargs):
        cache = Cache(ktype=kwargs['ktype'], code=kwargs['code'], start=kwargs['start'], end=kwargs['end'])
        return cache.get_kline_data()
        # return func(*args, **kwargs)

    return wrap_function


