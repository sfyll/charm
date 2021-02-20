#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import deribit_data as dm
import pandas as pd

def arb(bidCharm, askCharm, bidDeribit, askDeribit, strike):
    sellDeribit = bidDeribit-bidCharm
    buyDeribit = (1-askCharm)-askDeribit
    if sellDeribit > buyDeribit:
        return pd.Series([sellDeribit, sellDeribit/bidDeribit+bidCharm, 'SellDeribit'])
    else:
        return pd.Series([buyDeribit, buyDeribit/(1-askCharm)-askDeribit, 'buyDeribit'])


def dashBoard(CharmDataExcel, priceDeribitBtc, priceDeribitETH):
    priceCharm = pd.read_excel(CharmDataExcel, sheet_name = 'Input', engine='openpyxl')
    priceDeribit = pd.read_csv(priceDeribitBtc)
    priceEth = pd.read_csv(priceDeribitETH)
    priceDeribit = priceDeribit.append(priceEth)
    
    temp = priceDeribit[priceDeribit['instrument_name'].isin( priceCharm['Instrument'].values)][['instrument_name', 'best_bid_price', 'best_ask_price']]
    
    mergedPrice = (pd.merge(left=priceCharm, right=temp, left_on='Instrument', right_on='instrument_name')).drop(columns='instrument_name')
    
    mergedPrice[['Arb', 'percentReturns', 'direction']] = mergedPrice.apply(lambda row: arb(row['callPrice'], row['shortPrice'], row['best_bid_price'], row['best_ask_price'], row['strike']), axis = 1)

    return mergedPrice
