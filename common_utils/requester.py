import requests



def clean_index_data(api_resp):
    index_name = api_resp['latestData'][0]['indexName']
    index_stock_symbols = []
    for stock_details in api_resp['data']:
        index_stock_symbols.append(stock_details['symbol'])
    resp = {
        "index_name": index_name,
        "index_stocks": index_stock_symbols
    }

    return resp



def get_url_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'From': 'er.subarnasahoo@gmail.com'  # This is another valid field
    }
    try:
        response = requests.get(url, headers=headers).json()

        cleaned_data = clean_index_data(response)
        print("\n[ INFO ] :", cleaned_data['index_name'])

        return cleaned_data

    except Exception as E:
        print("\n[ ERROR ] : Not Required", E, url)
        return None



if __name__ == '__main__':
    all_index_urls = [
        'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json',
        'https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/bankNiftyStockWatch.json',
    ]
    print(get_url_data(all_index_urls[0]))