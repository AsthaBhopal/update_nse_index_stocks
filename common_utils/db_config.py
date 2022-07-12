import mysql.connector
from requests import get


def get_cms_db_conn():
    """
        * Use the db connection
        conn = get_cms_db_conn()
        cur = conn.cursor(buffered=True)
        cur.close()
        conn.close()
    """
    config = {
        'user': 'wwwastha_web',
        'password': 'EeM2wJAAmem5DdrMJQURCm5tvqEzFvEs',
        'host': 'astha-dev2.cwx3kboqzurw.ap-south-1.rds.amazonaws.com',
        'database': 'ashtha_cms',
        'raise_on_warnings': True,
        'autocommit': True,
        'connect_timeout': 1000,
    }
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except Exception as E:
        print("[ WARN ] : Failed connecting to CMS_DB")

def update_all_index_to_cms(index_details):
    """
    """
    print("[ INFO ] : upload_all_index_to_cms :")
    conn = get_cms_db_conn()
    cur = conn.cursor(buffered=True)
    for index_data in index_details:
        series = 'EQ'
        instrument_name = 'EQIDX'
        sql = f"""INSERT INTO ashtha_cms.flow_app_indexdata
                (scrip_token, market_segment_id, symbol, security_desc, eligibility, series, instrument_name)
                VALUES({index_data['nToken']}, {index_data['nMarketSegmentId']}, '{index_data['sIndex']}', '{index_data['sIndexDesc']}', 0, '{series}', '{instrument_name}')
                ON DUPLICATE KEY UPDATE  
                symbol = values(symbol),
                eligibility = values(eligibility), 
                security_desc = values(security_desc),
                series = values(series),
                instrument_name = values(instrument_name)
                ;"""
        # print(sql)
        try:
            cur.execute(sql)
            print(
                f"[ INFO ] : Successfully updated index {index_data['sIndexDesc']} > CMS_DB")
        except Exception as E:
            print(
                f"[ WARN ] : Failed to update index {index_data['sIndexDesc']} > CMS_DB",  E)
    cur.close()
    conn.close()


def update_index_stock_mapper_cms(index_stock_details):
    """
    * input : index_stock_details 


    """
    print("[ INFO ] : update_index_stock_mapper_cms :")
    conn = get_cms_db_conn()
    cur = conn.cursor(buffered=True)

    rows = ", ".join(str((indexdata_id, nsedata_id))
                     for indexdata_id, nsedata_id in index_stock_details)

    sql = f"""INSERT INTO ashtha_cms.flow_app_indexdata_stocks
            (indexdata_id, nsedata_id)
            VALUES {rows}
            ON DUPLICATE KEY UPDATE
            id = id ;"""

    # print(sql)

    try:
        cur.execute(sql)
        print(f"[ INFO ] : Successfully updated index_stock_mapper > CMS_DB")
    except Exception as E:
        print(f"[ WARN ] : Failed to update index_stock_mapper > CMS_DB",  E)

    cur.close()
    conn.close()


def get_index_stock_ids(index_data):
    # print("[ INFO ] : get_index_stock_ids :")
    conn = get_cms_db_conn()
    cur = conn.cursor(buffered=True)
    
    # Index
    try:
        # * HINT : 
        sql = f"""SELECT * FROM ashtha_cms.flow_app_indexdata WHERE market_segment_id=1 AND LOWER(TRIM(security_desc))=LOWER(TRIM('{index_data['index_name']}'));"""
        cur.execute(sql)
        resp = cur.fetchone()
        index_id = resp[0]

    except Exception as E:
        print(f"[ WARN ] : Failed CMS_DB INDEX Query",  E, sql)
        return None

    main_resp = []
    # Stocks
    for stock_symbol in index_data['index_stocks']:
       
        try:
            sql = f"""SELECT * FROM ashtha_cms.flow_app_nsedata where symbol='{stock_symbol}' and market_segment_id='1' and series='EQ';"""
            cur.execute(sql)
            resp = cur.fetchone()
            stock_id = resp[0]
            main_resp.append((index_id, stock_id))
        except Exception as E:
            print(f"[ WARN ] : Failed CMS_DB Stock Query",  E, sql)
        
    return main_resp



if __name__ == '__main__':
    if False:
        print("[ TEST ] : Insert Index Manually * This won't add all the index.")
        index_details = [
            {
                "nMarketSegmentId": 1,
                "nToken": 26000,
                "sIndex": "NIFTY",
                "sIndexDesc": "Nifty 50",
                "nIsDefaultIndex": 3,
                "cIsIndex": "Y"
            },
            {
                "nMarketSegmentId": 1,
                "nToken": 26009,
                "sIndex": "BANKNIFTY",
                "sIndexDesc": "Nifty Bank",
                "nIsDefaultIndex": 3,
                "cIsIndex": "Y"
            },
        ]
        upload_all_index_to_cms(index_details)

    if False:
        index_stock_details = [(26000, 910), (26000, 2475)]
        update_index_stock_mapper_cms(index_stock_details)


    if True:
        index_stock_details = {
            'index_name': 'NIFTY 50', 
            'index_stocks': ['APOLLOHOSP', 'ADANIPORTS', 'BHARTIARTL', 'TCS', 'AXISBANK', 'NTPC', 'WIPRO', 'SBIN', 'BAJAJ-AUTO', 'LT', 'COALINDIA', 'TECHM', 'ITC', 'SUNPHARMA',
                             'DRREDDY', 'HEROMOTOCO', 'KOTAKBANK', 'HINDUNILVR', 'ICICIBANK', 'RELIANCE', 'INDUSINDBK', 'BRITANNIA', 'MARUTI', 'EICHERMOT', 'POWERGRID', 
                             'HDFCLIFE', 'DIVISLAB', 'M&M', 'BAJFINANCE', 'HDFCBANK', 'INFY', 'ASIANPAINT', 'CIPLA', 'SBILIFE', 'ONGC', 'TATACONSUM', 'HCLTECH', 'TATAMOTORS', 
                             'NESTLEIND', 'BPCL', 'SHREECEM', 'GRASIM', 'ULTRACEMCO', 'HDFC', 'UPL', 'BAJAJFINSV', 'TITAN', 'TATASTEEL', 'JSWSTEEL', 'HINDALCO']}
        print(get_index_stock_ids(index_stock_details))