import yfinance as yf
import pandas as pd
from datetime import datetime
import json

# ================= 1. 股票名称中文翻译字典 =================
# 统一转换为小写进行键匹配，确保绝对不会漏掉
TICKER_TRANSLATIONS = {
    "apple inc.": "苹果 (AAPL)",
    "apple": "苹果 (AAPL)",
    "microsoft corporation": "微软 (MSFT)",
    "microsoft": "微软 (MSFT)",
    "nvidia corporation": "英伟达 (NVDA)",
    "nvidia": "英伟达 (NVDA)",
    "amazon.com, inc.": "亚马逊 (AMZN)",
    "amazon": "亚马逊 (AMZN)",
    "meta platforms, inc.": "Meta (META)",
    "meta": "Meta (META)",
    "tesla, inc.": "特斯拉 (TSLA)",
    "tesla": "特斯拉 (TSLA)",
    "broadcom inc.": "博通 (AVGO)",
    "broadcom": "博通 (AVGO)",
    "the home depot, inc.": "家得宝 (HD)",
    "home depot": "家得宝 (HD)",
    "abbvie inc.": "艾伯维 (ABBV)",
    "abbvie": "艾伯维 (ABBV)",
    "texas instruments incorporated": "德州仪器 (TXN)",
    "texas instruments": "德州仪器 (TXN)",
    "chevron corporation": "雪佛龙 (CVX)",
    "chevron": "雪佛龙 (CVX)",
    "exxon mobil corporation": "埃克森美孚 (XOM)",
    "exxon mobil": "埃克森美孚 (XOM)",
    "jPMorgan chase & co.": "摩根大通 (JPM)",
    "jpmorgan": "摩根大通 (JPM)",
    "johnson & johnson": "强生 (JNJ)",
    "taiwan semiconductor manufacturing company limited": "台积电 (TSM)",
    "tsmc": "台积电 (TSM)",
    "asml holding n.v.": "阿斯麦 (ASML)",
    "asml": "阿斯麦 (ASML)",
    "advanced micro devices, inc.": "超威半导体 (AMD)",
    "amd": "超威半导体 (AMD)",
    "salesforce, inc.": "赛富时 (CRM)",
    "salesforce": "赛富时 (CRM)",
    "nextera energy, inc.": "新纪元能源 (NEE)",
    "nextera energy": "新纪元能源 (NEE)",
    "the southern company": "南方电力 (SO)",
    "southern co": "南方电力 (SO)",
    "duke energy corporation": "杜克能源 (DUK)",
    "duke energy": "杜克能源 (DUK)",
    "sempra": "桑普拉能源 (SRE)",
    "american electric power company, inc.": "美国电力 (AEP)",
    "aep": "美国电力 (AEP)",
    "berkshire hathaway inc.": "伯克希尔 (BRK.B)",
    "alphabet inc.": "谷歌 (GOOGL)",
    "eli lilly and company": "礼来 (LLY)",
    "walmart inc.": "沃尔玛 (WMT)",
    "unitedhealth group incorporated": "联合健康 (UNH)",
    "visa inc.": "维萨 (V)",
    "costco wholesale corporation": "好市多 (COST)",
    "netflix, inc.": "网飞 (NFLX)",
    "pepsico, inc.": "百事可乐 (PEP)",
    "adobe inc.": "奥多比 (ADBE)",
    "cisco systems, inc.": "思科 (CSCO)",
    "qualcomm incorporated": "高通 (QCOM)",
    "applied materials, inc.": "应用材料 (AMAT)",
    "lam research corporation": "泛林集团 (LRCX)",
    "micron technology, inc.": "美光科技 (MU)",
    "analog devices, inc.": "亚德诺半导体 (ADI)",
    "kla corporation": "科磊 (KLAC)",
    "intel corporation": "英特尔 (INTC)",
    "marvell technology, inc.": "美满电子 (MRVL)",
    "microchip technology incorporated": "微芯科技 (MCHP)",
    "accenture plc": "埃森哲 (ACN)",
    "oracle corporation": "甲骨文 (ORCL)",
    "international business machines corporation": "IBM (IBM)",
    "intuit inc.": "直觉软件 (INTU)",
    "blackrock, inc.": "贝莱德 (BLK)",
    "lockheed martin corporation": "洛克希德马丁 (LMT)",
    "amgen inc.": "安进 (AMGN)",
    "pfizer inc.": "辉瑞 (PFE)",
    "united parcel service, inc.": "联合包裹 (UPS)",
    "verizon communications inc.": "威瑞森 (VZ)",
    "the coca-cola company": "可口可乐 (KO)",
    "bristol-myers squibb company": "百时美施贵宝 (BMY)",
    "emerson electric co.": "艾默生电气 (EMR)",
    "merck & co., inc.": "默沙东 (MRK)",
    "bank of america corporation": "美国银行 (BAC)",
    "constellation energy corporation": "星座能源 (CEG)",
    "dominion energy, inc.": "自治领能源 (D)",
    "public service enterprise group incorporated": "公共服务企业 (PEG)",
    "consolidated edison, inc.": "爱迪生联合 (ED)",
    "wec energy group, inc.": "WEC能源 (WEC)",
    "xcel energy inc.": "卓越能源 (XEL)",
    "edison international": "爱迪生国际 (EIX)",
    "american water works company, inc.": "美国水务 (AWK)",
    "dte energy company": "DTE能源 (DTE)",
    "ppl corporation": "PPL电力 (PPL)"
}

def smart_translate(raw_name, symbol):
    """智能翻译函数：去除前后空格、转小写并在字典中匹配，若无匹配则降级显示原名+代码"""
    if not raw_name:
        return symbol
    cleaned_key = str(raw_name).strip().lower()
    # 如果在字典中找到，返回翻译后的名称；否则组装一个默认的格式并返回
    if cleaned_key in TICKER_TRANSLATIONS:
        return TICKER_TRANSLATIONS[cleaned_key]
    return f"{raw_name} ({symbol})"

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

# ================= 2. 抓取真实持仓并应用智能翻译 =================
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
                if hasattr(etf, 'funds_data') and hasattr(etf.funds_data, 'top_holdings'):
                    raw_holdings = etf.funds_data.top_holdings
                    if raw_holdings is not None and not raw_holdings.empty:
                        for symbol, row in raw_holdings.iterrows():
                            raw_name = row.get('Name', symbol)
                            # 使用智能翻译函数拦截英文名
                            translated_name = smart_translate(raw_name, symbol)
                            
                            weight = row.get('Holding Percent', 0)
                            if weight > 0:
                                holdings.append({
                                    "ticker": symbol,
                                    "name": translated_name,
                                    "weight": round(weight * 100, 2)
                                })
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

print("Starting live fetch of ETF composition data...")
live_holdings, live_sectors = get_etf_holdings_and_sectors(proxy_chains.keys())

def generate_js_object(py_dict):
    return json.dumps(py_dict, ensure_ascii=False, indent=4)

# 动态组装 data.js 内容
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
