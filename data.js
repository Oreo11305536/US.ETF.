
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


window.proxyDatabase = {
    1993: { 'SCHD': [0.1461, 0.6433], 'DGRO': [0.1506, 0.5095], 'VPU': [0.1160, 0.4226], 'VOO': [0.0800, 0.0200], 'QQQM': [0.1058, 0.0020], 'SMH': [0.3211, 1.6195], 'VGT': [0.2867, 0.9653] },
    1994: { 'SCHD': [-0.0158, 0.3328], 'DGRO': [-0.0855, 0.3275], 'VPU': [-0.1158, 0.3479], 'VOO': [0.0040, 0.0468], 'QQQM': [0.0150, 0.0020], 'SMH': [0.1717, 0.0000], 'VGT': [0.1114, 0.2938] },
    1995: { 'SCHD': [0.3737, 0.3886], 'DGRO': [0.3404, 0.2824], 'VPU': [0.3066, 0.4416], 'VOO': [0.3805, 0.0486], 'QQQM': [0.4254, 0.0020], 'SMH': [0.6882, 1.9974], 'VGT': [0.4387, 1.4188] },
    1996: { 'SCHD': [0.1734, 0.4482], 'DGRO': [0.0528, 0.2182], 'VPU': [0.0200, 0.5393], 'VOO': [0.2250, 0.0373], 'QQQM': [0.4254, 0.0020], 'SMH': [0.4172, 0.0000], 'VGT': [0.1559, 0.4508] },
    1997: { 'SCHD': [0.3116, 0.4884], 'DGRO': [0.2509, 0.3074], 'VPU': [0.2495, 0.4370], 'VOO': [0.3348, 0.0309], 'QQQM': [0.2063, 0.0020], 'SMH': [0.1398, 1.6219], 'VGT': [0.1021, 1.6629] },
    1998: { 'SCHD': [0.1734, 0.3509], 'DGRO': [0.2185, 0.4572], 'VPU': [0.0764, 0.3804], 'VOO': [0.2869, 0.0238], 'QQQM': [0.8530, 0.0020], 'SMH': [0.5112, 0.0000], 'VGT': [0.7359, 0.0000] },
    1999: { 'SCHD': [-0.0020, 0.3092], 'DGRO': [-0.0296, 0.4010], 'VPU': [-0.1503, 0.3592], 'VOO': [0.2039, 0.0189], 'QQQM': [1.0195, 0.0020], 'SMH': [1.0646, 0.6112], 'VGT': [0.6514, 0.0000] },
    2000: { 'SCHD': [0.1350, 0.3567], 'DGRO': [0.1884, 0.3045], 'VPU': [0.4162, 0.2262], 'VOO': [-0.0974, 0.0164], 'QQQM': [-0.3611, 0.0000], 'SMH': [-0.1800, 0.8353], 'VGT': [-0.4188, 0.0000] },
    2001: { 'SCHD': [-0.0235, 0.1993], 'DGRO': [-0.1943, 0.1586], 'VPU': [-0.0809, 0.3143], 'VOO': [-0.1176, 0.0171], 'QQQM': [-0.3334, 0.0000], 'SMH': [-0.1459, 0.0000], 'VGT': [-0.2335, 0.0000] },
    2002: { 'SCHD': [-0.1567, 0.0883], 'DGRO': [-0.2378, 0.0782], 'VPU': [-0.1059, 0.1614], 'VOO': [-0.2158, 0.0204], 'QQQM': [-0.3737, 0.0000], 'SMH': [-0.4707, 0.0000], 'VGT': [-0.3817, 0.0023] },
    2003: { 'SCHD': [0.2515, 0.2174], 'DGRO': [0.2920, 0.0629], 'VPU': [0.1935, 0.1735], 'VOO': [0.2818, 0.0284], 'QQQM': [0.4967, 0.0007], 'SMH': [0.8731, 0.0000], 'VGT': [0.3868, 0.0128] },
    2004: { 'SCHD': [0.1354, 0.3079], 'DGRO': [0.1101, 0.0564], 'VPU': [0.2352, 0.1653], 'VOO': [0.1070, 0.0298], 'QQQM': [0.1054, 0.0123], 'SMH': [-0.1957, 0.0000], 'VGT': [0.0564, 0.0273] },
    2005: { 'SCHD': [0.0437, 0.2661], 'DGRO': [0.0422, 0.0554], 'VPU': [0.1456, 0.0655], 'VOO': [0.0483, 0.0263], 'QQQM': [0.0157, 0.0040], 'SMH': [0.0980, 0.0000], 'VGT': [0.0300, 0.0023] },
    2006: { 'SCHD': [0.2063, 0.3129], 'DGRO': [0.0800, 0.0200], 'VPU': [0.2166, 0.0659], 'VOO': [0.1585, 0.0286], 'QQQM': [0.0714, 0.0038], 'SMH': [-0.0816, 0.0000], 'VGT': [0.0885, 0.0033] },
    2007: { 'SCHD': [0.0137, 0.0477], 'DGRO': [0.0563, 0.0240], 'VPU': [0.1699, 0.0541], 'VOO': [0.0515, 0.0273], 'QQQM': [0.1903, 0.0039], 'SMH': [-0.0354, 0.0000], 'VGT': [0.1478, 0.0039] },
    2008: { 'SCHD': [-0.3192, 0.0500], 'DGRO': [-0.2669, 0.0267], 'VPU': [-0.2795, 0.0499], 'VOO': [-0.3679, 0.0261], 'QQQM': [-0.4173, 0.0031], 'SMH': [-0.4575, 0.0000], 'VGT': [-0.4282, 0.0064] },
    2009: { 'SCHD': [0.1719, 0.0595], 'DGRO': [0.1958, 0.0348], 'VPU': [0.1130, 0.0724], 'VOO': [0.2635, 0.0331], 'QQQM': [0.5468, 0.0081], 'SMH': [0.5855, 0.0000], 'VGT': [0.6189, 0.0085] },
    2010: { 'SCHD': [0.1422, 0.0474], 'DGRO': [0.1474, 0.0311], 'VPU': [0.0706, 0.0669], 'VOO': [0.1506, 0.0272], 'QQQM': [0.2014, 0.0113], 'SMH': [0.1651, 0.0000], 'VGT': [0.1278, 0.0076] },
    2011: { 'SCHD': [0.1055, 0.0505], 'DGRO': [0.0616, 0.0303], 'VPU': [0.1899, 0.0654], 'VOO': [0.0190, 0.0271], 'QQQM': [0.0348, 0.0107], 'SMH': [-0.0646, 0.0000], 'VGT': [0.0054, 0.0091] },
    2012: { 'SCHD': [0.1139, 0.0491], 'DGRO': [0.1165, 0.0344], 'VPU': [0.0185, 0.0620], 'VOO': [0.1599, 0.0318], 'QQQM': [0.1811, 0.0167], 'SMH': [0.0855, 0.0271], 'VGT': [0.1396, 0.0155] },
    2013: { 'SCHD': [0.3288, 0.0492], 'DGRO': [0.2887, 0.0303], 'VPU': [0.1491, 0.0636], 'VOO': [0.3239, 0.0300], 'QQQM': [0.3663, 0.0153], 'SMH': [0.3333, 0.0235], 'VGT': [0.3097, 0.0154] },
    2014: { 'SCHD': [0.1168, 0.0428], 'DGRO': [0.1008, 0.0269], 'VPU': [0.2595, 0.0400], 'VOO': [0.1293, 0.0180], 'QQQM': [0.1918, 0.0183], 'SMH': [0.3022, 0.0169], 'VGT': [0.1669, 0.0000] },
    2015: { 'SCHD': [-0.0030, 0.0421], 'DGRO': [-0.0069, 0.0317], 'VPU': [-0.0481, 0.0479], 'VOO': [0.0133, 0.0254], 'QQQM': [0.0944, 0.0116], 'SMH': [-0.0034, 0.0234], 'VGT': [0.0505, 0.0148] },
    2016: { 'SCHD': [0.1645, 0.0463], 'DGRO': [0.1452, 0.0246], 'VPU': [0.1758, 0.0503], 'VOO': [0.1217, 0.0264], 'QQQM': [0.0710, 0.0121], 'SMH': [0.3554, 0.0119], 'VGT': [0.1377, 0.0162] },
    2017: { 'SCHD': [0.2085, 0.0425], 'DGRO': [0.2300, 0.0305], 'VPU': [0.1244, 0.0465], 'VOO': [0.2177, 0.0248], 'QQQM': [0.3266, 0.0117], 'SMH': [0.3848, 0.0212], 'VGT': [0.3708, 0.0145] },
    2018: { 'SCHD': [-0.0556, 0.0376], 'DGRO': [-0.0238, 0.0284], 'VPU': [0.0438, 0.0425], 'VOO': [-0.0450, 0.0221], 'QQQM': [-0.0013, 0.0095], 'SMH': [-0.0905, 0.0180], 'VGT': [0.0246, 0.0141] },
    2019: { 'SCHD': [0.2729, 0.0477], 'DGRO': [0.2987, 0.0335], 'VPU': [0.2489, 0.0431], 'VOO': [0.3136, 0.0272], 'QQQM': [0.3896, 0.0107], 'SMH': [0.6445, 0.0256], 'VGT': [0.4862, 0.0173] },
    2020: { 'SCHD': [0.1503, 0.0441], 'DGRO': [0.0950, 0.0285], 'VPU': [-0.0073, 0.0372], 'VOO': [0.1832, 0.0197], 'QQQM': [0.4841, 0.0066], 'SMH': [0.5553, 0.0110], 'VGT': [0.4604, 0.0125] },
    2021: { 'SCHD': [0.2988, 0.0425], 'DGRO': [0.2665, 0.0271], 'VPU': [0.1740, 0.0364], 'VOO': [0.2879, 0.0171], 'QQQM': [0.2745, 0.0052], 'SMH': [0.4213, 0.0074], 'VGT': [0.3045, 0.0086] },
    2022: { 'SCHD': [-0.0326, 0.0373], 'DGRO': [-0.0791, 0.0233], 'VPU': [0.0106, 0.0336], 'VOO': [-0.1817, 0.0145], 'QQQM': [-0.3252, 0.0058], 'SMH': [-0.3353, 0.0080], 'VGT': [-0.2970, 0.0065] },
    2023: { 'SCHD': [0.0454, 0.0400], 'DGRO': [0.1047, 0.0285], 'VPU': [-0.0745, 0.0347], 'VOO': [0.2632, 0.0190], 'QQQM': [0.5501, 0.0102], 'SMH': [0.7338, 0.0104], 'VGT': [0.5266, 0.0100] },
    2024: { 'SCHD': [0.1166, 0.0430], 'DGRO': [0.1662, 0.0272], 'VPU': [0.2304, 0.0387], 'VOO': [0.2498, 0.0158], 'QQQM': [0.2568, 0.0077], 'SMH': [0.3910, 0.0062], 'VGT': [0.2930, 0.0078] },
    2025: { 'SCHD': [0.0434, 0.0405], 'DGRO': [0.1569, 0.0244], 'VPU': [0.1646, 0.0322], 'VOO': [0.1782, 0.0134], 'QQQM': [0.2085, 0.0060], 'SMH': [0.4917, 0.0046], 'VGT': [0.2177, 0.0049] },
    2026: { 'SCHD': [0.2162, 0.0189], 'DGRO': [0.1172, 0.0096], 'VPU': [0.0636, 0.0141], 'VOO': [0.1035, 0.0062], 'QQQM': [0.1570, 0.0027], 'SMH': [0.6219, 0.0000], 'VGT': [0.2340, 0.0025] },
};
