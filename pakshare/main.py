import akshare as ak
from datetime import datetime, date, timedelta

yesterday = date.today() + timedelta(days = -1) 

# date = time.strftime("%Y%m%d", time.localtime())
date = yesterday.strftime("%Y%m%d")
print("trade_date",date)

# 龙虎榜-每日详情
lhb_detail_daily = ak.stock_sina_lhb_detail_daily(trade_date=date)
print("每日详情")
print(lhb_detail_daily)

# 龙虎榜-个股上榜统计
lhb_ggtj = ak.stock_sina_lhb_ggtj(recent_day="1")
print("个股上榜统计")
print(lhb_ggtj)

# 龙虎榜-营业上榜统计
lhb_yytj = ak.stock_sina_lhb_yytj(recent_day="1")
print("营业上榜统计")
print(lhb_yytj)

# 龙虎榜-机构席位追踪
lhb_jgzz = ak.stock_sina_lhb_jgzz(recent_day="1")
print("机构席位追踪")
print(lhb_jgzz)

# 龙虎榜-机构席位成交明细
lhb_jgmx = ak.stock_sina_lhb_jgmx()
print("机构席位成交明细")
print(lhb_jgmx)

# 股票指数-成份股-最新成份股获取
index_stock_cons = ak.index_stock_cons()