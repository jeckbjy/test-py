import akshare as ak
from datetime import datetime, date, timedelta

yesterday = date.today() + timedelta(days = -1) 

# date = time.strftime("%Y%m%d", time.localtime())
date = yesterday.strftime("%Y%m%d")
print("trade_date",date)

# 股票指数-成份股-所有可以获取的指数表
# index_stock_info = ak.index_stock_info()
# print(index_stock_info)

# 股票指数-成份股-最新成份股获取
# index_stock_cons = ak.index_stock_cons(index="000001")
# print(index_stock_cons)

# 交易法门-工具-席位分析
# jyfm_tools_position_structure = ak.jyfm_tools_position_structure(trade_date=date)
# print(jyfm_tools_position_structure)

# stock_em_comment = ak.stock_em_comment()
# print(stock_em_comment)

# stock_em_hsgt_institution_statistics = ak.stock_em_hsgt_institution_statistics(start_date=date, end_date=date)
# print("沪深港通持股-每日机构统计")
# print(stock_em_hsgt_institution_statistics)

stock_institute_hold = ak.stock_institute_hold(quarter="20212")
print("机构持股一览表")
print(stock_institute_hold)