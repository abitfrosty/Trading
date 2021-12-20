import pandas as pd
import secrets
from string import ascii_letters
from itertools import product


def get_sp500_tickers():
    '''Return pandas Series of SP500 companies
    '''
    url_sp500_list = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    return pd.read_html(url_sp500_list)[0]['Symbol'].sort_values().reset_index(drop=True)


def get_api_url(symbols, types=['quote'], production=False):
    '''Return API URL
    Input:
        symbols (list) - list of tickers
        production (bool) - sandbox/production switch
    Output:
        url (str) - url for quote api
        single quote: stock/A/quote/?token=
        batch quote: stock/market/batch?symbols=aapl,fb,tsla&types=quote&token=
    '''
    base_url = ['sandbox', 'cloud']
    api_url = f'https://{base_url[production]}.iexapis.com/stable/'
    type_url = f'stock/{symbols[0]}/{types[0]}/?'
    if len(symbols) > 1:
        type_url = f'stock/market/batch?symbols={",".join(symbols)}&types={",".join(types)}&'
    token_url = f'token={secrets.IEX_CLOUD_API_TOKEN[production]}'
    url = api_url + type_url + token_url
    return url


def split_into_chunks(lst, n):
    for i in range(0, len(lst), n): 
        yield lst[i:i + n]


def get_xlsx_columns():
    xlsx_file_sheet_columns = list(ascii_letters[-26:])
    for combination in product(ascii_letters[-26:], repeat=2):
        xlsx_file_sheet_columns.append(''.join(combination))
    return xlsx_file_sheet_columns


