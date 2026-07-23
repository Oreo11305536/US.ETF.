import yfinance as yf
import pandas as pd
from datetime import datetime
import json

# ================= 1. 股票名称中文翻译字典 =================
# 核心优化：放弃用冗长的英文全称匹配，直接采用唯一的股票代码(Ticker)作为Key。
# 这能 100% 避免因雅虎财经API变动（如增删 Inc. 或 Corp. 后缀）导致的匹配失败。
TICKER_TRANSLATIONS = {
    "AAPL": "苹果 (AAPL)",
    "MSFT": "微软 (MSFT)",
    "NVDA": "英伟达 (NVDA)",
    "AMZN": "亚马逊 (AMZN)",
    "META": "Meta (META)",
    "TSLA": "特斯拉 (TSLA)",
    "AVGO": "博通 (AVGO)",
    "HD": "家得宝 (HD)",
    "ABBV": "艾伯维 (ABBV)",
    "TXN": "德州仪器 (TXN)",
    "CVX": "雪佛龙 (CVX)",
    "XOM": "埃克森美孚 (XOM)",
    "JPM": "摩根大通 (JPM)",
    "JNJ": "强生 (JNJ)",
    "TSM": "台积电 (TSM)",
    "ASML": "阿斯麦 (ASML)",
    "AMD": "超威半导体 (AMD)",
    "CRM": "赛富时 (CRM)",
    "NEE": "新纪元能源 (NEE)",
    "SO": "南方电力 (SO)",
    "DUK": "杜克能源 (DUK)",
    "SRE": "桑普拉能源 (SRE)",
    "AEP": "美国电力 (AEP)",
    "BRK.B": "伯克希尔 (BRK.B)",
    "BRK-B": "伯克希尔 (BRK.B)",
    "GOOGL": "谷歌 (GOOGL)",
    "GOOG": "谷歌 (GOOG)",
    "LLY": "礼来 (LLY)",
    "WMT": "沃尔玛 (WMT)",
    "UNH": "联合健康 (UNH)",
    "V": "维萨 (V)",
    "COST": "好市多 (COST)",
    "NFLX": "网飞 (NFLX)",
    "PEP": "百事可乐 (PEP)",
    "ADBE": "奥多比 (ADBE)",
    "CSCO": "思科 (CSCO)",
    "QCOM": "高通 (QCOM)",
    "AMAT": "应用材料 (AMAT)",
    "LRCX": "泛林集团 (LRCX)",
    "MU": "美光科技 (MU)",
    "ADI": "亚德诺半导体 (ADI)",
    "KLAC": "科磊 (KLAC)",
    "INTC": "英特尔 (INTC)",
    "MRVL": "美满电子 (MRVL)",
    "MCHP": "微芯科技 (MCHP)",
    "ACN": "埃森哲 (ACN)",
    "ORCL": "甲骨文 (ORCL)",
    "IBM": "IBM (IBM)",
    "INTU": "直觉软件 (INTU)",
    "BLK": "贝莱德 (BLK)",
    "LMT": "洛克希德马丁 (LMT)",
    "AMGN": "安进 (AMGN)",
    "PFE": "辉瑞 (PFE)",
    "UPS": "联合包裹 (UPS)",
    "VZ": "威瑞森 (VZ)",
    "KO": "可口可乐 (KO)",
    "BMY": "百时美施贵宝 (BMY)",
    "EMR": "艾默生电气 (EMR)",
    "MRK": "默沙东 (MRK)",
    "BAC": "美国银行 (BAC)",
    "CEG": "星座能源 (CEG)",
    "D": "自治领能源 (D)",
    "PEG": "公共服务企业 (PEG)",
    "ED": "爱迪生联合 (ED)",
    "WEC": "WEC能源 (WEC)",
    "XEL": "卓越能源 (XEL)",
    "EIX": "爱迪生国际 (EIX)",
    "AWK": "美国水务 (AWK)",
    "DTE": "DTE能源 (DTE)",
    "PPL": "PPL电力 (PPL)",
    "PG": "宝洁 (PG)",
    "MA": "万事达 (MA)",
    "MCD": "麦当劳 (MCD)",
    "DIS": "迪士尼 (DIS)",
    "ABT": "雅培 (ABT)",
    "DHR": "丹纳赫 (DHR)",
    "TMO": "赛默飞世尔 (TMO)",
    "NKE": "耐克 (NKE)",
    "LIN": "林德 (LIN)",
    "PM": "菲利普莫里斯 (PM)",
    "BA": "波音 (BA)",
    "RTX": "雷神 (RTX)"
}

