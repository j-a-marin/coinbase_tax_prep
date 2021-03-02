import yfinance as yf
import numpy as np
import pandas as pd
import tabula, pickle

btc_2015 = yf.download("BTC-USD", start="2015-01-01", end="2015-12-31")
btc_2016 = yf.download("BTC-USD", start="2016-01-01", end="2016-12-31")
btc_2017 = yf.download("BTC-USD", start="2017-01-01", end="2017-12-31")
btc_2018 = yf.download("BTC-USD", start="2018-01-01", end="2018-12-31")

btc_years = ["btc_" + str(y) for y in range(2015, 2019)]

for year in zip(range(2015, 2019), btc_years):
    if year[0] == 2015:
        print('\n')
    yearly_close = np.round(np.mean(locals()[year[1]].Close), 2)
    print("Year", year[0], f"BTC average ${yearly_close:,}")

sale_date = np.round(btc_2018.loc['2018-01-18', 'Close'], 2)

print("\n", "BTC Price on sale date Jan 18, 2018 was", f"${sale_date:,}")

eth_2015 = yf.download("ETH-USD", start="2015-01-01", end="2015-12-31")
eth_2016 = yf.download("ETH-USD", start="2016-01-01", end="2016-12-31")
eth_2017 = yf.download("ETH-USD", start="2017-01-01", end="2017-12-31")
eth_2018 = yf.download("ETH-USD", start="2018-01-01", end="2018-12-31")

eth_years = ["eth_" + str(y) for y in range(2015, 2019)]

for year in zip(range(2015, 2019), eth_years):
    if year[0] == 2015:
        print('\n')
    yearly_close = np.round(np.mean(locals()[year[1]].Close), 2)
    print("Year", year[0], f"ETH average ${yearly_close:,}")

eos_2017 = yf.download("EOS-USD", start="2017-01-01", end="2017-12-31")
eos_2018 = yf.download("EOS-USD", start="2018-01-01", end="2018-12-31")

eos_years = ["eos_" + str(y) for y in range(2017, 2019)]

for year in zip(range(2017, 2019), eos_years):
    if year[0] == 2017:
        print('\n')
    yearly_close = np.round(np.mean(locals()[year[1]].Close), 2)
    print("Year", year[0], f"EOS average ${yearly_close:,}")

bch_2017 = yf.download("BCH-USD", start="2017-01-01", end="2017-12-31")
bch_2018 = yf.download("BCH-USD", start="2018-01-01", end="2018-12-31")

bch_years = ["bch_" + str(y) for y in range(2017, 2019)]

for year in zip(range(2017, 2019), bch_years):
    if year[0] == 2017:
        print('\n')
    yearly_close = np.round(np.mean(locals()[year[1]].Close), 2)
    print("Year", year[0], f"BCH average ${yearly_close:,}")

ltc_2016 = yf.download("LTC-USD", start="2016-01-01", end="2016-12-31")
ltc_2017 = yf.download("LTC-USD", start="2017-01-01", end="2017-12-31")
ltc_2018 = yf.download("LTC-USD", start="2018-01-01", end="2018-12-31")

ltc_years = ["ltc_" + str(y) for y in range(2016, 2019)]

for year in zip(range(2016, 2019), ltc_years):
    if year[0] == 2016:
        print('\n')
    yearly_close = np.round(np.mean(locals()[year[1]].Close), 2)
    print("Year", year[0], f"LTC average ${yearly_close:,}")

#
# gdax_ledger_1 = tabula.read_pdf('/Users/jam3/Downloads/account.pdf', pages='1')
# output = open('gdax_ledger_1.pkl', 'wb')
# pickle.dump(gdax_ledger_1, output)
#
# gdax_ledger_2 = tabula.read_pdf('/Users/jam3/Downloads/account.pdf', pages='2')
# output = open('gdax_ledger_2.pkl', 'wb')
# pickle.dump(gdax_ledger_2, output)
#
# coinbase_ledger = tabula.read_pdf('/Users/jam3/Downloads/Coinbase_Ledger_.pdf', pages='all')
# output = open('coinbase_ledger.pkl', 'wb')
# pickle.dump(coinbase_ledger, output)

