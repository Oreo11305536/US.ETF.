import yfinance as yf
import pandas as pd
from datetime import datetime

proxy_chains = {
    'SCHD': [(1993, 2006, 'VEIPX'), (2007, 2011, 'VYM'), (2012, 2030, 'SCHD')],
    'DGRO': [(1993, 2005, 'VDIGX'), (2006, 2014, 'VIG'), (2015, 2030, 'DGRO')],
    'VPU':  [(1993, 2004, 'FKUTX'), (2005, 2030, 'VPU')],
    'VOO':  [(1993, 2010, 'SPY'), (2011, 2030, 'VOO')],
    'QQQM': [(1993, 1999, '^NDX'), (2000, 2020, 'QQQ'), (2021, 2030, 'QQQM')],
    'SMH':  [(1993, 2000, 'FSELX'), (2001, 2030, 'SMH')],
    'VGT':  [(1993, 1998, 'FSPTX'), (1999, 2004, 'XLK'), (2005, 2030, 'VGT')]
}

start_year = 1993
end_year = datetime.now().year
database = {year: {} for year in range(start_year, end_year + 1)}

def get_annual_data(ticker, start_y, end_y):
    # 下载历史
    stock = yf.Ticker(ticker)
    df = stock.history(start=f"{start_y-1}-12-01", end=f"{end_y+1}-01-01")
    if df.empty: return {}
    annual_data = {}
    for year in range(start_y, min(end_y + 1, end_year + 1)):
        try:
            prev = df[df.index.year == year - 1]
            curr = df[df.index.year == year]
            if prev.empty or curr.empty: continue
            
            p_close = prev.iloc[-1]['Close']
            c_close = curr.iloc[-1]['Close']
            cap_ret = (c_close - p_close) / p_close
            divs = curr['Dividends'].sum()
            dy = divs / p_close if p_close > 0 else 0
            if ticker == '^NDX': dy = 0.002
            
            annual_data[year] = [round(cap_ret, 4), round(dy, 4)]
        except:
            pass
    return annual_data

for asset, chain in proxy_chains.items():
    for start, end, ticker in chain:
        data = get_annual_data(ticker, start, end)
        for y, metrics in data.items():
            database[y][asset] = metrics

# 把数据直接写入 JS 文件
with open("data.js", "w") as f:
    f.write("window.proxyDatabase = {\n")
    for year in sorted(database.keys()):
        assets = []
        for asset in proxy_chains.keys():
            m = database[year].get(asset, [0.08, 0.02])
            assets.append(f"'{asset}': [{m[0]:.4f}, {m[1]:.4f}]")
        f.write(f"    {year}: {{ {', '.join(assets)} }},\n")
    f.write("};\n")
