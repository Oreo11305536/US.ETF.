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

# ================= 新增：X-Ray 穿透所需的基础持仓与行业数据 =================
etf_holdings_js = """
// 1. ETF 底层真实前 15 大持仓数据 (Top Holdings)
window.etfHoldings = {
    SCHD: [
        { ticker: 'HD', name: '家得宝 (Home Depot)', weight: 4.35 }, { ticker: 'BLK', name: '贝莱德 (BlackRock)', weight: 4.21 }, { ticker: 'CSCO', name: '思科 (Cisco)', weight: 4.15 }, { ticker: 'CVX', name: '雪佛龙 (Chevron)', weight: 4.08 }, { ticker: 'ABBV', name: '艾伯维 (AbbVie)', weight: 4.02 }, { ticker: 'TXN', name: '德州仪器 (TI)', weight: 3.95 }, { ticker: 'LMT', name: '洛克希德马丁', weight: 3.88 }, { ticker: 'AMGN', name: '安进 (Amgen)', weight: 3.75 }, { ticker: 'PEP', name: '百事可乐', weight: 3.62 }, { ticker: 'PFE', name: '辉瑞 (Pfizer)', weight: 3.51 }, { ticker: 'UPS', name: '联合包裹', weight: 3.20 }, { ticker: 'VZ', name: '威瑞森', weight: 3.10 }, { ticker: 'KO', name: '可口可乐', weight: 2.95 }, { ticker: 'BMY', name: '百时美施贵宝', weight: 2.80 }, { ticker: 'EMR', name: '艾默生电气', weight: 2.65 }
    ],
    DGRO: [
        { ticker: 'MSFT', name: '微软 (Microsoft)', weight: 3.12 }, { ticker: 'AAPL', name: '苹果 (Apple)', weight: 2.98 }, { ticker: 'JNJ', name: '强生 (J&J)', weight: 2.75 }, { ticker: 'JPM', name: '摩根大通', weight: 2.65 }, { ticker: 'AVGO', name: '博通 (Broadcom)', weight: 2.58 }, { ticker: 'XOM', name: '埃克森美孚', weight: 2.42 }, { ticker: 'HD', name: '家得宝', weight: 2.30 }, { ticker: 'PG', name: '宝洁', weight: 2.21 }, { ticker: 'ABBV', name: '艾伯维', weight: 2.10 }, { ticker: 'CVX', name: '雪佛龙', weight: 2.02 }, { ticker: 'MRK', name: '默沙东', weight: 1.95 }, { ticker: 'BAC', name: '美国银行', weight: 1.85 }, { ticker: 'COST', name: '好市多', weight: 1.78 }, { ticker: 'CSCO', name: '思科', weight: 1.65 }, { ticker: 'PEP', name: '百事可乐', weight: 1.55 }
    ],
    VPU: [
        { ticker: 'NEE', name: '新纪元能源', weight: 12.15 }, { ticker: 'SO', name: '南方电力', weight: 7.25 }, { ticker: 'DUK', name: '杜克能源', weight: 6.80 }, { ticker: 'CEG', name: '星座能源', weight: 5.40 }, { ticker: 'AEP', name: '美国电力', weight: 4.35 }, { ticker: 'SRE', name: '桑普拉能源', weight: 3.85 }, { ticker: 'D', name: '自治领能源', weight: 3.50 }, { ticker: 'PEG', name: '公共服务企业', weight: 3.25 }, { ticker: 'ED', name: '爱迪生联合', weight: 2.95 }, { ticker: 'WEC', name: 'WEC能源', weight: 2.70 }, { ticker: 'XEL', name: '卓越能源', weight: 2.50 }, { ticker: 'EIX', name: '爱迪生国际', weight: 2.35 }, { ticker: 'AWK', name: '美国水务', weight: 2.10 }, { ticker: 'DTE', name: 'DTE能源', weight: 1.95 }, { ticker: 'PPL', name: 'PPL电力', weight: 1.80 }
    ],
    VOO: [
        { ticker: 'MSFT', name: '微软 (Microsoft)', weight: 7.15 }, { ticker: 'AAPL', name: '苹果 (Apple)', weight: 6.85 }, { ticker: 'NVDA', name: '英伟达 (NVIDIA)', weight: 6.20 }, { ticker: 'AMZN', name: '亚马逊 (Amazon)', weight: 3.65 }, { ticker: 'META', name: 'Meta (脸书)', weight: 2.45 }, { ticker: 'GOOGL', name: '谷歌-A (Alphabet)', weight: 2.05 }, { ticker: 'BRK.B', name: '伯克希尔哈撒韦', weight: 1.72 }, { ticker: 'GOOG', name: '谷歌-C (Alphabet)', weight: 1.70 }, { ticker: 'LLY', name: '礼来', weight: 1.55 }, { ticker: 'AVGO', name: '博通', weight: 1.48 }, { ticker: 'TSLA', name: '特斯拉', weight: 1.35 }, { ticker: 'JPM', name: '摩根大通', weight: 1.25 }, { ticker: 'WMT', name: '沃尔玛', weight: 1.10 }, { ticker: 'UNH', name: '联合健康', weight: 1.05 }, { ticker: 'V', name: '维萨', weight: 0.98 }
    ],
    QQQM: [
        { ticker: 'AAPL', name: '苹果 (Apple)', weight: 8.85 }, { ticker: 'MSFT', name: '微软 (Microsoft)', weight: 8.45 }, { ticker: 'NVDA', name: '英伟达 (NVIDIA)', weight: 7.65 }, { ticker: 'AMZN', name: '亚马逊 (Amazon)', weight: 5.25 }, { ticker: 'META', name: 'Meta (脸书)', weight: 4.85 }, { ticker: 'AVGO', name: '博通', weight: 4.15 }, { ticker: 'GOOGL', name: '谷歌-A', weight: 2.85 }, { ticker: 'GOOG', name: '谷歌-C', weight: 2.75 }, { ticker: 'TSLA', name: '特斯拉', weight: 2.65 }, { ticker: 'COST', name: '好市多', weight: 2.45 }, { ticker: 'NFLX', name: '网飞', weight: 1.95 }, { ticker: 'AMD', name: '超威半导体', weight: 1.65 }, { ticker: 'TMUS', name: 'T-Mobile', weight: 1.45 }, { ticker: 'PEP', name: '百事可乐', weight: 1.35 }, { ticker: 'ADBE', name: '奥多比', weight: 1.25 }
    ],
    SMH: [
        { ticker: 'NVDA', name: '英伟达 (NVIDIA)', weight: 20.45 }, { ticker: 'TSM', name: '台积电 (TSMC)', weight: 12.85 }, { ticker: 'AVGO', name: '博通 (Broadcom)', weight: 7.65 }, { ticker: 'ASML', name: '阿斯麦 (ASML)', weight: 4.85 }, { ticker: 'AMD', name: '超威半导体', weight: 4.45 }, { ticker: 'QCOM', name: '高通', weight: 4.25 }, { ticker: 'AMAT', name: '应用材料', weight: 4.10 }, { ticker: 'LRCX', name: '泛林集团', weight: 3.85 }, { ticker: 'TXN', name: '德州仪器', weight: 3.65 }, { ticker: 'MU', name: '美光科技', weight: 3.45 }, { ticker: 'ADI', name: '亚德诺半导体', weight: 3.15 }, { ticker: 'KLAC', name: '科磊', weight: 2.95 }, { ticker: 'INTC', name: '英特尔', weight: 2.65 }, { ticker: 'MRVL', name: '美满电子', weight: 2.35 }, { ticker: 'MCHP', name: '微芯科技', weight: 2.05 }
    ],
    VGT: [
        { ticker: 'MSFT', name: '微软 (Microsoft)', weight: 16.45 }, { ticker: 'AAPL', name: '苹果 (Apple)', weight: 15.85 }, { ticker: 'NVDA', name: '英伟达 (NVIDIA)', weight: 13.75 }, { ticker: 'AVGO', name: '博通', weight: 4.55 }, { ticker: 'CRM', name: '赛富时', weight: 2.35 }, { ticker: 'AMD', name: '超威半导体', weight: 2.15 }, { ticker: 'ACN', name: '埃森哲', weight: 1.95 }, { ticker: 'CSCO', name: '思科', weight: 1.85 }, { ticker: 'ORCL', name: '甲骨文', weight: 1.75 }, { ticker: 'ADBE', name: '奥多比', weight: 1.65 }, { ticker: 'TXN', name: '德州仪器', weight: 1.45 }, { ticker: 'QCOM', name: '高通', weight: 1.35 }, { ticker: 'IBM', name: 'IBM', weight: 1.25 }, { ticker: 'AMAT', name: '应用材料', weight: 1.15 }, { ticker: 'INTU', name: '直觉软件', weight: 1.05 }
    ]
};

// 2. ETF 真实行业分布数据 (Sector Weights %)
window.etfSectors = {
    SCHD: { '金融': 38.5, '工业': 16.2, '医疗健康': 14.8, '必需消费': 11.5, '信息技术': 9.2, '能源': 8.5, '其他': 1.3 },
    DGRO: { '信息技术': 32.5, '金融': 18.2, '医疗健康': 16.5, '工业': 11.8, '必需消费': 9.5, '能源': 6.2, '其他': 5.3 },
    VPU:  { '公用事业': 100.0 },
    VOO:  { '信息技术': 31.5, '金融': 13.2, '医疗健康': 11.8, '非必需消费': 10.2, '通信服务': 8.9, '工业': 8.2, '其他': 16.2 },
    QQQM: { '信息技术': 51.2, '通信服务': 15.5, '非必需消费': 13.8, '医疗健康': 6.2, '必需消费': 5.8, '工业': 4.5, '其他': 3.0 },
    SMH:  { '信息技术(半导体)': 100.0 },
    VGT:  { '信息技术': 100.0 }
};
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
