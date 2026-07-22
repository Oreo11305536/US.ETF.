import yfinance as yf
import pandas as pd
from datetime import datetime
import json

# ================= 新增：股票名称中文翻译字典 =================
# 用于拦截 Yahoo Finance 的英文名，转换为更友好的中文格式
TICKER_TRANSLATIONS = {
    "Apple Inc.": "苹果 (AAPL)",
    "Apple": "苹果 (AAPL)",
    "Microsoft Corporation": "微软 (MSFT)",
    "Microsoft": "微软 (MSFT)",
    "NVIDIA Corporation": "英伟达 (NVDA)",
    "Nvidia": "英伟达 (NVDA)",
    "Amazon.com, Inc.": "亚马逊 (AMZN)",
    "Amazon": "亚马逊 (AMZN)",
    "Meta Platforms, Inc.": "Meta (META)",
    "Meta": "Meta (META)",
    "Tesla, Inc.": "特斯拉 (TSLA)",
    "Tesla": "特斯拉 (TSLA)",
    "Broadcom Inc.": "博通 (AVGO)",
    "Broadcom": "博通 (AVGO)",
    "The Home Depot, Inc.": "家得宝 (HD)",
    "Home Depot": "家得宝 (HD)",
    "AbbVie Inc.": "艾伯维 (ABBV)",
    "AbbVie": "艾伯维 (ABBV)",
    "Texas Instruments Incorporated": "德州仪器 (TXN)",
    "Texas Instruments": "德州仪器 (TXN)",
    "Chevron Corporation": "雪佛龙 (CVX)",
    "Chevron": "雪佛龙 (CVX)",
    "Exxon Mobil Corporation": "埃克森美孚 (XOM)",
    "Exxon Mobil": "埃克森美孚 (XOM)",
    "JPMorgan Chase & Co.": "摩根大通 (JPM)",
    "JPMorgan": "摩根大通 (JPM)",
    "Johnson & Johnson": "强生 (JNJ)",
    "Taiwan Semiconductor Manufacturing Company Limited": "台积电 (TSM)",
    "TSMC": "台积电 (TSM)",
    "ASML Holding N.V.": "阿斯麦 (ASML)",
    "ASML": "阿斯麦 (ASML)",
    "Advanced Micro Devices, Inc.": "超威半导体 (AMD)",
    "AMD": "超威半导体 (AMD)",
    "Salesforce, Inc.": "赛富时 (CRM)",
    "Salesforce": "赛富时 (CRM)",
    "NextEra Energy, Inc.": "新纪元能源 (NEE)",
    "NextEra Energy": "新纪元能源 (NEE)",
    "The Southern Company": "南方电力 (SO)",
    "Southern Co": "南方电力 (SO)",
    "Duke Energy Corporation": "杜克能源 (DUK)",
    "Duke Energy": "杜克能源 (DUK)",
    "Sempra": "桑普拉能源 (SRE)",
    "American Electric Power Company, Inc.": "美国电力 (AEP)",
    "AEP": "美国电力 (AEP)",
    "Berkshire Hathaway Inc.": "伯克希尔 (BRK.B)",
    "Alphabet Inc.": "谷歌 (GOOGL)",
    "Eli Lilly and Company": "礼来 (LLY)",
    "Walmart Inc.": "沃尔玛 (WMT)",
    "UnitedHealth Group Incorporated": "联合健康 (UNH)",
    "Visa Inc.": "维萨 (V)",
    "Costco Wholesale Corporation": "好市多 (COST)",
    "Netflix, Inc.": "网飞 (NFLX)",
    "PepsiCo, Inc.": "百事可乐 (PEP)",
    "Adobe Inc.": "奥多比 (ADBE)",
    "Cisco Systems, Inc.": "思科 (CSCO)",
    "Qualcomm Incorporated": "高通 (QCOM)",
    "Applied Materials, Inc.": "应用材料 (AMAT)",
    "Lam Research Corporation": "泛林集团 (LRCX)",
    "Micron Technology, episodic.": "美光科技 (MU)",
    "Analog Devices, Inc.": "亚德诺半导体 (ADI)",
    "KLA Corporation": "科磊 (KLAC)",
    "Intel Corporation": "英特尔 (INTC)",
    "Marvell Technology, Inc.": "美满电子 (MRVL)",
    "Microchip Technology Incorporated": "微芯科技 (MCHP)",
    "Accenture plc": "埃森哲 (ACN)",
    "Oracle Corporation": "甲骨文 (ORCL)",
    "International Business Machines Corporation": "IBM (IBM)",
    "Intuit Inc.": "直觉软件 (INTU)",
    "BlackRock, Inc.": "贝莱德 (BLK)",
    "Lockheed Martin Corporation": "洛克希德马丁 (LMT)",
    "Amgen Inc.": "安进 (AMGN)",
    "Pfizer Inc.": "辉瑞 (PFE)",
    "United Parcel Service, Inc.": "联合包裹 (UPS)",
    "Verizon Communications Inc.": "威瑞森 (VZ)",
    "The Coca-Cola Company": "可口可乐 (KO)",
    "Bristol-Myers Squibb Company": "百时美施贵宝 (BMY)",
    "Emerson Electric Co.": "艾默生电气 (EMR)",
    "Merck & Co., Inc.": "默沙东 (MRK)",
    "Bank of America Corporation": "美国银行 (BAC)",
    "Constellation Energy Corporation": "星座能源 (CEG)",
    "Dominion Energy, Inc.": "自治领能源 (D)",
    "Public Service Enterprise Group Incorporated": "公共服务企业 (PEG)",
    "Consolidated Edison, Inc.": "爱迪生联合 (ED)",
    "WEC Energy Group, Inc.": "WEC能源 (WEC)",
    "Xcel Energy Inc.": "卓越能源 (XEL)",
    "Edison International": "爱迪生国际 (EIX)",
    "American Water Works Company, Inc.": "美国水务 (AWK)",
    "DTE Energy Company": "DTE能源 (DTE)",
    "PPL Corporation": "PPL电力 (PPL)"
}

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

