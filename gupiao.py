import tushare as ts
ts.set_token('8d07aac9a2a04897ad28aeb384d107a2f9162fc9882552efc7eb9d30')
#pro = ts.pro_api()
#获取股票基本信息
#data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
#获取股票日线行情
#daily_data=pro.daily(exchange='', list_status='L',fields='ts_code,trade_date,open,high,low,pct_chg')
#df = daily_data.sort_values('ts_code',ascending=True)
#df = ts.pro_bar(ts_code='000001.SZ', adj='qfq', start_date='20220317', end_date='20220319')
#获取所有A股实时行情
def get_A():
    df=ts.get_today_all()
    df.rename(columns = {"code": "股票代码", "name":"名称","changepercent":"涨跌幅",
                            "trade":"当前价","open":"开盘价","high":"最高价","low":"最低价",
                            "settlement":"收盘价","volume":"成交量","turnoverratio":"换手率",
                            "amount":"成交额","per":"市盈率","pb":"市净率",
                            "mktcap":"市值","nmc":"流通市值"},  inplace=True)
    df.to_csv('result.csv',encoding="utf_8_sig")
    df = df.sort_values('股票代码',ascending=True)
    print(df[df['涨跌幅']>9])
if __name__ == '__main__':
    get_A()
    