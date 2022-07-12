from distutils.command.upload import upload
import imp
from common_utils.scraper import scrap_all_index_urls
from common_utils.requester import get_url_data
from common_utils.odin_index_api import get_odin_index_details
from common_utils.db_config import update_all_index_to_cms, get_index_stock_ids, update_index_stock_mapper_cms


def main():
    """
    * Start
        - Scrap NSE Index Stocks
            - URL :- `https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm?cat=N`
            - Get all URLS of those Dynamic event of the DropDown
            
    """
    
    # Insert & Update Index From ODIN to CMS_DB
    # index_details = get_odin_index_details()
    # update_all_index_to_cms(index_details)

    # Get all Index's Stocks Table from Network URL 
    all_index_urls = scrap_all_index_urls()
    print("[INFO] : Successfully scraped all_index_urls")

    for url in all_index_urls:
        index_data = get_url_data(url)
        if index_data:
            index_stock_token_groups = get_index_stock_ids(index_data)
            if index_stock_token_groups:
                # * Finally Upload Index-Token and Stock-Token to Mapper(ashtha_cms.flow_app_indexdata_stocks)
                update_index_stock_mapper_cms(index_stock_token_groups)

    

if __name__ == '__main__':
    main()