def smart_translate(raw_name, symbol):
    """智能翻译函数：根据股票代码精准匹配，若无匹配则降级显示 原名 (代码)"""
    if not symbol or str(symbol).strip() == "" or str(symbol).strip().lower() == "unknown":
        return str(raw_name).strip()
        
    clean_symbol = str(symbol).strip().upper()
    
    # 1. 优先尝试直接用代码(Ticker)进行匹配翻译
    if clean_symbol in TICKER_TRANSLATIONS:
        return TICKER_TRANSLATIONS[clean_symbol]
        
    # 2. 如果字典里没收录这只股票，兜底拼装成 "原英文名 (股票代码)"
    clean_name = str(raw_name).strip()
    
    # 避免拼装出 "Apple (AAPL) (AAPL)" 这种叠词情况
    if f"({clean_symbol})" in clean_name:
        return clean_name
        
    return f"{clean_name} ({clean_symbol})"

# ================= 3. 回测数据代理链与抓取引擎 =================
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

# ================= 4. 抓取真实持仓并应用智能翻译 =================
def get_etf_holdings_and_sectors(etf_tickers):
    holdings_dict = {}
    sectors_dict = {}
    
    for ticker in etf_tickers:
        print(f"Fetching holdings and sectors for {ticker}...")
        try:
            etf = yf.Ticker(ticker)
            
            # 获取持仓
            holdings = []
            try:
                # 新版 yfinance 取法
                if hasattr(etf, 'funds_data') and hasattr(etf.funds_data, 'top_holdings'):
                    raw_holdings = etf.funds_data.top_holdings
                    if raw_holdings is not None and not raw_holdings.empty:
                        for symbol, row in raw_holdings.iterrows():
                            raw_name = row.get('Name', symbol)
                            # 使用智能翻译函数，传入原名和代码
                            translated_name = smart_translate(raw_name, symbol)
                            
                            weight = row.get('Holding Percent', 0)
                            if weight > 0:
                                holdings.append({
                                    "ticker": symbol,
                                    "name": translated_name,
                                    "weight": round(weight * 100, 2)
                                })
                # 兼容旧版 yfinance 取法
                elif hasattr(etf, 'info') and 'holdings' in etf.info:
                     raw_holdings = etf.info['holdings']
                     for h in raw_holdings:
                         symbol = h.get('symbol', 'Unknown')
                         raw_name = h.get('holdingName', symbol)
                         translated_name = smart_translate(raw_name, symbol)
                         
                         weight = h.get('holdingPercent', 0)
                         if weight > 0:
                             holdings.append({
                                 "ticker": symbol,
                                 "name": translated_name,
                                 "weight": round(weight * 100, 2)
                             })
            except Exception as e:
                print(f"  Failed to fetch holdings for {ticker}: {e}")
            
            if holdings:
                holdings_dict[ticker] = holdings
                
            # 获取行业
            sectors = {}
            try:
                 if hasattr(etf, 'funds_data') and hasattr(etf.funds_data, 'sector_weightings'):
                     raw_sectors = etf.funds_data.sector_weightings
                     if raw_sectors is not None and not raw_sectors.empty:
                         for index, row in raw_sectors.iterrows():
                             sector_name_en = index
                             weight = row.iloc[0] if isinstance(row, pd.Series) else row
                             
                             sector_mapping = {
                                 "Technology": "信息技术",
                                 "Financial Services": "金融",
                                 "Healthcare": "医疗保健",
                                 "Consumer Cyclical": "可选消费",
                                 "Consumer Defensive": "必选消费",
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

print("Starting live fetch of ETF composition data...")
live_holdings, live_sectors = get_etf_holdings_and_sectors(proxy_chains.keys())

def generate_js_object(py_dict):
    return json.dumps(py_dict, ensure_ascii=False, indent=4)

# ================= 5. 生成 data.js =================
etf_holdings_js = f"""
window.etfHoldings = {generate_js_object(live_holdings) if live_holdings else "{}"};
window.etfSectors = {generate_js_object(live_sectors) if live_sectors else "{}"};
"""

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
