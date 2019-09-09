import time
import requests
import tushare as ts
import pandas as pd
import numpy as np


class Stock():
    def __init__(self,q):
        self.q = q
        # self.stock_num = stock_num
        # self._terminal = True

    def query_stock_real_price(self):
        df = ts.get_realtime_quotes(self.stock_num)
        df = df[['price', 'time']]
        price = df['price'].values[0]
        time = df['time'].values[0]
        return price, time


    def get_kline_data(self, ktype='ma5'):
        today = datetime.now().strftime('%Y-%m-%d')
        df = ts.get_hist_data(self.stock_num, start='2018-08-08', end=today)
        return (df[[ktype]])

    def get_hour_data(self,code):
        df = ts.get_hist_data(code,ktype = 'D')  # 获取60分钟k线数据
        # self.write_data(code,df)
        print(df.columns)
        # for i in df.loc[:,'close']:
        #     print(i)
        # print(ts.get_today_all())

    def get_kx_data(self,code):
        df = ts.get_k_data(code,ktype = 'D')  # 获取60分钟k线数据
        # self.write_data(code,df)
        print(df.columns)


    def write_data(self,code,data):
        with open('{}.txt'.format(code),'w') as f:
            for i in range(data.shape[0]):
                if i != 0:
                    f.write('%s' % data.loc[i:i,:])
                    print('{}行'.format(i))

    def start_run(self):
        while self._terminal:
            p,t =  self.query_stock_real_price()
            print('>>{}:stock price {}'.format(t,p))
            real_price = float(p)
            self.q.put(real_price)
            time.sleep(3)

    def get_histort(self):
        data = ts.get_hist_data('600848')
        # self.write_data(111,data)
        # for i in range(data.shape[0]):
        #     print('%s' % data.loc[i:i+1,'open'])
        print(data.columns)

    def get_daly(self,code):
        data = ts.get_today_all()
        print(data)

    def stop_run(self):
        self._terminal = False



if __name__ == '__main__':
    stock = Stock(1)
    # codelist = []
    # with open('all.txt', 'rt') as f:
    #     a = f.readlines()
    # for i in a:
    #     c = i.replace('\n', '')
    #     data = c.split('\t')[0]
    #     codelist.append(data)
    # for code in codelist:
    #     time.sleep(1)
    #     stock.get_hour_data(code)

    # stock.get_hour_data('600549')
    # stock.get_kx_data('600549')
    # stock.get_histort()
    stock.get_daly('600549')

    # Index(['open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
           # 'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover'],