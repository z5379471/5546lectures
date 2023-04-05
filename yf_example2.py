""" yf_example2.py
Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf
import os

def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file
    Parameters
    ----------
    tic : str
        Ticker
    pth : str
        Location of the output CSV file
    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'
    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

yf_prc_to_csv('QAN.AX','qan_stk_prc.csv')