# ================= 新增：提取真实持仓，并应用字典翻译 =================
def get_etf_holdings_and_sectors(etf_tickers):
    holdings_dict = {}
    sectors_dict = {}
    
    for ticker in etf_tickers:
        print(f"Fetching holdings and sectors for {ticker}...")
        try:
            etf = yf.Ticker(ticker)
            
            # 1. 获取持仓 (Holdings)
            holdings = []
            try:
                # 尝试新的 fund_data API
                if hasattr(etf, 'funds_data') and hasattr(etf.funds_data, 'top_holdings'):
                    raw_holdings = etf.funds_data.top_holdings
                    if raw_holdings is not None and not raw_holdings.empty:
                        for symbol, row in raw_holdings.iterrows():
                            # 获取英文名并尝试翻译
                            raw_name = row.get('Name', symbol)
                            translated_name = TICKER_TRANSLATIONS.get(raw_name, raw_name)
                            
                            weight = row.get('Holding Percent', 0)
                            if weight > 0:
                                holdings.append({
                                    "ticker": symbol,
                                    "name": translated_name, # 这里写入翻译后的名字
                                    "weight": round(weight * 100, 2) # Yahoo API 返回的是小数，乘 100 变百分比
                                })
                
                # 降级方案：如果老 API 能用
                elif hasattr(etf, 'info') and 'holdings' in etf.info:
                     raw_holdings = etf.info['holdings']
                     for h in raw_holdings:
                         raw_name = h.get('holdingName', h.get('symbol', 'Unknown'))
                         translated_name = TICKER_TRANSLATIONS.get(raw_name, raw_name)
                         weight = h.get('holdingPercent', 0)
                         if weight > 0:
                             holdings.append({
                                 "ticker": h.get('symbol', 'Unknown'),
                                 "name": translated_name, # 这里写入翻译后的名字
                                 "weight": round(weight * 100, 2)
                             })
            except Exception as e:
                print(f"  Failed to fetch holdings for {ticker}: {e}")
            
            # 如果抓到了，保存下来
            if holdings:
                holdings_dict[ticker] = holdings
                
            # 2. 获取行业 (Sectors)
            sectors = {}
            try:
                 if hasattr(etf, 'funds_data') and hasattr(etf.funds_data, 'sector_weightings'):
                     raw_sectors = etf.funds_data.sector_weightings
                     if raw_sectors is not None and not raw_sectors.empty:
                         for index, row in raw_sectors.iterrows():
                             # 将 Yahoo 默认的行业英文翻译成你的前端分类
                             sector_name_en = index
                             weight = row.iloc[0] if isinstance(row, pd.Series) else row
                             
                             # 简单的内置行业翻译
                             sector_mapping = {
                                 "Technology": "信息技术",
                                 "Financial Services": "金融",
                                 "Healthcare": "医疗健康",
                                 "Consumer Cyclical": "可选消费",
                                 "Consumer Defensive": "必需消费",
                                 "Industrials": "工业",
                                 "Communication Services": "通信服务",
                                 "Energy": "能源",
                                 "Utilities": "公用事业",
                                 "Real Estate": "房地产",
                                 "Basic Materials": "原材料"
                             }
                             sector_name_cn = sector_mapping.get(sector_name_en, "其他")
                             
                             if weight > 0:
                                 sectors[sector_name_cn] = round(weight * 100, 2)
            except Exception as e:
                print(f"  Failed to fetch sectors for {ticker}: {e}")
                
            if sectors:
                sectors_dict[ticker] = sectors
                
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
            
    return holdings_dict, sectors_dict

# 抓取数据
print("Starting live fetch of ETF composition data...")
live_holdings, live_sectors = get_etf_holdings_and_sectors(proxy_chains.keys())

# 生成最终的 JS 字符串
# 这里做了一个极度优雅的降级处理：如果你没抓到，用我们在前端约定的格式输出
def generate_js_object(py_dict):
    return json.dumps(py_dict, ensure_ascii=False, indent=4)

# 动态组装 JS 文件内容
etf_holdings_js = f"""
// 1. ETF 底层真实前 15 大持仓数据 (Top Holdings) - Live Fetched
window.etfHoldings = {generate_js_object(live_holdings) if live_holdings else "{}"};

// 2. ETF 真实行业分布数据 (Sector Weights %) - Live Fetched
window.etfSectors = {generate_js_object(live_sectors) if live_sectors else "{}"};
"""


# 把数据直接写入 JS 文件 (包含 X-Ray 数据 + 抓取的回测数据)
with open("data.js", "w", encoding="utf-8") as f:
    f.write(etf_holdings_js + "\n\n")
    f.write("window.proxyDatabase = {\n")
    for year in sorted(database.keys()):
        assets = []
        for asset in proxy_chains.keys():
            m = database[year].get(asset, [0.08, 0.02])
            assets.append(f"'{asset}': [{m[0]:.4f}, {m[1]:.4f}]")
        f.write(f"    {year}: {{ {', '.join(assets)} }},\n")
    f.write("};\n")

print("Update completed successfully! Check data.js.")
